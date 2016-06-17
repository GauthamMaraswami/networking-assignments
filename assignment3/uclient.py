#!/usr/bin/env python   
import socket

# This is an example of a UDP client - it creates
# a socket and sends data through it

# create the UDP socket
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = " welcome\n"

# Simply set up a target address and port ...
addr = ("localhost",21561)
# ... and send data out to it!
UDPSock.sendto(data,addr)
data='h'

while data!='bye':
   data,addr = UDPSock.recvfrom(1024)
   print data.strip(),addr
   print ('enter the message')
   data=raw_input()
   UDPSock.sendto(data,addr)
UDPSock.close()

