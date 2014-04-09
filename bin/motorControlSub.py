#!/usr/bin/env python
from homecontrol.automation import Motor
import sys
import time
import zmq

port = "5556"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

def sub_motor_control():
	print "Listening for motor control messages"
	socket.connect ("tcp://localhost:%s" % port)
	topicfilter = "motor"
	while True:
		socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
		string = socket.recv()
		topic, messagedata = string.split()
		print topic, messagedata

if __name__ == "__main__":
	sub_motor_control)
