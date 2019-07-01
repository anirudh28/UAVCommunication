#import os
#hostname = "google.com" #example
#response = os.system("ping -c 1 " + hostname)

#and then check the response...
#if response == 0:
  #print hostname, 'is up!'
#else:
  #print hostname, 'is down!'
import os
import socket
import sys
import time
port = 2000            # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = "192.168.43.79"
 
rep = 0
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = raw_input('Enter server IP ')
while(True):
	#time.sleep(10)
	rep = os.system('ping -c 1 '+server_ip)
	if rep == 0:
		print 'server is up'
		s.bind((host, port))           
		s.listen(5)         
		print 'Server listening....' # Now wait for client connection.
		while True:
			conn,addr = s.accept()
			print 'Got connection from', addr
			data = conn.recv(1024)
			print ('server recieved',repr(data))

			filename = 'mytext.txt'
			f = open(filename,'rb')
			l = f.read(1024)
			while(l):
				conn.send(l)
				print('Sent ',repr(l))
				l = f.read(1024)
			f.close()

			print('Done Sending')
			conn.send('Thank You for connecting')
			conn.close()
	else:
		print 'server is down'

		break
