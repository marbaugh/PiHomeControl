#!/usr/bin/env python

from homecontrol.automation import MotionSensor
import sys
import time


def MOTION(self):
     print "Motion Detected!"

def motion_sensor_status():
     MotionSensor().event_detect(MOTION)
     while 1:
          time.sleep(100)

if __name__ == "__main__":
     motion_sensor_status()
