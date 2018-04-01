import subprocess
import db

def dht11_temp_humi(equip,mode):
    '''
    获取温湿度api接口
    equip: 设备上贴着的传感器序列号
    mode: 支持once / always两种参数，once只进行一个温湿度数据读取，always自动周期性读取，并保存至数据库中。
    ctime: int 在always模式下生效，单位秒，默认60s
    '''
    result = db.find(equip)
    if result == None:
        return (False, 'not found this equip')
    (ipaddr, port) = result
    if mode == 'host':
        ipaddr = ipaddr
    elif mode == 'docker':
        ipaddr = equip
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

def switch(equip,mode):
    result = db.find(equip)
    if result == None:
        return (False, 'not found this equip')
    (ipaddr, port) = result
    if mode == 'host':
        cmd = 'python3 send.py ' + ipaddr + ' ' + str(port) + ' True'
        (status, output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            return output
        else:
            return (False, output)
    elif mode == 'docker':
        print('failed')
        return (False, 'mode error')
    else:
        return (False, 'no this mode')

if __name__ == '__main__':
    print(switch('switch','host'))


