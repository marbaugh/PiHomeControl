#!/usr/bin/env python

# Import the required libraries
import argparse
import time
import signal
import sys

try:
    # Class to control the GPIO on a Raspberry Pi
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPI!\n")
    print("Possible you need to run script with 'sudo'")
    
# Avoid warnings if more than one script/circuit
# is connected to the GPIO of the Raspberry Pi.
#GPIO.setwarnings(False)

# Set the GPIO numbering to BOARD or BCM
# GPIO.setmode(GPIO.BOARD) # Pin numbers on the P1 header of the board
GPIO.setmode(GPIO.BCM) # Channel numbers on the Broadcom chip

# Define GPIO channel numbers to be used with the motion sensor
# Pin 16  GPIO 23
channel_number = 23

# Set up the GPIO channel being used as input
print "Setting up channel %s as an input" %(channel_number)
GPIO.setup(channel_number,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
  if GPIO.input(channel_number):
    print("DOOR OPEN")
    break
  time.sleep(0.5)

GPIO.cleanup()
