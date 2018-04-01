import subprocess
import db
import os
import time

class Switch:
    def __init__(self, equip, mode, method='e'):
        self.equip = equip
        self.mode = mode
        self.result = 0

    def getData(self,method):
        result = db.find(self.equip)
        if result == None:
            return False
        (ipaddr, port) = result
        if self.mode == 'host' or self.mode == 'host_remote' or self.mode == 'docker_remote':
            ipaddr = os.getenv('HFV_HOST')
        elif self.mode == 'docker':
            ipaddr = self.equip
            port = 3000
        else:
            return False

        cmd = 'python3 send.py ' + ipaddr + ' ' + str(port) + ' ' + method
        (status, output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            return output
        else:
            return False

    def execute(self, method):
        self.result = self.getData(method)

if __name__ == '__main__':
    #a = Switch("switchv2.0","host","on")
    a = Switch("switch001","host","on")
    #a.execute('on')
    #time.sleep(5)
    #a.execute('off')
    #a = Switch("switch006","host","on")
    time.sleep(2)
