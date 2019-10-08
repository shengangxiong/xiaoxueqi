# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:39:09 2019

@author: liyunxuan
"""

import socket

host="127.0.0.1"
client="127.0.0.1"
port=8188


print("get started")
while True:
        sock_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock_client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock_client.bind((client,port))
        sock_client.listen(100)
        clientsock,client_address=sock_client.accept()
        clientsock.send(b'client')
        while True:
            command=clientsock.recv(1024)
            print(command)
"""
            if command.isdigit():
                print(command)
#clientsock.close()

            else:
                print("wrong message")
           # se=input()
           # clientsock.send((se).encode("utf-8"))   
"""
    