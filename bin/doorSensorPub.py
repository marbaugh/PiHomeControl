#!/usr/bin/env python

from homecontrol.automation import DoorSensor
import requests
import sys
import time

def DOOR(self):
     messagedata = DoorSensor().status()
     webserver = 'localhost'
     url = webserver+"/doorSensor/status/"
     if messagedata == True:
     	print "Door Opened!"
     	r = requests.post(url+"opened")
     else:
     	print "Door Closed!"
     	r = requests.post(url+"closed")


def pub_door_sensor_status():
    DoorSensor().event_detect(DOOR)
    while 1:
        time.sleep(100)
    
if __name__ == "__main__":
    pub_door_sensor_status()
