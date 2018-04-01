import time
import os
import socket
import pydb

def update_dev_sta():
    ip_list = getAcDevIp()
    if len(ip_list) > 0:
        print(ip_list)
        for item in ip_list:
            print(test_conn(item))
            if not test_conn(item):
                sql = "update " + os.getenv('GROUP_NAME') + " set equip_status = 0 where equip_ip = '" + item + "'"
                print(sql)
                pydb.db_exe(sql)
    else:
        print("No available device")

def test_conn(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 8085))
        s.sendall("test_connect".encode())
        response = s.recv(1024).decode()
        return True
    except OSError:
        return False
    finally:
        s.close()

def getAcDevIp():
    sql = "select equip_ip from " + os.getenv('GROUP_NAME') + " where equip_status = 1"
    ip_result = pydb.db_get(sql)
    ip_list = []
    if ip_result:
        for item in ip_result:
            ip_list.append(item[0])
    return ip_list

def db_get(sql):
    db = pymysql.connect("mysql_test", "root", "Vudo3423", "HiDockerwifi")
    cursor = db.cursor()
    cursor.execute(sql)
    cur_result = cursor.fetchall()
    cursor.close()
    db.close()
    return cur_result

def db_exe(sql):
    db = pymysql.connect("mysql_test", "root", "Vudo3423", "HiDockerwifi")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    while True:
        update_dev_sta()
        print("Do test_conn")
        time.sleep(3600)
