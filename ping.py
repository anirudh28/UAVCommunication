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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = raw_input(‘Enter server IP : ‘)
while(true)
	rep = os.system(‘ping ‘ + server_ip)
	if rep == 0:
		print ‘server is up’
	else:
		print ‘server is down’
		break