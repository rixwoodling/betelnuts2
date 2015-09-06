
<i>Running `python piglowtest.py` without being root will cause this error:</i>   
```
Traceback (most recent call last):
  File "piglowtest.py", line 4, in <module>
    pyglow = PyGlow()
  File "/home/rix/piglow/PyGlow.py", line 117, in __init__
    self.bus = SMBus(i2c_bus)
IOError: [Errno 13] Permission denied
```
<i>Instead, use `sudo python piglowtest.py`</i>  
