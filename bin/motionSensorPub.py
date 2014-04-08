from homecontrol.automation import MotionSensor
import sys
import time
import zmq

def pub_motion_sensor_status():
	port = "5556"
	topic = "motion"
	context = zmq.Context()
	socket = context.socket(zmq.PUB)
	socket.bind("tcp://*:%s" % port)
	while True:
		messagedata = MotionSensor().status
		print "%d %d" % (topic, messagedata)
		socket.send("%d %d" % (topic, messagedata))
		time.sleep(10)

if __name__ == "__main__":
	pub_motion_sensor_status()
