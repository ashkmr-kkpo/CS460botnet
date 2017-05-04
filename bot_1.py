#!/usr/bin/python           # This is client.py file
import urllib
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 11111                # Reserve a port for your service.

s.connect((host, port))
receive= s.recv(1024)
if(receive== 'ddos'):
	getreq= urllib.urlopen("http://example.com")
	print(getreq.info())
	
s.close                     # Close the socket when done
