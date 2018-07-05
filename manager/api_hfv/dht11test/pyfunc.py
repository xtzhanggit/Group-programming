# !/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import json, types,string
import os, time
import subprocess
import logging
import pydb

def temp(ac_devs, sub_group):
    """
    temp子群体方法
    """
    temp_data = 0
    humi_data = 0
    available_num = 0
    for item in ac_devs:
        e_ip = item[0]
        (status, output) = subprocess.getstatusoutput('python3 tcpclient.py  ' + e_ip + ' value_command ' + sub_group)
        print ("client result:" + output)
        if output == "OSError":
            print("Degvice " + e_ip + " is already offline")
        else:
            lists = output.split('&')
            if len(lists) == 1:
                print('wrong')
            else:
                available_num += 1
                temp_data += float(lists[0])
                humi_data += float(lists[1])
    if available_num > 0:
        temp_data = temp_data / available_num
        humi_data = humi_data / available_num
    return temp_data

def humi(ac_devs, sub_group):
    """
    humi子群体方法
    """
    temp_data = 0
    humi_data = 0
    available_num = 0
    for item in ac_devs:
        e_ip = item[0]
        (status, output) = subprocess.getstatusoutput('python3 tcpclient.py  ' + e_ip + ' value_command ' + sub_group)
        print ("client result:" + output)
        if output == "OSError":
            print("Degvice " + e_ip + " is already offline")
        else:
            lists = output.split('&')
            if len(lists) == 1:
                print('wrong')
            else:
                available_num += 1
                temp_data += float(lists[0])
                humi_data += float(lists[1])
    if available_num > 0:
        temp_data = temp_data / available_num
        humi_data = humi_data / available_num
    return humi_data

def switch(ac_devs, command, sub_group):
    """
    switch子方法
    """
    available_num = 0 
    for item in ac_devs: 
        e_ip = item[0]
        (status, output) = subprocess.getstatusoutput('python3 tcpclient.py  ' + e_ip + ' ' + command + ' ' + sub_group)
        print ("client result:" + output)
        if output == "OSError":
            print("Degvice " + e_ip + " is already offline")
        else:
            available_num += 1
    return available_num > 0


def getListAverage(data_list):
    if len(data_list) > 0:
        sum = 0
        for item in data_list:
            sum += float(item)
        result = sum / len(data_list)
    else:
        result = "None"
    return result


def get_AcDevIp(group, sub_group):
    """
    获取所有在线设备的ip地址
    """
    sql = "select equip_ip from " + sub_group + " where equip_status =1"
    cur_result = pydb.db_get(sql, group)
    ip_list = []
    if cur_result:
        for item in cur_result:
            ip_list.append(item[0])
    return ip_list


if __name__ == "__main__":
    print("test")
