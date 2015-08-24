SOFTWARE INSTALLATION

You'll need to make sure you have the following packages installed to proceed with the worksheet:

smbus for Python 2
PyGlow for Python 2
You'll need to be online to install packages.

First update and upgrade your system. Open the terminal by clicking on Main Menu, Accessories and then selecting Terminal. Enter the following commands:

```
sudo apt-get update
sudo apt-get upgrade
```

Install smbus with the following command:

sudo apt-get install python-smbus
Check you have it installed correctly by entering:

sudo python -c "import smbus"
If you get an error saying No module named 'smbus' then check you have entered the commands above correctly.

ENABLE I2C DRIVER MODULES

You'll also need to enable the I2C driver module.

Edit the modules configuration file:

sudo nano /etc/modules
Then add the following line at the end of the file, if it's not already there:

i2c-dev
Press CTRL + X, followed by Y and Enter to save your changes.

Enter sudo raspi-config to open the Raspberry Pi Configuration Tool.

Select Advanced Options and then choose I2C with the keyboard's up/down keys. Enable the I2C interface and kernel module when prompted, and you'll be prompted to reboot the Pi when finishing.
DOWNLOAD PYGLOW MODULE AND TEST

You'll need to create a pyglow folder, and download the PyGlow module and a test file from GitHub, using the following commands:

mkdir pyglow
cd pyglow
wget http://goo.gl/zQ3CHB -O PyGlow.py --no-check-certificate
wget http://goo.gl/18fwzn -O test.py --no-check-certificate
To test this works, enter:

sudo python test.py
It should ask you to enter a series of colour values. If you get an error, check you have entered the commands above correctly.
