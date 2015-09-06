from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

pyglow.led(1, 100)
sleep(1)
pyglow.led(1,0)
sleep(1)
pyglow.update_leds()
