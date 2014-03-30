from nose.tools import *
from homecontrol.automation import MotionSensor
import unittest

class MotionTest(unittest.TestCase):

	def setUp(self):
		self.motion_sensor = MotionSensor()

	def tearDown(self):
		self.motion_sensor.cleanup()

	def test_motion_status(self):
		print "Checking Status of Motion Sensor"
		self.motion_sensor.status()