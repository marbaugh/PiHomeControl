from nose.tools import *
from homecontrol.automation import MotionSensor
import unittest

class MotionTest(unittest.TestCase):

	def setUp(self):
		self.motion_sensor = MotionSensor()

	def tearDown(self):
		self.motion_sensor.cleanup()

	def test_motion_status_true(self):
		print "Checking Status of Motion Sensor"
		self.assertTrue(self.motor.status())

	def test_motion_status_false(self):
		print "Checking Status of Motion Sensor"
		self.assertFalse(self.motor.status())
