#!/usr/bin/env python

from homecontrol.automation import DoorSensor
import requests
import sys
import time

def door_openend(self):
     webserver = 'http://192.168.3.107:5000'
     url = webserver+"/doorSensor/status/opened"
     r = requests.post(url)

def door_closed(self):
     webserver = 'http://192.168.3.107:5000'
     url = webserver+"/doorSensor/status/closed"
     r = requests.post(url)

def door_sensor_status():
    DoorSensor().event_detect(DOOR)
    while 1:
        time.sleep(100)
    
if __name__ == "__main__":
    door_sensor_status()
