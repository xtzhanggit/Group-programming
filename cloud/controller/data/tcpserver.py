#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import socketserver
import json, types,string
import os, time
import logging
import subprocess

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    路由器监听程序
    负责监听设备接入请求，部署应用
    """
    def handle(self):
        logger = logging.getLogger("TCPServer")
        data = self.request.recv(1024).decode()
        jdata = json.loads(data)
        logger.info("Receive data from '%r'"% (data))
        #:设备唯一编码
        device = jdata['equipid']
        method = jdata['cmd']
        cmd = 'python3 prowo.py ' + device + ' "' + method + '"'
        output = subprocess.getoutput(cmd)
 
        cur_thread = threading.current_thread()
        #:构建json消息
        response = {'ip':'test','ans':output}
        jresp = json.dumps(response)
        self.request.sendall(jresp.encode())
           
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    print('started!')
    #:设置host和port 
    HOST, PORT = "0.0.0.0", 22223
    
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
