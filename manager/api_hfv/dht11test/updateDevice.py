import time
import os
import socket
import pydb

def update_dev_sta(sub_group):
    ip_list = getAcDevIp(sub_group)
    if len(ip_list) > 0:
        print(ip_list)
        for item in ip_list:
            conn_flag = test_conn(item)
            print(conn_flag)
            if not conn_flag:
                sql = "update " + sub_group + " set e_status = 0 where e_ip = '" + item + "'"
                pydb.db_exe(sql, os.getenv('GROUP_NAME'))
                print(sql)
                #sql = "update attributes set population_density = population_density - 1, offline_number = offline_number + 1 where group_name = 'G_001'"
                #pydb.db_exe(sql, "Group_data")
                #print(sql)
    else:
        print("No device available")

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

def getAcDevIp(sub_group):
    sql = "select e_ip from " + sub_group + " where e_status = 1"
    ip_result = pydb.db_get(sql, os.getenv('GROUP_NAME'))
    ip_list = []
    if ip_result:
        for item in ip_result:
            ip_list.append(item[0])
    return ip_list

def get_subGroup():
    sql = "select subgroup_name from " + os.getenv('GROUP_NAME')
    cur_result = pydb.db_get(sql, 'Group_data')
    subGroup_list = []
    if cur_result:
        for item in cur_result:
            subGroup_list.append(item[0])
    return subGroup_list

if __name__ == "__main__":
    while True:
        subGroup_list = get_subGroup()
        for item in subGroup_list:
            update_dev_sta(item)
        print("Do test_conn")
        time.sleep(20)
