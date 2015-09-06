from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

count = 0
while (count < 10):
	pyglow.led(1, 100)
	pyglow.led(7, 100)
	pyglow.led(13,100)
	sleep(0.1)
	pyglow.led(1, 0)
	pyglow.led(7, 0)
	pyglow.led(13,0)

	pyglow.led(2, 100)
	pyglow.led(8, 100)
	pyglow.led(14,100)
	sleep(0.1)
	pyglow.led(2, 0)
	pyglow.led(8, 0)
	pyglow.led(14,0)

	pyglow.led(3, 100)
	pyglow.led(9, 100)
	pyglow.led(15,100)
	sleep(0.1)
	pyglow.led(3, 0)
	pyglow.led(9, 0)
	pyglow.led(15,0)

	pyglow.led(4, 100)
	pyglow.led(10,100)
	pyglow.led(16,100)
	sleep(0.1)
	pyglow.led(4, 0)
	pyglow.led(10,0)
	pyglow.led(16,0)

	pyglow.led(5, 100)
	pyglow.led(11,100)
	pyglow.led(17,100)
	sleep(0.1)
	pyglow.led(5, 0)
	pyglow.led(11,0)
	pyglow.led(17,0)

	pyglow.led(6, 100)
	pyglow.led(12,100)
	pyglow.led(18,100)
	sleep(0.1)
	pyglow.led(6, 0)
	pyglow.led(12,0)
	pyglow.led(18,0)

	pyglow.update_leds()
	
	count = count + 1
