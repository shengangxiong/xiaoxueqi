
from socket import *
import threading
s=socket()
s.connect(('127.0.0.1',8888))
f=open(r'C:\Users\lenovo\Desktop\test0.jpg','rb')
while True:
     data=f.read(1024)
     if not data:
         break
     s.send(data)
f.close()
s.close()