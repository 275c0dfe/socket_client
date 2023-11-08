import socket
import time
from importlib import reload

import handler

class client:
    def __init__(self) -> None:
        self.socket  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        self.connected = False
        self.config  = {"addr":("",0)}
    def connect(self , host:tuple)->None:
        self.config["addr"]  = host
        self.socket.connect(host)
        self.connected = True
        reload(handler)
        handler.on_connect(self)
    def disconnect(self) -> None:
        self.socket.close()
        reload(handler)
        handler.on_disconnect(self)
    def receive(self) -> None:
        data = self.socket.recv(2048)
        reload(handler)
        handler.on_recv(self , data) 
    def send(self , data:bytes) -> None:
        reload(handler)
        data = handler.on_send(self, data)
        self.socket.send(data)