from nose.tools import *
from homecontrol.automation import Motor
import unittest


class MotorTest(unittest.TestCase):

	def setUp(self):
		self.motor = Motor()

	def tearDown(self):
		self.motor.cleanup()

	def test_motor_forward(self):
		print "Moving stepper motor forward"
		self.motor.forward(5)

	def test_motor_reverse(self):
		print "Moving stepper in reverse"
		self.motor.reverse(5)
