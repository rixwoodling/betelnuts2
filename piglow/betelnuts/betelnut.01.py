#betelnut01.py

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

pyglow.led(1, 100)
sleep(0.5)
pyglow.led(1, 0)

pyglow.led(2, 100)
sleep(0.5)
pyglow.led(2, 0)

pyglow.led(3, 100)
sleep(0.5)
pyglow.led(3, 0)

pyglow.led(4, 100)
sleep(0.5)
pyglow.led(4, 0)
