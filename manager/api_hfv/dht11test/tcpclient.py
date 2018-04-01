import socket
import sys
import json
import os



def client(ip,port,message):
    """
    设备接入函数
    """
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        s.sendall(message.encode())
        response = s.recv(1024).decode()
        print(response)
    except OSError:
        print("OSError")
    finally:
        s.close()


if __name__ == "__main__":
    #:配置host和port
    HOST,PORT = os.getenv('HOST'),8085
    
    if len(sys.argv) != 2:
        print ("parameter is incorrect!")
        exit(1)
    #:构建发送消息

    #msg1 = [{'cmd':r'python3 /tmp/server+.py','equip':"xdlight1", 'log':"up",'repo':"xjhuang/light",'imname':"hiwifi/light","dcport":"33332"}]
    msg1 = '1'
    #:将json转化成可发送数据
    #jmsg1 = json.dumps(msg1)
    #list = GetGroupip()
    client(sys.argv[1], PORT, msg1)

