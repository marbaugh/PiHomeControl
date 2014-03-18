from homecontrol.automation import Motor

def setup_func():
	motor = Motor()

def teardown_func():
	motor.cleanup()

@with_setup(setup_func, teardown_func)
def test_motor_forward():
	motor = Motor()
	print "Moving stepper motor forward"
	motor.forward(5)
	motor.cleanup()
	pass
	
@with_setup(setup_func, teardown_func)
def test_motor_reverse():
	motor = Motor()
	print "Moving stepper in reverse"
	motor.reverse(5)
	motor.cleanup()
	pass