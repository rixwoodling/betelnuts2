##################################################
## Switch each colour on in sequence on and off ##
##                                              ##
## Example by Jason - @Boeeerb                  ##
##################################################

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()
val = 100
color = 2
dark = 1

pyglow.all(0)

while True:
	if color == 7:
		break
	pyglow.led(color, val)
	pyglow.led(dark, 0)
	sleep(0.5)

	color = color + 1
	dark = dark + 1

while True:	
	a = color
	b = a + 6
	
	pyglow.led(a, val)
	pyglow.led(b, val)
	sleep(0.1)	

	high = high + 1
	low = low + 1
		
print ("tada!")
pyglow.all(0)
