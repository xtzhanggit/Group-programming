# !/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import json, types,string
import os, time
import subprocess
import logging
import pydb



def dhtfunc(sub_group):
    """
    dht processing module 
    """
    ip_list = get_AcDevIp('G_001', sub_group)
    if len(ip_list) > 0:
        print(ip_list)
        temp_list = []
        humi_list = []

        for item in ip_list:
            (status, output) = subprocess.getstatusoutput('python3 tcpclient.py ' + item)
            print ("client result:" + output)
            if output == "OSError":
                print("Degvice " + item + " is already offline")
                sql = "update " + sub_group + " set equip_status = 0 where equip_ip = '" + item + "'"
                pydb.db_exe(sql,'G_001')

            else:
                lists = output.split('&')
                if len(lists) == 1:
                    print('wrong')
                else:
                    temp_list.append(lists[0])
                    humi_list.append(lists[1])

        temp = getListAverage(temp_list)
        humi = getListAverage(humi_list)
        dresp = {'temp': temp ,'humi': humi}
    else:
        dresp = "No device available"
    print(dresp)
    return dresp


def lumifunc(sub_group):
    """
    lumi processing module 
    """
    ip_list = get_AcDevIp('G_001', sub_group)
    if len(ip_list) > 0:
        print(ip_list)
        lumi_list = []

        for item in ip_list:
            (status, output) = subprocess.getstatusoutput('python3 tcpclient.py ' + item)
            print ("client result:" + output)
            if output == "OSError":
                print("Degvice " + item + " is already offline")
                sql = "update " + sub_group + " set equip_status = 0 where equip_ip = '" + item + "'"
                pydb.db_exe(sql,'G_001')

            else:
                lumi_list.append(output)

        lumi = getListAverage(lumi_list)
        dresp = lumi
    else:
        dresp = "No device available"
    print(dresp)
    return dresp


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
