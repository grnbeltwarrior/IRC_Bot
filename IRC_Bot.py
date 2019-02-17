#!/usr/bin/python3

# Not very high speed low drag but it works.

import socket
import time
import math

server = 'irc.root-me.org'
port = 6667
nickname = 'Py_Botv2'
channel = '#root-me_challenge'
bot = 'Candy'

# Create socket
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect
ircsock.connect((server, port))
print("Connected to: %s:%s" % (server, port))

# Login
ircsock.send(bytes("USER " + nickname + " " + nickname + " " + nickname + " " + nickname + "\n", "utf-8"))
ircsock.send(bytes("NICK " + nickname + "\n", "utf-8"))
while 1:
	text = ircsock.recv(2048).decode("utf-8")
	text = str(text)
	if "is now your displayed host" in text:
		print(text)
		break
	else:
		print(text)
print("Logged in...")

# Join
ircsock.send(bytes("JOIN " + channel + "\n", "utf-8"))
print("Joined " + channel)

while 1:
	text = ircsock.recv(2040)
	text = str(text)
	if "PRIVMSG " + nickname in text:
		print(text)
	if "PING :" in text:
		print(text)
		ircsock.send(bytes("PONG :pingis\n", "utf-8"))

	else:
		ircsock.send(bytes("PRIVMSG Candy :!ep1\n", "utf-8"))
		datarecv = ircsock.recv(2048).decode("utf-8")
		print(datarecv)
		# Do work bay bay
    # redacted per Root-Me guidance. No spoilers or answser. The solutions are online elsewhere.
		print(returned)
		break
ircsock.close()
