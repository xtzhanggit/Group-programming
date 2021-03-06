#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import socketserver
import json, types,string
import os, time
import logging
import subprocess
import pymysql
import buildDock
import db
import login

os.chdir("/home/xtzhang/HiDockerwifi/manager/wifiserver")
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    路由器监听程序
    负责监听设备接入请求，部署应用
    """
    def handle(self):
        logger = logging.getLogger("TCPServer")
        data = self.request.recv(1024).decode()
        jdata = json.loads(data)
        logger.info("Receive data from '%r'"% (data))
        #:设备唯一编码
        rec_equip = jdata['equip']
        #:设备接入请求，判断不同业务
        rec_log = jdata['log']
        #:代码库
        repo = jdata['repo']
        #:镜像名
        imname = jdata['imname']
        #:应用启动预执行命令
        rec_cmd = jdata['cmd']
        #:设备ip地址
        rec_ipaddr = jdata['ip']
 
        #:是否参与群体;群体名称;是否参与子群体；子群体名称
        rec_group_status = jdata['group_status']
        rec_group_name = jdata['group_name']
        rec_sub_group_name = jdata['sub_group_name']
        
        #:设备类型
        rec_equip_category = jdata['equip_category']

        #:容器名
        if rec_group_status == 1:
            docker_name = rec_group_name
        else:
            docker_name = rec_equip

        #:设备注册流程
        #login.run('000-000-001', rec_equip)
        if rec_log == 'up':
            #:标记用户为接入但未部署应用
            status = 0
            #:接入时间
            timel = str(time.time()).split('.')[0]
            print("new equip:"+rec_equip)
            #:在equipdb数据表中注册设备
            sql = "insert into equipdb (equip,status,signintime,dockername,ipaddress,group_status,group_name,sub_group_name) values ('" + rec_equip +"'," + str(status)+","+str(timel)+",'"+imname+"','"+rec_ipaddr+"',"+str(rec_group_status)+",'"+rec_group_name+"','"+rec_sub_group_name+"')"
            db.exec(sql)
           	
            #:把设备在子群体中标识上线，并录入ip和设备类型；在群体密度上加1，上线设备数加1
            if rec_group_status == 1:
                #:设备上线
                sqlG = "update " + rec_sub_group_name + " set e_status = 1 where e_name = '" + rec_equip + "'"
                database_exec(sqlG, rec_group_name)
                #:登记设备ip
                sqlG = "update " + rec_sub_group_name + " set e_ip = '" + rec_ipaddr + "' where e_name = '" + rec_equip + "'"
                database_exec(sqlG, rec_group_name)                
                #:标记设备类型
                sqlG = "update " + rec_sub_group_name + " set e_class = '" + rec_equip_category + "' where e_name = '" + rec_equip + "'"
                database_exec(sqlG, rec_group_name)
                #:群体密度加1，上线设备数目加1
                #sqlG = "update attributes set population_density = population_density + 1, online_number = online_number + 1 where group_name = '" + rec_group_name + "'"
                #database_exec(sqlG, "Group_data")
            
            #:标记设备登录成功
            log_ans = True
            #:检查本地镜像库是否已经存在该镜像
            if not buildDock.checkim(imname):
                if buildDock.pulldc(imname):
                    flag = buildDock.run(imname,docker_name,rec_cmd,rec_ipaddr)
                    if flag[0]:
                        cmd_ans = True
                    else:
                        cmd_ans = False
                else:
                    print('pull failed')
                    cmd_ans = False

#以下为使用ftp下载的命令            
#                #:下载镜像
#                if buildDock.download(repo) and log_ans:
#                    #:载入镜像
#                    if buildDock.load(repo):
#                        #:运行镜像
#                        flag = buildDock.run(imname,rec_equip,dcport,rec_cmd)
#                        #:判断运行是否成功
#                        if flag[0]:
#                            cmd_ans = True
#                        else:
#                            cmd_ans = False
#                    else:
#                        cmd_ans = False
#                else:
#                    cmd_ans = False

            else:
                #:检查容器是否正在运行
                if not buildDock.checkdcing(docker_name):

                    #:检查是否已经创建过应用
                    if buildDock.checkdc(docker_name):
                        #:若存在应用，则启动容器，不创建
                        flag = buildDock.start(docker_name)
                        #:判断启动结果
                        if flag[0]:
                            cmd_ans = True
                        else:
                            cmd_ans = False

                    else:
                        #:创建并启用容器
                        flag = buildDock.run(imname,docker_name,rec_cmd,rec_ipaddr)
                        #:判断启动结果
                        if flag[0]:
                            cmd_ans = True
                        else:
                            cmd_ans = False
                else:
                    flag = buildDock.getPort(docker_name)
                    cmd_ans = True
                    
            

        #:该请求未完成，暂不使用    
        elif rec_log == 'in':
            status = 1
            timel = 1
            sql = 'update equipdb set status=1 where equip="'+rec_equip+"'"
            db.exec(sql)
            log_ans = True
            if builDock.start(rec_equip) and log_ans:
                cmd_ans = True
            else:
                cmd_ans = False
        else:
            log_ans = False
            cmd_ans = False
 
        cur_thread = threading.current_thread()
        #:构建json消息
        response = {'equip':rec_equip,'log_ans':log_ans,'cmd_ans':cmd_ans,'port':flag[1],'group_status':rec_group_status,'group_name':rec_group_name,'sub_group_name':rec_sub_group_name}
        jresp = json.dumps(response)
        self.request.sendall(jresp.encode())
           
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def database_exec(sql,database):
    conn = pymysql.connect(host = '127.0.0.1', port = 12306, user = 'root', passwd = 'Vudo3423', db = database, charset = 'utf8')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    cmd = 'docker start test-mysql'
    (status, output) = subprocess.getstatusoutput(cmd)
    if status != 0:
        exit(0)

    print('started!')

    #:设置host和port 
    HOST, PORT = "0.0.0.0", 22223
    
    logger = logging.getLogger("TCPServer")
    logger.setLevel(logging.INFO)

    # 创建句柄
    fh = logging.FileHandler("1.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -\
%(message)s')
    fh.setFormatter(formatter)

    # 添加句柄到logger类
    logger.addHandler(fh)

    logger.info("Program started")
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    #:启动多进程监听服务
    server_thread = threading.Thread(target=server.serve_forever)
    #:当主进程中断时退出程序
    server_thread.daemon = True
    server_thread.start()
    logger.info("Server loop running in thread:" + server_thread.name)
    logger.info(" .... waiting for connection")

    #:使用Ctrl + C退出程序
    server.serve_forever()
