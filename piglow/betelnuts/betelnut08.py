from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()
count = 0
while (count < 8):
	pyglow.color("white", 100)
	sleep(0.05)
	pyglow.color("blue", 110)
	sleep(0.05)
        pyglow.color("green", 100)
        sleep(0.05)
        pyglow.color("yellow", 100)
        pyglow.color("white", 80)
        sleep(0.05)
        pyglow.color("orange", 100)
        pyglow.color("white", 60)
        sleep(0.05)
        pyglow.color("red", 100)
        pyglow.color("white", 40)
        sleep(0.05)

        pyglow.color("white",   0)
        sleep(0.05)
        pyglow.color("blue",   0)
        sleep(0.05)
        pyglow.color("green",   0)
        sleep(0.05)
        pyglow.color("yellow",   0)
        sleep(0.05)
        pyglow.color("orange",   0)
        sleep(0.05)
        pyglow.color("red",   0)
        sleep(0.05)
	
	count = count + 1
