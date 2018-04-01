import subprocess
import os
import db
import configparser
import logging

#:从配置信息中读取配置信息
module_logger = logging.getLogger("TCPServer.buildDock")

config = configparser.ConfigParser()
config.read('db.ini')
ftphost = config.get("FTP","host")
registry_host = config.get("Registry","host")
output = subprocess.getoutput('uname -a')
output = output.split(' ')
version = output[12]
def pulldc(imname):
    """
    从私有库拉去镜像
    """
    logger = logging.getLogger("TCPServer.buildDock.pulldc")
    if version != 'x86_64':
        imname = imname + '-arm'
    full_imname = registry_host + '/' + imname
    print(full_imname)
    cmd = "docker pull " + full_imname
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        logger.info("pull from registry success!")
        return True
    else:
        logger.error("pull from registry failed!")
        return False

def checkdc(equip):
    """
    检查是否存在已equip为名字的容器应用
    """
    logger = logging.getLogger("TCPServer.buildDock.checkdc")
    #:查看全部应用
    cmd = r"docker ps -a | awk '{print $NF}' | sed 1d | sort"
    (status,output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        dockers = output.split('\n')
        #:返回是否存在
        if equip in dockers:
            return True
        else:
            return False
    else:
        logger.error("docker cmd is not running!")
        return False

def checkdcing(equip):
    """
    检查以equip为名字的容器应用是否正在运行
    """
    logger = logging.getLogger("TCPServer.buildDock.checkdcing")
    #:查看全部应用
    cmd = r"docker ps | awk '{print $NF}' | sed 1d | sort"
    (status,output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        dockers = output.split('\n')
        #:返回是否存在
        if equip in dockers:
            return True
        else:
            return False
    else:
        logger.error("docker is not running!")
        return False

def checkim(imname,force=False):
    '''
    检查是否存在该镜像
    '''
    logger = logging.getLogger("TCPServer.buildDock.checkim")
    #:force为真强制不检查镜像
    if not force:
        #:获取全部的镜像
        cmd = r"docker images | awk '{print $1,$2}' | sed 1d |sort"
        (status,output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            images = output.split('\n')
            imlist = imname.split(':')
            imname = imlist[0]
            tag = 'latest'
            if len(imlist) == 2:
                tag = imlist[1]
            imname = registry_host + '/' + imname + ' ' + tag
            if version != 'x86_64':
                imname = imname + '-arm'

            if imname in images:
                logger.info("image exists!")
                return True
            else:
                logger.info("image not exists!")
                return False
        else:
            return False
    else:
        logger.info("force is False")
        return False

def build(repo,imname):
    """
    使用dockerfile构建容器
    """
    logger = logging.getLogger("TCPServer.buildDock.build")
    repo = '112.74.171.161/' + repo
    if os.path.isdir(repo):
        cmd = "docker build -t "+imname+" "+repo
        (status, output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            logger.info("build success!")
            return True
        else:
            logger.error("build failed:" + cmd)
            return False

def load(repo):
    '''
    加载镜像
    '''
    #:下载目录
    repo = str(ftphost) + '/' + repo + '.tar'
    #:判断是否存在
    if os.path.isfile(repo):
        cmd = "docker load < " + repo
        (status,output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            print("load success!")
            return True
        else:
            print("load failed!")
            print(output)
            return False

def download(repo):
    """
    从FTP服务器下载镜像
    """
    #:判断是否已经下载过该镜像
    if not os.path.exists(str(ftphost) + '/' + repo + '.tar'):
        cmd = "wget -r --no-passive-ftp ftp://uftp:WyrXa9@" +str(ftphost)+ "/" + repo + '.tar'
        (status, output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            print("download success!")
            return True
        else:
            print("download failed!")
            return False
    else:
        print("download successed before!")
        return True

def run(imname,equip,rec_cmd,ipaddr):
    """
    启动容器
    """
    imname = registry_host + '/' + imname
    if version != 'x86_64':
        imname = imname + '-arm'
    logger = logging.getLogger("TCPServer.buildDock.run")

    #:提取未使用的端口
    sql = "select port from portdb where equip='" + equip + "'"
    hostport = db.get(sql)
    if hostport == None:
        sql = "select port from portdb where status=0 limit 1"
        hostport = db.get(sql)
    #:应用启动命令
    cmd = "docker run -it --name " + equip + " -d -p " + str(hostport) + ":3000 -P --link=test-mysql:mysql_test -e HOST=" + ipaddr + " -e GROUP_NAME=" + equip + " " + imname + " " + rec_cmd
    print(cmd)
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        logger.info("docker is running!")
        #:将端口号标记为占用
        sql = 'update portdb set status=1,equip="'+equip+'",ipaddress="'+ipaddr+'" where port='+str(hostport)
        db.exec(sql)
        #:返回执行结果和端口号
        flag = [True,hostport]
    else:
        logging.error("docker cannot run!")
        print(cmd)
        flag = [True,hostport]
    return flag

def start(equip):
    """
    启动容器
    """
    logger = logging.getLogger("TCPServer.buildDock.start")
    cmd = "docker start " + equip
    (status,output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        logger.info("docker starts!")
        sql = 'select port from portdb where equip="'+equip+'"'
        hostport = db.get(sql)
        flag = [True,hostport]
    else:
        logger.info("docker cannot run!:" + cmd)
        flag = [False,None]
    return flag


def getPort(equip):
    """
    获取docker的端口号
    """
    logger = logging.getLogger("TCPServer.buildDock.getPort")
    sql = 'select port from portdb where equip="'+equip+'"'
    hostport = db.get(sql)
    flag = [True,hostport]
    return flag


if __name__ == "__main__":
    print(checkim("hfv/dht11:v2.0"))
    #pulldc('mysql')
    #download("joliu/debian")
    #load("joliu/debian")
    #build("joliu","jo/mysqll")

