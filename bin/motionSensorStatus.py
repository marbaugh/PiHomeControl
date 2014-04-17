#!/usr/bin/env python

from homecontrol.automation import MotionSensor
import sys
import requests
import time

motionSensor = MotionSensor()

def motion_event(self):
     messagedata = motionSensor.status()
     webserver = 'http://192.168.3.107:5000'
     url = webserver+"/motionSensor/status/"
     if messagedata == True:
        print "Motion Sensed!"
        r = requests.post(url+"motion")

def motion_sensor_status():
     motionSensor.event_detect(motion_event)
     while 1:
          time.sleep(100)

if __name__ == "__main__":
     motion_sensor_status()
