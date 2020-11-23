# PhoneSploitGui

![Screenshot](Screenshots/Firstpage.png)
![Screenshot](Screenshots/Secondpage.png)

**PhoneSploitGui is a gui version of the cli tool PhoneSploit used to manage android devices that have USB Debugging enabled. Which was created by metachar but is no longer available.
There are 20+ functions. This program uses ADB which must be installed to your device in order for this program to work. This program works for Windows, Linux and Mac OS.**

# Installing PhoneSploitGui
# Windows
* **First, unzip the adb.rar file. This archive contains the files needed for adb to run and the adb program itself. Files must be extracted to the PhoneSploitGui folder because PhoneSploitGui looks for adb in the root of the folder.**

* **Then, open your command prompt but clicking the Windows start menu then type ``cmd``.**
* **Type ``pip install -r requirments.txt``. This will install all the libraries needed for PhoneSploitGui to run.**
* **Now you can run the program by typing ``python PhoneSploitGui.py``.**

# Linux
_The adb.rar file is not needed for Linux. Please disregard it._

* **Install adb and python3 using ``sudo apt-get install adb python3.6``.**
* **Next, type ``pip3 install -r requirements.txt`` which will install all the necessary libraries.**
* **Finally, type ``sudo python3 PhoneSploitGui.py``.**
