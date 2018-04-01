import time

from prowo import Device
from prowo import Prowo

# 创建Prowo连接
p = Prowo('127.0.0.1', 'Vudo3423', 'host')
# 实例化风扇
fan = Device(p, 'switch001')
# 启动风扇
fan.do('on')

time.sleep(5)

# 关闭风扇
fan.do('off')

