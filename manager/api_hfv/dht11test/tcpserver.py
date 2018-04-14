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

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    路由器监听程序
    负责监听设备接入请求，部署应用
    """
    def handle(self):
        logger = logging.getLogger("TCPServer")
        data = self.request.recv(1024).decode()
        
        # 新建字典，存储各个子群体的信息处理结果
        dresp = {}
        subGroup_list = get_subGroup() # 子群体列表
        for sub_group in subGroup_list:
            sub_data = groupDataProcess(sub_group) # 对于所有子群体，得到子群体的信息处理结果
            dresp[sub_group] = sub_data

        jresp = json.dumps(dresp)
        self.request.sendall(jresp.encode())

        # out = subprocess.getoutput('python3 saveToMysql.py ' + temp + ' ' + humi)
        # print(out)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def groupDataProcess(sub_group):
    """
    Group information processing module 
    """
    function = get_sub_function('G_001', sub_group)
    print("\n"+"***********************")
    print(function + " start")
    if function == "dht_function":
        return pyfunc.dhtfunc(sub_group)
    elif function == "lumi_function":
        return pyfunc.lumifunc(sub_group)

def getListAverage(data_list):
    if len(data_list) > 0:
        sum = 0
        for item in data_list:
            sum += float(item)
        result = sum / len(data_list)
    else:
        result = "No data available"
    return result

def get_subGroup():
    sql = "select sub_group from " + "G_001" 
    cur_result = pydb.db_get(sql, 'Group_data')
    subGroup_list = []
    if cur_result:
        for item in cur_result:
            subGroup_list.append(item[0])
    return subGroup_list

def get_AcDevIp(group, sub_group):
    """
    获取所有在线设备的ip地址
    """
    sql = "select equip_ip from " + sub_group + " where equip_status =1"
    cur_result = pydb.db_get(sql, group)
    ip_list = []
    if cur_result:
        for item in cur_result:
            ip_list.append(item[0])
    return ip_list

def get_sub_function(sub, sub_group): 
    """
    Group information processing module 
    """
    sql = "select function from " + sub + " where sub_group = '" + sub_group + "'"
    cur_result = pydb.db_get(sql, 'Group_data')
    if cur_result:
        return cur_result[0][0]

if __name__ == "__main__":
    #:设置host和port 
    #HOST, PORT = "0.0.0.0", 3000
    HOST, PORT = "0.0.0.0", 33341

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
