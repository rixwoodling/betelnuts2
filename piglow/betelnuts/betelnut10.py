from PyGlow import PyGlow
from time import sleep

b = 100
s = 1000

pyglow = PyGlow(brightness=b, speed=s, pulse=True)

pyglow.all(0)

count = 0
while (count < 5):
	pyglow.all()

	count = count + 1

pyglow.all(0)
