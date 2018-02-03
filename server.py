import socket
import sys
from _thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host, port))
except socket.error as e:
	print(str(e))

s.listen(5)
print('Waiting for a connection.')
def threaded_client(conn):
	conn.send(str.encode('Welcome, type your info\n'))

	while True:
		data = conn.recv(2048) #buffer rate
		reply = 'Server output: '+ data.decode('utf-8')
		if not data:
			break
		conn.sendall(str.encode(reply))
	conn.close()
	print ('connection lost: ' +addr[0]+':'+str(addr[1]))			

while True:

	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))

	start_new_thread(threaded_client, (conn,))











































# import socket
# import threading
#
# sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tells the socket that it's going to send socket using ipv4 and second param tells to set a tcp connection
#
# sock.bind(('0.0.0.0', 10000))
#
# sock.listen(1)
#
# connections=[]
#
# def handler(c, a):
# 	global connections
# 	while True:
# 			data=c.recv(3024)
# 			for connection in connections
# 				connection.send(bytes(data))
# 			if not data:
# 			connections.remove(c)
# 			c.close()
# 			break
#
# while True:
# 	c, a=sock.accept()
# 	cThread=threading.Thread(target=handler, args=(c,a))
# 	cThread.daemon=True #program can exit regardless of threads running
# 	cThread.start()
# 	connections.append(c)
# 	print(connections)
