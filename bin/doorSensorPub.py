#!/usr/bin/env python

from homecontrol.automation import DoorSensor
import sys
import time
import requests

def DOOR(self):
     print "Door Movement Detected!"
     print DoorSensor().status()


def pub_door_sensor_status():
    DoorSensor().event_detect(DOOR)
    while 1:
        time.sleep(100)
    
if __name__ == "__main__":
    pub_door_sensor_status()
