#!/usr/bin/env python

from homecontrol.automation import DoorSensor
import sys
import time
import zmq

def pub_door_sensor_status():
    port = "5556"
    topic = "door"
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:{0}".format(port))
    # Allow clients to connect before sending data
    sleep(10)
    while True:
        messagedata = DoorSensor().status()
        print "{0} {1}".format(topic, messagedata)
        socket.send("{0} {1}".format(topic, messagedata))
        time.sleep(15)

if __name__ == "__main__":
    pub_door_sensor_status()
