import pymysql
import socket
import json

class Prowo():
    '''
    Prowo网关API
    '''
    def __init__(self, ip, password, mode):
        # Prowo网关IP地址
        self.ip = ip
        # 数据库密码
        self.password = password
        # API模式
        self.mode = mode

    # 创建数据库连接
    def connectDB(self):
        conn = pymysql.connect(
            host=self.ip, 
            port=12306, 
            user='root', 
            passwd=self.password, 
            db='HiDockerwifi', 
            charset='utf8')
        return conn

    # 更新数据
    def execDB(self, sql):
        conn = self.connectDB()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    # 查询数据
    def get(self, sql):
        conn = self.connectDB()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is not None:
            result = result
        cursor.close()
        conn.close()
        return result

    # 查询设备信息
    def find(self, equipid):
        sql = 'select port from portdb where equip="' + \
            equipid + '"'
        result = self.get(sql)

        return result
    
    # 向下发送消息
    def socketClient(self, e_ip, e_port, message):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((e_ip, int(e_port)))
            s.sendall(message.encode())
            response = s.recv(1024).decode()
            return response
            # 此处需要加上判断
        except BaseException:
            #print("Connection refused Error")
            return None
        finally:
            s.close()

    # 获取HFV模块数据
    def connectDevice(self, equipid, method):
        if self.mode == 'host':
            result = self.find(equipid)
            if result is None:
                return False
            ipaddr = self.ip
            port = result[0]
        elif self.mode == 'docker':
            ipaddr = equipid
            port = 3000
        else:
            return False
        result = self.socketClient(ipaddr, int(port), method)
        if not result:
            #print("与docker无连接")
            return False
        else:    
            result = json.loads(result)
            #if result is None:
                #print('查询错误')           
                #return False
            return result

    def getData(self, equipid, command):
        return self.connectDevice(equipid, command)

    def execute(self, equipid, method):
        return self.connectDevice(equipid, method)


class DHT11():
    def __init__(self, p, equipid):
        self.equipid = equipid
        self.p = p

    def getTemperature(self):
        data = self.p.getData(self.equipid)
        return data


class waterDepth():
    def __init__(self, p, equipid):
        self.equipid = equipid
        self.p = p

    def getDepth(self):
        data = self.p.getData(self.equipid)
        return data


class Device():
    def __init__(self, p, equipid):
        self.equipid = equipid
        self.p = p

    def value(self):
        data = self.p.getData(self.equipid, "value_command")
        return data

    def do(self, method):
        data = self.p.execute(self.equipid, method)
        return data

    def health(self):
        data = self.p.getData(self.equipid, "health_command")
        return data

if __name__ == "__main__":
    #a = Prowo('192.168.31.229', 'Vudo3423', 'host')
    #cluster1 = Device(a, 'cluster1')
    #value = cluster1.value()
    #print(value)
    #cluster2 = Device(a,'cluster2')
    #result = cluster2.do('off')
    print(result)
    #for key in value.keys():
    #    print("%s:%s"%(key, value[key]))
    #fan = Device(a, 'switch006')
    #fan.do('on')
    #health = G_001.health()
    #print("health:", health)
