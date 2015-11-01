#!/usr/bin/env python

import socket
import time


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
# TCP_IP = '203.0.113.17'
# TCP_PORT = 50301
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
SLEEP_TIME = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))
print "connect to server succeded.."

while(1):
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data
    time.sleep(SLEEP_TIME)
    
#Application shall not close itself, to test if if maybe closed by other parties
s.close()
print "End of game...."