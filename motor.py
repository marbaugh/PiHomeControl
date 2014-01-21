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

class Motor:
	"""Motor class creates and instance of Motor

    Provides an init function to setup the GPIO channels,
    and other functions to step the motor forward and backward.

    """
	
	motor_sequence = []
	motor_sequence = range(0, 4)
	motor_sequence[0] = [1, 0, 0, 0]
	motor_sequence[1] = [0, 1, 0, 0]
	motor_sequence[2] = [0, 0, 1, 0]
	motor_sequence[3] = [0, 0, 0, 1]
	
	def __init__(self, IN1=17, IN2=18, IN3=27, IN4=22):
		"""Init function sets and intializes IN1-IN4 to the corresponding GPIO channels

		The init function defines GPIO channel numbers to be used with the stepper motor.
		By default Pin 11, 12, 13, 15 are used on the Raspberry Pi and map to --> GPIO 17, 18, 27, 22
    	but can be changed when initializing the Motor class
    	"""

		self.IN1 = IN1
		self.IN2 = IN2
		self.IN3 = IN3
		self.IN4 = IN4
		self.channel_numbers = [self.IN1, self.IN2, self.IN3, self.IN4]
		self.setupGPIOChannels(self.channel_numbers)

	def setupGPIOChannels(self, channel_numbers):
		"""seteupGPIOChannles takes the list of channles numbers and sets them as outputs"""

		# Choose to set the GPIO numbering to BOARD or BCM
		# Uncomment line below to use the pin numbers on the P1 header of the board
		#GPIO.setmode(GPIO.BOARD) 
		# Default to use the channel numbers on the Broadcom chip
		GPIO.setmode(GPIO.BCM) 

		# Set up the GPIO channel's being used as output
		# ex: GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
		for channel in channel_numbers:
		  print "Setting up channel %s as an output" %(channel)
		  GPIO.setup(channel,GPIO.OUT)
		  # Set the output state of a GPIO pin:
		  # The state can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True. 
		  GPIO.output(channel, False)

	def stepMotorForward(self, duration):
		"""stepMotorForward takes the duration and steps through the motor sequence in a forward direction for that duration"""

		timeout = time.time() + duration   #5 seconds from now
		while True:
			if not time.time() > timeout:
				step_num = 0
				for sequence in range(0, len(self.motor_sequence)):
					for channel in self.channel_numbers:
						GPIO.output(channel, self.motor_sequence[sequence][step_num])
						step_num += 1
					step_num = 0
					time.sleep(.003)
			else:
				break

	def stepMotorBackward(self, duration):
		"""stepMotorBackward takes the duration and steps through the motor sequence in a backward direction for that duration"""

		timeout = time.time() + duration   #5 seconds from now
		while True:
			if not time.time() > timeout:
				step_num = 0
				for sequence in range(len(self.motor_sequence)-1, -1, -1):
					for channel in self.channel_numbers:
						GPIO.output(channel, self.motor_sequence[sequence][step_num])
						step_num += 1
					step_num = 0
					time.sleep(.003)
			else:
				break

def main():
	"""main function creates an instance of the Motor class and spins in in the given direction for the given duration"""

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

	motor = Motor()
	if forward:
		print "Moving stepper motor forward"
		motor.stepMotorForward(duration)

	elif backward:
		print "Moving stepper bakward"
		motor.stepMotorBackward(duration)

	# Returning all channels
	GPIO.cleanup()

if __name__ == '__main__':
	main()