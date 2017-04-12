#### PiGlow

<sup><i>The `groupadd` command creates permission groups for users and processes.</i></sup>  
<sup><i>It is often used in harmony with `adduser` and `sudo`.</i></sup>  

---

`1` Identify current groups.  
><sup>`+` Type `groups`. <i>Assuming no users have been added yet, the only group shown is root.</i></sup>  
><sup>`+` Then identify root with `id root`, which outputs:  
```
uid=0(root) gid=0(root) groups=0(root)
```
><sup>uid=0<i>...</i></sup>  

<sup>`+` `groupadd `</sup>  
<sup><i>`+` `apt-get install sudo`</i></sup>  
<sup><i>`+` `apt-get install sudo`</i></sup>  

###### sudo vs su

<sup><i>Both `sudo` and `su` allows the same root privileges to the regular user, with a difference. Essentially, `sudo` is enabled as one-time usage, say to install a package at root level. Once the command is executed, root permissions revert back. With `su`, in addition to `su -` or `su - root`, the user is able to log into root to make any number of root-level commands up until the time the user exits the root session.</i></sup>  

###### advantages, disadvantages and warnings  
<sup>`+` Users use their own user login password instead of using root password.</sup>  
<sup>`+` Every action requires the user to enter a password, forcing the user to think before each action.</sup>  
<sup>`+` A log is kept of any command(s) run, which are located in `/var/log/auth.log`</sup>  
<sup>`+` Because the user does not enter root first, any brute-force attacks to root are blocked.</sup>  
<sup>`+` Admin rights for groups and users can be maintained without needing to change root password.</sup>  
<sup>`+` Security settings can be customized for each user/group.</sup>   
<sup>`!` Be aware the power of `sudo` can be just as damaging as `su`.</sup>  

###### user levels  
<sup><i>Once users and groups are added and defined with [useradd](useradd.md) and [groupadd](groupadd.md), security settings can be defined to each.</i></sup>  
<sup>`root` Cannot ssh into root. Can only access via admin level.</sup>  
<sup>`admin` Can read, write and excute all user files. Can use sudo to have root level permissions.</sup>  
<sup>`user` Can read, write and execute if owner. Read and execute only if not owner. No sudo.</sup>  
<sup>`guest` The most restricted security level. Can only read and execute, hence read-only. </sup>  

###### resources

<sup>`?` https://github.com/pimoroni/piglow</sup>  
<sup>`?` http://askubuntu.com/questions/14222/how-to-add-a-guest-account-without-a-password</sup>   
<sup>`?` http://www.yolinux.com/TUTORIALS/LinuxTutorialManagingGroups.html</sup>  
<sup>`?` http://www.computerhope.com/unix/groupadd.htm</sup>  
<sup>`?` http://linux.101hacks.com/unix/groupadd/</sup>  
<sup>`?` http://www.hostingadvice.com/how-to/linux-add-user-to-group/</sup>  
<sup>`?` http://stackoverflow.com/questions/14059916/is-there-a-command-to-list-all-unix-group-names</sup>  


SOFTWARE INSTALLATION

<sup><i>The original notes can be found at `https://www.raspberrypi.org/learning/piglow/software/`.</i></sup>

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

#### PiGlow Installation
http://www.raspberrypi.org/learning/piglow/software/

Installing smbus
<sup>`+` `sudo apt-get update`</sup>  
<sup>`+` `sudo apt-get upgrade`</sup>  

<sup>`+` `sudo apt-get install python-smbus`</sup>  
<sup>`+` `sudo python -c "import smbus"`</sup>  

<sup>`+` `mkdir piglow`</sup>  
<sup>`+` `cd piglow`</sup>  
<sup>`+` `wget http://...`</sup>  
<sup>`+` `wget http://...`</sup>  

Enable I2C Driver Module
```sudo nano /etc/modules```

add the following lines
> i2c-dev
> i2c-bcm2708
