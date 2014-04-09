#!/usr/bin/env python

from homecontrol.automation import MotionSensor
import sys
import time
import zmq

def pub_motion_sensor_status():
     port = "5556"
     topic = "motion"
     context = zmq.Context()
     socket = context.socket(zmq.PUB)
     socket.bind("tcp://*:{0}".format(port))
#     while True:
     messagedata = MotionSensor().status()
     print "{0} {1}".format(topic, messagedata)
     socket.send("{0} {1}".format(topic, messagedata))

    # time.sleep(10)

if __name__ == "__main__":
     pub_motion_sensor_status()
