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

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    路由器监听程序
    负责监听设备接入请求，部署应用
    """
    def handle(self):
        logger = logging.getLogger("TCPServer")
        data = self.request.recv(1024).decode()
        
        dresp = groupDataProcess()

        jresp = json.dumps(dresp)
        self.request.sendall(jresp.encode())

            # out = subprocess.getoutput('python3 saveToMysql.py ' + temp + ' ' + humi)
            # print(out)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def groupDataProcess():
    """
    Group information processing module 
    """
    ip_list = get_AcDevIp()
    if len(ip_list) > 0:
        print(ip_list)
        temp_list = []
        humi_list = []

        for item in ip_list:
            (status, output) = subprocess.getstatusoutput('python3 tcpclient.py ' + item)
            print ("client result:" + output)
            if output == "OSErrpr":
                print("Degvice " + item + " is already offline")
                sql = "update " + os.getenv('GROUP_NAME') + " set equip_status = 0 where equip_ip = '" + item + "'"
                pydb.db_exe(sql)

            else:
                lists = output.split('&')
                if len(lists) == 1:
                    print('wrong')
                else:
                    temp_list.append(lists[0])
                    humi_list.append(lists[1])

        temp = getListAverage(temp_list)
        humi = getListAverage(humi_list)
        dresp = {'temp': temp ,'humi': humi}
    else:
        dresp = "No device available"
    print(dresp)
    return dresp

def getListAverage(data_list):
    if len(data_list) > 0:
        sum = 0
        for item in data_list:
            sum += float(item)
        result = sum / len(data_list)
    else:
        result = "No data available"
    return result

def get_AcDevIp():
    """
    获取所有在线设备的ip地址
    """
    sql = "select equip_ip from " + os.getenv('GROUP_NAME') + " where equip_status =1"
    cur_result = pydb.db_get(sql)
    ip_list = []
    if cur_result:
        for item in cur_result:
            ip_list.append(item[0])
    return ip_list



if __name__ == "__main__":
    #:设置host和port 
    HOST, PORT = "0.0.0.0", 3000
    #HOST, PORT = "0.0.0.0", 33342

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
