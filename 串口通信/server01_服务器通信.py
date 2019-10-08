import socket
import os
import sys
def socket_service_data():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #s.bind(('127.0.0.1', 6666))  # 在同一台主机的ip下使用测试ip进行通信

        s.bind(('127.0.0.1', 8888))  #在不同主机或者同一主机的不同系统下使用实际ip

        s.listen(10)

    except socket.error as msg:

        print(msg)

        sys.exit(1)

    print("Wait for Connection..................")

    while True:

        sock, addr = s.accept()

        buf = sock.recv(1024)  #接收数据

        buf = buf.decode()  #解码

        print("The data from " + str(addr[0]) + " is " + str(buf))

        print("Successfully")

        # return buf

        # sock.close()

if __name__ == '__main__':

    socket_service_data()