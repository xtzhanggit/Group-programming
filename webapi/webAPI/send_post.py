#:coding:utf-8
import requests

#data = {'params':'room_alarm','val':'1','notes':'test1'}
data = {'host':'10.0.9.6','user_name':'xjhuang','user_age':'1','user_weight':'67','user_height':'170','user_blood_sugar':'23','user_blood_pressure':'63/120'}
#data = {'host':'192.168.31.111','params':'body_humidity','val':'100','notes':"test"}

#r = requests.post("http://192.168.31.111:36666/todo/api/v1.0/update_user_monitor/", data=data)

#r = requests.post("http://192.168.31.111:36666/todo/api/v1.0/update_user_info/", data=data)
#r = requests.post("http://192.168.31.111:36666/todo/api/v1.0/update_iot_monitor/", data=data)
#data = {'params':'equip_humidity','uuids':'1000-00002','val':2,'notes':'test'}
r = requests.post("http://192.168.12.1:37779/todo/api/v1.0/update_user_info/", data=data)

print(r.text)
