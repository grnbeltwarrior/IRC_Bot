#!/usr/bin/python3

import base64
import codecs
import math
import socket
import sys
import time
import zlib

server = 'irc.root-me.org'
port = 6667
nickname = 'Py_Botv2'
channel = '#root-me_challenge'
bot = 'Candy'

user = "USER %s %s %s %s\n" % (nickname, nickname, nickname, nickname)
nick = "NICK %s \n" % nickname

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def valid():
	if len(sys.argv) == 1:
		print("No arguments passed. I'm lost and don't know where I am.")
		exit()

def send(command):
	ircsock.send(bytes(command + "\n", "utf-8"))

def receive():
	inbound = ircsock.recv(2048).decode("utf-8")
	return inbound

def buildConnection():
	# Connect
	ircsock.connect((server, port))
	print("Connected to: %s:%s" % (server, port))
	# Login
	send(user)
	send(nick)
	while 1:
		text = receive()
		text = str(text)
		if "is now your displayed host" in text:
			print(text)
			break
		else:
			print(text)
			print("Logged in...")

	# Join
	send("JOIN " + channel)
	print("Joined " + channel)

def main():
	buildConnection()
	while 1:
		text = receive()
		text = str(text)
		if "PRIVMSG " + nickname in text:
			print(text)
		elif "PING :" in text:
			print(text)
			send("PONG :pingis\n")
		else:
			valid()
			todo = sys.argv[1]
			if todo == 'ep1':
				send("PRIVMSG Candy :!ep1")
				datarecv = receive()
				print(datarecv)
				# Do work bay bay
        # Redacted, no spoilers/answers here.
				returned = receive()
				print(returned)
				break
			elif todo == 'ep2':
				send("PRIVMSG Candy :!ep2")
				datarecv = receive()
				print(datarecv)
        # Redacted, no spoilers/answers here.
				returned = receive()
				print(returned)
				break
			elif todo == 'ep3':
				send("PRIVMSG Candy :!ep3")
				datarecv = receive()
				print(datarecv)
        # Redacted, no spoilers/answers here.
				returned = receive()
				print(returned)
			elif todo == 'ep4':
				send("PRIVMSG Candy :!ep4")
				datarecv = receive()
				print(datarecv)
        # Redacted, no spoilers/answers here.
				returned = receive()
				print(returned)
			else:
				print("I honestly don't know what you want me to do. ¯\_(ツ)_/¯ ")
				break
	ircsock.close()
main()
