#PyGlow test

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

while True:
	pyglow.color("green", 0)
	pyglow.color("red", 100)
	pyglow.color("yellow",100)
	sleep(1)
	pyglow.color("green", 100)
	pyglow.color("red", 0)
	pyglow.color("yellow", 100)
	sleep(1)
	pyglow.color("green", 100)
	pyglow.color("red",100)
	pyglow.color("yellow", 0)
	sleep(1)

pyglow.update_leds()
