import os
import db
import subprocess
import time
class Luminance:
    """硬件虚拟化基础类"""

    def __init__(self,equip,mode):
        self.equip = equip
        self.value = -1
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
            return output
        else:
            return False
    
    def getLuminance(self):
        self.value = self.getData()
        return self.value

if __name__ == "__main__":
    a = Luminance('luminancev2.0', 'host')
    depth = a.getLuminance()
    print(depth)
    
