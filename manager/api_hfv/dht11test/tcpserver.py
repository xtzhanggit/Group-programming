# !/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import socketserver
import json, types,string
import os, time
import subprocess
import logging
import pydb
import pyfunc
import updateDevice
import threading

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    路由器监听程序
    负责监听设备接入请求，部署应用
    """
    def handle(self):
        logger = logging.getLogger("TCPServer")
        command = self.request.recv(1024).decode()
        if command == "health_command":
            # 暂时不用 
            """
            查询群体状态模块
            """    
            sql = "select health_degree from attributes where group_name = '" + "G_001" + "'" 
            dresp = pydb.db_get(sql, "Group_data")[0][0]
        elif command == 'on' or command == 'off':
            """
            调用模块
            """
            # 新建字典，存储各个子群体的指令处理结果
            subGroup_list = get_subGroup() # 子群体列表
            if len(subGroup_list) > 0:
                for sub_group in subGroup_list:
                    sub_data = groupCommandProcess(sub_group, command) # 对于所有子群体，得到子群体的指令处理结果
                    #dresp[sub_group] = sub_data
                    dresp = sub_data
            else:
                dresp = "No sub_group available"
            sql = "update group_table set group_value = '" + str(dresp) + "' where group_name = '" + os.getenv('GROUP_NAME') + "'"
            pydb.db_exe(sql, "Group_data")
        else:
            """
            查询模块
            """
            # 新建字典，存储各个子群体的信息处理结果
            subGroup_list = get_subGroup() # 子群体列表
            if len(subGroup_list) > 0:
                for sub_group in subGroup_list:
                    sub_data = groupDataProcess(sub_group) # 对于所有子群体，得到子群体的信息处理结果
                    #dresp[sub_group] = sub_data
                    dresp = sub_data
            else:
                dresp = "No sub_group available"

            sql = "update group_table set group_value = '" + str(dresp) + "' where group_name = '" + os.getenv('GROUP_NAME') + "'"
            pydb.db_exe(sql, "Group_data")
        jresp = json.dumps(dresp)
        self.request.sendall(jresp.encode())

        # out = subprocess.getoutput('python3 saveToMysql.py ' + temp + ' ' + humi)
        # print(out)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def groupDataProcess(sub_group):
    """
    对子群体中的设备按其调用方法进行调用,现有均为同类设备
    """
    ac_devs = get_AcDev(os.getenv('GROUP_NAME'), sub_group)
    if len(ac_devs) > 0:
        subgroup_class = ac_devs[0][1] # 子群体属性 
        resp = eval("pyfunc." + subgroup_class)(ac_devs, sub_group)
        return resp
    else:
        return "No dev available"   

def groupCommandProcess(sub_group,command):
    """
    对子群体中的设备按其调用方法进行调用,现有均为同类设备
    """
    ac_devs = get_AcDev(os.getenv('GROUP_NAME'), sub_group)
    if len(ac_devs) > 0:
        subgroup_class = ac_devs[0][1] # 子群体属性 
        resp = eval("pyfunc." + subgroup_class)(ac_devs, command, sub_group)
        return resp
    else:
        return "No dev available"   

def get_subGroup():
    """
    获取所有子群体名称
    """
    sql = "select subgroup_name from " + os.getenv('GROUP_NAME') 
    cur_result = pydb.db_get(sql, 'Group_data')
    subGroup_list = []
    if cur_result:
        for item in cur_result:
            subGroup_list.append(item[0])
    return subGroup_list

def get_AcDev(group, sub_group):
    """
    获取所有在线设备的ip地址
    """
    sql = "select e_ip, e_class from " + sub_group + " where e_status = 1"
    cur_result = pydb.db_get(sql, group)
    return cur_result

def server_thread():
    """
    server监听进程
    """
    #:设置host和port 
    HOST, PORT = "0.0.0.0", 3000

    logger = logging.getLogger("TCPServer")
    logger.setLevel(logging.INFO)

    # 创建句柄
    fh = logging.FileHandler("1.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -\
%(message)s')
    fh.setFormatter(formatter)

    # 添加句柄到logger类
    logger.addHandler(fh)

    logger.info("Program started")
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    #:启动多进程监听服务
    server_thread = threading.Thread(target=server.serve_forever)
    #:当主进程中断时退出程序
    server_thread.daemon = True
    server_thread.start()
    logger.info("Server loop running in thread:" + server_thread.name)
    logger.info(" .... waiting for connection")

    #:使用Ctrl + C退出程序
    server.serve_forever()

def updateDev_thread():
    """
    更新设备状态进程
    """
    while True:
        subGroup_list = updateDevice.get_subGroup()
        for item in subGroup_list:
            updateDevice.update_dev_sta(item)
        print("Do test_conn")
        time.sleep(600)
    
if __name__ == "__main__":
    thread_server = threading.Thread(target = server_thread, args=())   
    thread_updateDev = threading.Thread(target = updateDev_thread, args=())
    thread_server.start()
    thread_updateDev.start() 
    thread_server.join()
    thread_updateDev.join()
    print("双线程结束")
