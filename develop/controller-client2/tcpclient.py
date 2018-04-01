#!/usr/bin/python
#coding=utf-8
import socket
import sys
import json

def client(ip,port,message):
    """
    设备接入函数
    """

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    try:
        s.sendall(message.encode())
        response = s.recv(1024).decode()
        jresp = json.loads(response)

    finally:
        s.close()
        return jresp

def control(username, userpassword, ipaddr, equip, method):
    
    #:配置host和port
    HOST,PORT = 'opengn.org', 22223
    #:构建发送消息

    msg1 = {'name':username,'password':userpassword,'ipaddress':ipaddr,'equipid':equip,'method':method}
    #:将json转化成可发送数据
    jmsg1 = json.dumps(msg1)
    return client(HOST,PORT,jmsg1)

if __name__ == '__main__':
    print(control('jl','da','10.0.9.3','dht11v21.0','value&'))

