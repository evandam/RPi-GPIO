import RPi.GPIO as gpio

OUT = gpio.OUT
IN = gpio.IN

gpio.setmode(gpio.BCM)

def setup(pin, mode):
	gpio.setup(pin, mode)

def cleanup():
	gpio.cleanup()

def write(pin, state):
	gpio.output(pin, state)

def read(pin):
	return gpio.input(pin)
