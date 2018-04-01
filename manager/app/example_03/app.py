import hfv
import time

while True:
    (temp, humi) = hfv.dht11_temp_humi('dht11v2.0','host')
    print(temp)
    time.sleep(10)


