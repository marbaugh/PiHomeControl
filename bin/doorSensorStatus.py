#!/usr/bin/env python

from homecontrol.automation import DoorSensor
import requests
import sys
import time

door = DoorSensor()

def door_event(self):
     messagedata = door.status()
     webserver = 'http://192.168.3.107:5000'
     url = webserver+"/doorSensor/status/"
     if messagedata == True:
        print "Door Opened!"
        r = requests.post(url+"opened")
     else:
        print "Door Closed!"
        r = requests.post(url+"closed")

def door_sensor_status():
    door.event_detect(door_event)
    while 1:
        time.sleep(100)
    
if __name__ == "__main__":
    door_sensor_status()
