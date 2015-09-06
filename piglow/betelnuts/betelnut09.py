from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

pyglow.all(0)

count = 0
while (count < 10):

	pyglow.color("white", 0)
	pyglow.color("blue", 110)
	sleep(0.1)

        pyglow.color("blue", 0)
        pyglow.color("green", 100)
        sleep(0.1)

	pyglow.color("green", 0)
	pyglow.color("yellow", 100)
	sleep(0.1)

        pyglow.color("yellow", 0)
        pyglow.color("orange", 100)
        sleep(0.2)

        pyglow.color("orange", 0)
        pyglow.color("red", 100)
        sleep(0.3)


        pyglow.color("red", 0)
        pyglow.color("orange", 100)
        sleep(0.2)

        pyglow.color("orange", 0)
        pyglow.color("yellow", 100)
        sleep(0.1)

        pyglow.color("yellow", 0)
        pyglow.color("green", 100)
        sleep(0.1)

        pyglow.color("green", 0)
        pyglow.color("blue", 110)
        sleep(0.1)

	pyglow.color("blue",  0)
	pyglow.color("white", 100)
	sleep(0.1)

	count = count + 1

pyglow.all(0)
