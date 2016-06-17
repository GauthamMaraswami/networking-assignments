#!/usr/bin/env python   
import socket
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_addr = ("",21561)
UDPSock.bind(listen_addr)
while True:
        data,addr = UDPSock.recvfrom(1024)
        print data.strip(),addr
        data='hi'
        while(data!='bye'):
          print('enter the message')
          data=raw_input() 
          UDPSock.sendto(data,addr)
          data,addr = UDPSock.recvfrom(1024)
          print data.strip(),addr
        UDPSock.close()
