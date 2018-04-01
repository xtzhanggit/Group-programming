import socketserver 
import subprocess 
import string 
import time 
import sys
class MyTcpServer(socketserver.BaseRequestHandler): 
    def recvfile(self, filename): 
        print("starting reve file!")
        f = open(filename, 'wb')
        self.request.send('ready'.encode())
        while True: 
            data = self.request.recv(4096).decode()
            if data == 'EOF': 
                print("recv file success!")
                break
            f.write(data.encode()) 
        f.close() 
                                         
    def sendfile(self, filename): 
        print("starting send file!")
        self.request.send('ready'.encode()) 
        time.sleep(1) 
        f = open(filename, 'rb') 
        while True: 
            data = f.read(4096) 
            if not data: 
                break
            self.request.send(data.encode()) 
        f.close() 
        time.sleep(1) 
        self.request.send('EOF'.encode()) 
        print("send file success!")
                                     
    def handle(self): 
        print("get connection from :" + str(self.client_address))
        while True: 
            try: 
                data = self.request.recv(4096).decode() 
                print("get data:" + str(data))
                if not data: 
                    print("break the connection!")
                    break                
                else: 
                    action, filename = data.split() 
                    if action == "put": 
                        self.recvfile(filename) 
                    elif action == 'get': 
                        self.sendfile(filename)  
                    else: 
                        print("gt error!")
                        continue
            except Exception as e: 
                print(e)
                                             
                                         
if __name__ == "__main__": 
    host = ''
    port = 9666
    s = socketserver.ThreadingTCPServer((host,port), MyTcpServer) 
s.serve_forever() 
