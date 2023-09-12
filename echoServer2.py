#!/usr/bin/env python3
import socket


def tcp_echo():
    s = socket.socket()#AF_INET and SOCK_STREAM by default
    s.connect(('127.0.0.1', 55550))
    s.sendall(b'hello world')
    echodata = s.recv(4096)
    print(echodata)

   # while True:
   #     conn,address = s.accept()
   #     print(f'connection accepted from {address}')
   #     conn.sendall(conn.recv(4096))
   #     conn.close()


def udp_echo():
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.sendto(b'hello world',('127.0.0.1', 55550))
    echodata,address = s.recvfrom(4096)
    print(echodata)

    #while True:
    #    data,address = s.recvfrom(4096)
    #    print(data, f' received from {address}')
    #    s.sendtp(data.address)


if __name__ == '__main__':
    udp_echo()
