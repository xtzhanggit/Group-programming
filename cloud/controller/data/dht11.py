import os
import db
import subprocess
import time
import sys

class DHT11:
    """硬件虚拟化基础类"""

    def __init__(self,equip,mode):
        self.equip = equip
        self.temp = 0
        self.humi = 0
        self.mode = mode

    def getData(self):
        result = db.find(self.equip)
        if result == None:
            return (False, 'not found this equip')
        (ipaddr, port) = result
        if self.mode == 'host' or self.mode == 'host_remote' or self.mode == 'docker_remote':
            ipaddr = os.getenv('HFV_HOST')
        elif self.mode == 'docker':
            ipaddr = self.equip
            port = 3000
        else:
            return (False, 'no this mode')

        cmd = 'python3 send.py ' + ipaddr + ' ' + str(port) + ' temp'
        (status, output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            (temp, humi) = output.split('&')
            return (temp, humi)
        else:
            return (False, output)
    
    def getTemperature(self):
        (self.temp, self.humi) = self.getData()
        return self.temp

    def getHumidity(self):
        (self.temp, self.humi) = self.getData()
        return self.humi

if __name__ == "__main__":
    equip = sys.argv[1]
    a = DHT11(equip, 'host')
    temp = a.getTemperature()
    humi = a.getHumidity()
    print(temp + '& '+ humi)
    
