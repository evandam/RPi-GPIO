from django.db import models
from time import sleep
import gpio_interface as gpio

PRESS_DURATION = 0.5

class Switch(models.Model):
	name = models.CharField(max_length=50)
	on_pin = models.IntegerField(default=0)
	off_pin = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name
	
	def write(self, value):
		if int(value) == 0:
			pin = self.off_pin
		else:
			pin = self.on_pin

		gpio.setup(pin, gpio.OUT)
		gpio.write(pin, 1)
		sleep(PRESS_DURATION)
		gpio.write(pin, 0)
		gpio.cleanup()
		
