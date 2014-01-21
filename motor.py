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

# Choose to set the GPIO numbering to BOARD or BCM
# Uncomment to use the pin numbers on the P1 header of the board
#GPIO.setmode(GPIO.BOARD) 

# Uncomment to use the channel numbers on the Broadcom chip
GPIO.setmode(GPIO.BCM) 

# Define GPIO channel numbers to be used with the stepper motor
# Pin 11, 12, 13, 15 --> GPIO 17, 18, 27, 22
channel_numbers = [17, 18, 27, 22]

parser = argparse.ArgumentParser(description='Stepper Motor Program.')
parser.add_argument('-f', '--forward', action='store_true',
	dest='forward', help='Move motor forward')
parser.add_argument('-b', '--backward', action='store_true',
	dest='backward', help='Move motor backward')
parser.add_argument('-d', '--duration', action='store', 
	dest='duration', type=int, help='Duration in seconds')
args = parser.parse_args()

if args.forward is False and args.backward is False:
   parser.error("At least one of -f and -b are required")

if args.duration is None:
	parser.error("Duration must be set")

forward = args.forward
backward  = args.backward
duration = args.duration

# Set up the GPIO channel's being used as output
# ex: GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
for channel in channel_numbers:
  print "Setting up channel %s as an output" %(channel)
  GPIO.setup(channel,GPIO.OUT)
  # Set the output state of a GPIO pin:
  # The state can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True. 
  GPIO.output(channel, False)

motor_sequence = []
motor_sequence = range(0, 4)
motor_sequence[0] = [1, 0, 0, 0]
motor_sequence[1] = [0, 1, 0, 0]
motor_sequence[2] = [0, 0, 1, 0]
motor_sequence[3] = [0, 0, 0, 1]

def stepMotor(channels, state):
	step_num = 0
	for channel in channels:
		GPIO.output(channel, state[step_num])
		step_num += 1
	time.sleep(.003)

print "Moving stepper motor"
timeout = time.time() + duration   #5 seconds from now

while True:
	if not time.time() > timeout:
		if forward:
			for sequence in range(0, len(motor_sequence)):
				stepMotor(channel_numbers, motor_sequence[sequence])

		if backward:
			for sequence in range(len(motor_sequence)-1, -1, -1):
				stepMotor(channel_numbers, motor_sequence[sequence])
	else:
		break

# Returning all channels
GPIO.cleanup()