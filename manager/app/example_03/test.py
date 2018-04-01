import hfv
import time

print(hfv.dht11_temp_humi('dht11v2.0','host'))
while True:
    print(hfv.switch('switchv2.0','host','off'))

    print(hfv.switch('switchv2.0','host','on'))

    time.sleep(10)

