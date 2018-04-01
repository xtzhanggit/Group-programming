from tcpclient import control
import json
class DHT11():
    
    def __init__(self, username, password, equip, type):
        self.username = username
        self.password = password
        self.equip = equip
        self.type = type

    def getData(self):
        method = ''
        result = control(self.username, self.password, self.equip, method , self.type)
        data = eval(result['ans'])['ans']
        return data

    def getTemperature(self):
        if self.type != 'dht11':
            return 'error equip'
        return self.getData().split('&')[0]

    def getHumidity(self):
        if self.type != 'dht11':
            return 'error equip'
        return self.getData().split('&')[1].replace(' ','')


class Base():
    def __init__(self, username, password, equip, type):
        self.username = username
        self.password = password
        self.equip = equip
        self.type = type
    
    def getData(self):
        method = ''
        result = control(self.username, self.password, self.equip, method, self.type)
        data = eval(result['ans'])['ans']
        return data

class SoilHumidity(Base):
    def __init__(self, username, password, equip, type):
        super().__init__(username, password, equip, type)

    def getHumidity(self):
        return super().getData()

class Depth(Base):
    def __init__(self, username, password, equip, type):
        super().__init__(username, password, equip, type)

    def getDepth(self):
        return super().getData()

class Luminance(Base):
    def __init__(self, username, password, equip, type):
        super().__init__(username, password, equip, type)

    def getLuminance(self):
        return super().getData()

class Switch(Base):
    def __init__(self, username, password, equip, type):
        super().__init__(username, password, equip, type)
    
    def getData(self, method):
        result = control(self.username, self.password, self.equip, method, self.type)
        return result
    def execute(self, method):
        return self.getData(method)
         
if __name__ == '__main__':
    #dht11 = DHT11('joliu','123','dht11v2.0','dht11')
    #dep = Depth('joliu','123','soilHumidityv2.0','soilHumidity')
    #soi = SoilHumidity('joliu','123','waterSensorv2.0','depth')
    #lum = Luminance('joliu','123','luminancev2.0','luminance')
    #print(dht11.getTemperature())
    #print(dep.getDepth())
    #print(soi.getHumidity())
    #print(lum.getLuminance())
    swi = Switch('joliu','123','switchv2.0','switch')
    swi.execute('off')
