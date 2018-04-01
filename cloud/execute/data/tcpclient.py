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
        print(str(jresp))

    finally:
        s.close()

if __name__ == "__main__":
    host = sys.argv[1]
    cmd = sys.argv[2]
    
    #:配置host和port
    HOST,PORT = host, 22223
    #:构建发送消息

    #msg1 = [{'cmd':r'python3 /tmp/server+.py','equip':"xdlight1", 'log':"up",'repo':"xjhuang/light",'imname':"hiwifi/light","dcport":"33332"}]
    msg1 = {'cmd':cmd,'ip':'192123'}
    #:将json转化成可发送数据
    jmsg1 = json.dumps(msg1)
    client(HOST,PORT,jmsg1)
