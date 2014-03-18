from homecontrol.automation import Motor

def test_motor_forward(motor):
	motor = Motor()
	print "Moving stepper motor forward"
	motor.forward(5)

def test_motor_reverse(motor):
	motor = Motor()
	print "Moving stepper in reverse"
	motor.reverse(5)