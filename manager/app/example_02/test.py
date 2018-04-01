import hfv
import time

while True:
    print(hfv.dht11_temp_humi('dht11v2.0','host'))
    time.sleep(10)

