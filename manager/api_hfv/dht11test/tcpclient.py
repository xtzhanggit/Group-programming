import socket
import sys
import json
import os
import pydb


def client(ip, port, message, sub_group):
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
        sql = "update " + sub_group + " set e_status = 0 where e_ip = '" + ip + "'"
        pydb.db_exe(sql, os.getenv('GROUP_NAME'))
        print(sql)
        #sql = "update attributes set population_density = population_density - 1, offline_number = offline_number + 1 where group_name = 'G_001'"
        #pydb.db_exe(sql, "Group_data")
    finally:
        s.close()


if __name__ == "__main__":
    #:配置host和port
    HOST,PORT = os.getenv('HOST'),8085
    
    if len(sys.argv) != 4:
        print ("parameter is incorrect!")
        exit(1)
    #:构建发送消息

    #msg1 = [{'cmd':r'python3 /tmp/server+.py','equip':"xdlight1", 'log':"up",'repo':"xjhuang/light",'imname':"hiwifi/light","dcport":"33332"}]
    msg1 = sys.argv[2]
    sub_group = sys.argv[3]
    #:将json转化成可发送数据
    #jmsg1 = json.dumps(msg1)
    #list = GetGroupip()
    client(sys.argv[1], PORT, msg1, sub_group)

