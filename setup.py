#!/usr/bin/env python

from setuptools import setup

setup(name='homeautomation',
      version='1.0',
      description='Home Automation Utilities for Raspberry Pi',
      author='Matthew Arbaugh',
      author_email='marbaugh@gmail.com',
      url='https://github.com/marbaugh/stepperMotor',
      package_dir = {'': 'src'},
      packages=['homeautomation'],
      install_requires=['RPi.GPIO'],
     )
