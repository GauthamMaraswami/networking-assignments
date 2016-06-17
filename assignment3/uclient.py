#!/usr/bin/env python   
import socket
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = " welcome\n"
addr = ("localhost",21561)

UDPSock.sendto(data,addr)
data='h'

while data!='bye':
   data,addr = UDPSock.recvfrom(1024)
   print data.strip(),addr
   print ('enter the message')
   data=raw_input()
   UDPSock.sendto(data,addr)
UDPSock.close()

