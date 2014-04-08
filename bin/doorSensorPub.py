
from homecontrol.automation import DoorSensor
import sys
import time
import zmq

def pub_door_sensor_status():
	port = "5556"
	topic = 10001
	context = zmq.Context()
	socket = context.socket(zmq.PUB)
	socket.bind("tcp://*:%s" % port)
	while True:
		messagedata = DoorSensor().status
		print "%d %d" % (topic, messagedata)
		socket.send("%d %d" % (topic, messagedata))
		time.sleep(10)

if __name__ == "__main__":
	pub_door_sensor_status()