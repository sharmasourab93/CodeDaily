import time
import socket
import sys

print("\n Welcome to Chat room\n")
print("Initialising ...\n")
time.sleep(1)


s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\n Enter your name:"))
port = 1234
print("\n Trying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected ...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room \nEnter [e] to exit chat room")


while True:
				message = s.recv(1024)
				print(s_name, ":", message)
				message = input(str("Me : "))
				if message == "[e]":
								message = "left chat room!"
								s.send(message.encode())
								print("\n")
								break
				
				
				s.send(message.encode())
				