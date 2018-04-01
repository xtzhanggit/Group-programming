#!/usr/bin/python
#coding=utf-8
import socket
import sys
import json
import os

def client(ip,port,message):
    """
    设备接入函数
    """

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    try:
        print("Send:"+message)
        s.sendall(message.encode())
        response = s.recv(1024).decode()
        print(str(response))

    finally:
        s.close()

if __name__ == "__main__":
    #:配置host和port
    HOST,PORT = os.getenv('HOST'),8085
    #:构建发送消息

    #msg1 = [{'cmd':r'python3 /tmp/server+.py','equip':"xdlight1", 'log':"up",'repo':"xjhuang/light",'imname':"hiwifi/light","dcport":"33332"}]
    msg1 = 'off'
    #:将json转化成可发送数据
    #jmsg1 = json.dumps(msg1)
    client(HOST,PORT,msg1)
