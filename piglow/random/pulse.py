#PyGlow test

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

while True:
	pyglow.all(brightness=150, speed=60000, pulse=True)
	sleep(1)

pyglow.update_leds()
