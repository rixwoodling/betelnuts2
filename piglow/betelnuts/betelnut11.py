##################################################
## Switch each colour on in sequence on and off ##
##                                              ##
## Example by Jason - @Boeeerb                  ##
##################################################

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()
val = 20
colour = 1

while True:
    if colour == 19:
        colour = 1
        if val == 20:
            val = 0
        else:
            val = 20
    
    pyglow.led(colour, val)
    sleep(0.05)

    colour = colour + 1
