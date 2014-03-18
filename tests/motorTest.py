from homecontrol.automation import Motor

def test_motor_forward():
	motor = Motor()
	print "Moving stepper motor forward"
	motor.forward(5)
	motor.cleanup()
	pass

def test_motor_reverse():
	motor = Motor()
	print "Moving stepper in reverse"
	motor.reverse(5)
	motor.cleanup()
	pass