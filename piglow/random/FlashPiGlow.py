#PyGlow test

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

while True:
	pyglow.color("blue", 100)
	sleep(1)
	pyglow.color("blue", 0)
	pyglow.color("red", 100)
	sleep(1)
	pyglow.color("red", 0)

pyglow.update_leds()
