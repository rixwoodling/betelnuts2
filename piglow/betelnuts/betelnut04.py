from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

### Blink 2
#while True:
#    pyglow.color("red", 100)
#    sleep(1)
#    pyglow.color("red", 0)
#    pyglow.color("orange", 100)
#    sleep(1)
#    pyglow.color("orange", 0)

### Pulse All
while True:
    pyglow.pulse_all(150, 500)
    sleep(1)
