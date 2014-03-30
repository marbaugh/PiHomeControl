from nose.tools import *
from homecontrol.automation import DoorSensor
import unittest

class DoorSensorTest(unittest.TestCase):

	def setUp(self):
		self.door_sensor = DoorSensor()

	def tearDown(self):
		self.door_sensor.cleanup()

	def test_door_status(self):
		print "Checking Status of Door Sensor"
		self.door_sensor.status()