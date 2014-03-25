=============
PiHomeControl
=============

The PiHomeControl project provides end users a way to control and motor home automation software using the Raspberry Pi

Install
-------

To install latest::

    pip install git+git://github.com/marbaugh/PiHomeControl.git


Usage
-----

Once installed you can simply import the classes you would like to leverage::

    from homecontrol.automation import Motor
    from homecontrol.automation import MotionSensor
    from homecontrol.automation import DoorSensor
    from homecontrol.automation import Accessory

Motor Example::

    from homecontrol.automation import Motor
    motor = Motor()
    motor.forward(5)
    motor.reverse(5)


Limitations
-----------

Currently only supports:

1. Stepper motors connected to the Raspberry Pi
2. Monitor motion sensors connected to the Raspberry Pi
3. Door sensors connected to the Raspberry Pi
