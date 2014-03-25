#!/usr/bin/env python

# Import the required libraries
import argparse
import time
import signal
import sys
# Class to control the GPIO on a Raspberry Pi
import RPi.GPIO as GPIO

# Avoid warnings if more than one script/circuit
# is connected to the GPIO of the Raspberry Pi.
#GPIO.setwarnings(False)

class AlarmException(Exception):
    pass

class Accessory(object):

    def set_GPIO_board_mode(self, mode):
        """set_GPIO_board_mode set the GPIO board numbering to BOARD or BCM"""
        
        #GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)
        GPIO.setmode(mode)

    def cleanup(self):
        """reutrns all the channels used"""
        GPIO.cleanup()
    
    def alarmHandler(signum, frame):
        raise AlarmException

class Motor(Accessory):
    """Motor class creates and instance of Motor

    Provides an init function to setup the GPIO channels,
    and other functions to step the motor forward and in reverse.

    """

    motor_sequence = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))

    def __init__(self,
                 IN1=17,
                 IN2=18,
                 IN3=27,
                 IN4=22,
                 speed=.003,
                 mode=GPIO.BCM):
        """Init function sets and intializes IN1-IN4 to the corresponding 
        GPIO channels

        The init function defines GPIO channel numbers to be used with the 
        stepper motor.
        By default Pin 11, 12, 13, 15 are used on the Raspberry Pi and map 
        to --> GPIO 17, 18, 27, 22
        but can be changed when initializing the Motor class.

        The default speed is set to .003 for the time the motor sleeps 
        in-between each sequence 

        The default board mode is to use the channel numbers on the 
        Broadcom chip (GPIO.BCM)
        """

        self._channels = [IN1, IN2, IN3, IN4]
        self._speed = speed
        self.set_GPIO_board_mode(mode)
        self.set_GPIO_output_channels()

    def set_GPIO_output_channels(self):
        """set_GPIO_output_channels takes the list of channles numbers and 
        sets them as outputs"""
        # Set up the GPIO channel's being used as output
        # ex: GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
        for channel in self._channels:
          print "Setting up channel %s as an output" %(channel)
          GPIO.setup(channel,GPIO.OUT)
          # Set the output state of a GPIO pin:
          # The state can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
          GPIO.output(channel, False)

    def forward(self, duration):
        """forward takes the duration and steps through the motor sequence 
        in a forward direction for that duration"""

        signal.signal(signal.SIGALRM, alarmHandler)
        signal.alarm(duration)
        while True:
            step_num = 0
            for sequence in range(0, len(Motor.motor_sequence)):
                for channel in self._channels:
                    GPIO.output(channel,
                                Motor.motor_sequence[sequence][step_num])
                    step_num += 1
                step_num = 0
                time.sleep(self._speed)

    def reverse(self, duration):
        """reverse takes the duration and steps through the motor sequence 
        in a reverse direction for that duration"""

        timeout = time.time() + duration   #5 seconds from now
        while True:
            if not time.time() > timeout:
                step_num = 0
                for sequence in range(len(Motor.motor_sequence)-1, -1, -1):
                    for channel in self._channels:
                        GPIO.output(channel,
                                    Motor.motor_sequence[sequence][step_num])
                        step_num += 1
                    step_num = 0
                    time.sleep(self._speed)
            else:
                break

class MotionSensor(Accessory):
    """MotorSensor class creates and instance of MotionSensor

    Provides an init function to setup the GPIO channel,
    and a function to detect is there is motion

    """

    def __init__(self, CHANNEL=25, mode=GPIO.BCM):
        """Init function sets and intializes the channel to the corresponding
        GPIO channels

        The init function defines GPIO channel number to be used with the 
        motion sensor.
        By default Pin 22 is used on the Raspberry Pi and map to --> GPIO 25
        but can be changed when initializing the MotionSensor class.

        The default board mode is to use the channel numbers on the Broadcom
        chip (GPIO.BCM)
        """

        self.channels = [CHANNEL]
        self.set_GPIO_board_mode(mode)
        self.set_GPIO_output_channels(self.channels)

    def set_GPIO_input_channels(self, channels):
        """set_GPIO_input_channels takes the list of channles numbers and 
        sets them as inputs"""
        # Set up the GPIO channel's being used as input
        # ex: GPIO.setup(channel, GPIO.IN, initial=GPIO.HIGH)
        for channel in channels:
          print "Setting up channel %s as an input" %(channel)
          GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD.UP)

    def status(self):
        """status returns TRUE if the sensor is activate and 
        FALSE otherwise"""

        motion = False
        for channel in self.channels:
            timeout = time.time() + 5 #5 seconds from now
            while True:
                if GPIO.input(channel):
                    motion = True
                if time.time() > timeout:
                    break

        return motion

class DoorSensor(Accessory):
    """DoorSensor class creates and instance of DoorSensor

    Provides an init function to setup the GPIO channel,
    and a function to detect if the door is open

    """

    def __init__(self, CHANNEL=23, mode=GPIO.BCM):
        """Init function sets and intializes the channel to the 
        corresponding GPIO channels

        The init function defines GPIO channel number to be used with
        the door sensor.
        By default Pin 16 is used on the Raspberry Pi and map 
        to --> GPIO 23
        but can be changed when initializing the DoorSensor class.

        The default board mode is to use the channel numbers on the 
        Broadcom chip (GPIO.BCM)
        """

        self.channels = [CHANNEL]
        self.set_GPIO_board_mode(mode)
        self.set_GPIO_output_channels(self.channels)

    def set_GPIO_input_channels(self, channels):
        """set_GPIO_input_channels takes the list of channles numbers and 
        sets them as inputs"""
        # Set up the GPIO channel's being used as input
        # ex: GPIO.setup(channel, GPIO.IN, initial=GPIO.HIGH)
        for channel in channels:
          print "Setting up channel %s as an input" %(channel)
          GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD.UP)

    def status(self):
        """status returns TRUE if the door is open and FALSE otherwise"""

        door = False
        for channel in self.channels:
            timeout = time.time() + 5 #5 seconds from now
            while True:
                if GPIO.input(channel):
                    door = True
                if time.time() > timeout:
                    break

        return door
