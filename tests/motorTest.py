from homecontrol.automation import Motor

def motor_forward_test():
	motor = Motor()
	print "Moving stepper motor forward"
	motor.forward(5)

def motor_reverse_test():
	print "Moving stepper in reverse"
	motor.reverse(5)

def main():
	motor_forward_test()
	motor_reverse_test()

if __name__ == '__main__':
	main()
