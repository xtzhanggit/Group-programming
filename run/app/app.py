import time

from prowo import Device
from prowo import Prowo

startT = time.time()
# 创建Prowo连接
p = Prowo('192.168.12.1', 'Vudo3423', 'host')
# 实例化风扇
fan = Device(p, 'switch101')
# 实例化警报器
#alarm = Device(p, 'switch006')
# 实例化温传
dht11 = Device(p, 'dht11v21.0')

while True:
    temperature = dht11.value()[0]
    print(temperature)
    if  temperature > 24.0:
        # 启动风扇
        fan.do('on')
        #alarm.do('on')
    else:
        fan.do('off')
        #alarm.do('off')
    
    time.sleep(2)
    runT = time.time()
    if runT - startT > 60:
        break

time.sleep(5)

# 关闭风扇
fan.do('off')
