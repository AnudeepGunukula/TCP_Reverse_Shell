from socket import *
from sys import *
import time

host = "localhost"
port=4444
print("reciver started")
s=socket(AF_INET,SOCK_STREAM)

s.bind((host,port))

s.listen(20)

while True:
	c,addr=s.accept()
	f_name=c.recv(1024).decode('utf-8')

	with open(f_name,'wb') as f:
		print("file opened")
		while True:
			print("recieving data")
			data=c.recv(99999999)
			if not data:
				break
			f.write(data)
	print('success')

					
