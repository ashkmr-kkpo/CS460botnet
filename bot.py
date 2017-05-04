#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
receive= s.recv(1024)
if(receive== 'ddos'):
	print("waddup")
s.close                     # Close the socket when done testnew
