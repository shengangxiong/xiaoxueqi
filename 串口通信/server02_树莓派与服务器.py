# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:42:42 2019

@author: liyunxuan
"""
import socket
import os
def read():
    with open(r"/home/xiaoxueqi/darknet/test.txt",'r',encoding='utf-8') as f:
             lines=[] # 创建了一个空列表，里面没有元素
             for line in f.readlines():
                 if line!='\n':
                    lines.append(line.strip('\n'))
    f.close()
    return lines

def commun(line):
    s=socket()
    s.connect(('127.0.0.1',8888))
    while True:
        s.send(line)
    #s.send(line + "\r\n")
        print(line)
    f.close()
    s.close()

if __name__ == "__main__":
    line=read()
    commun(line)