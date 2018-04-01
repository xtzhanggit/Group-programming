from switch import Switch
from dht11 import DHT11
import time

while True:
    b = Switch('switch002',"host", "on")
    a = DHT11('dht11v2.0', 'host')
    temp = a.getHumidity()
    print(temp)
    if float(temp) > 80:
        print('c')
        b.execute('on')
        time.sleep(2)
        b.execute('off')
    time.sleep(1)


