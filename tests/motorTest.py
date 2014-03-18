from homecontrol.automation import Motor

def motor_forward_test(motor):
	print "Moving stepper motor forward"
	motor.forward(5)

def motor_reverse_test(motor):
	print "Moving stepper in reverse"
	motor.reverse(5)

def main():
	motor = Motor()
	motor_forward_test(motor)
	motor_reverse_test(motor)

if __name__ == '__main__':
	main()
