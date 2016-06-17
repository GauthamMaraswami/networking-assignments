#!/usr/bin/env python         

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12348                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
msg='h'

while msg!='bye':
   print s.recv(1024)
   print ('enter the message')
   msg=raw_input()
   s.send('client:'+msg)
  
s.close()
