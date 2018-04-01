#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import socketserver
import json, types,string
import os, time
import subprocess
import logging
import sqlite3

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    路由器监听程序
    负责监听设备接入请求，部署应用
    """
    def handle(self):
        logger = logging.getLogger("TCPServer")
        data = self.request.recv(1024).decode()
        list = data.split('&')
        if len(list) == 1:
            priority = 1
            app = 'last_version'
            data = list[0]
        else:
            data = list[0]
            priority = int(list[1])
            app = list[2]
        num = get_num(app)
        num = num + 1
        if data == 'on':
            if save_status(1, priority, app, num):
                (status, output) = subprocess.getstatusoutput('python3 tcpOnclient.py')
            else:
                output = 'busy'
        else:
            if save_status(1, priority, app, num):
                (status, output) = subprocess.getstatusoutput('python3 tcpOffclient.py')
            else:
                output = 'busy'

        jresp = output
        self.request.sendall(jresp.encode())
        if output != 'busy':
            time.sleep(30)
            save_status(0, float(priority)+0.5, app, num)
           
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def get_num(app):
    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE if not exists switch
                      (status int(5) NOT NULL default 0,priority int(5) NOT NULL default 0,app text,num int(8) NOT NULL default 0)
                   """)
    sql = "select num from switch where app='" + app + "'"
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is None:
        return 0
    else:
        return data[0]

def save_status(status, priority, app, num):
    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE if not exists switch
                      (status int(5) NOT NULL default 0,priority int(5) NOT NULL default 0,app text,num int(8) NOT NULL default 0)
                   """)
    sql = "select * from switch"
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is None:
        sql = "insert into switch values (" + str(status) + "," + str(priority) + ",'" + app + "'," + '0' +")"
        cursor.execute(sql)
        conn.commit()
        result = True
    else:
        (statusdb, prioritydb, appdb, numdb) = data
        if priority > prioritydb or appdb == app :
            if status == 0:
                
                if num < numdb and priority <= (prioritydb+0.5):
                    cursor.close()
                    conn.close()
                    return True
                
                priority = 0
                app = 'NULL'
                num = 0
            sql = "update switch set status=" + str(status) + ", priority=" + str(priority) + ',app="' + app + '",num=' + str(num)
            cursor.execute(sql)
            conn.commit()
            result = True
        else:
            result = False
    cursor.close()
    conn.close()
    return result

        
if __name__ == "__main__":
    #:设置host和port 
    HOST, PORT = "0.0.0.0", 3000
    save_status(0, float("inf"), 'NULL', 0)
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
