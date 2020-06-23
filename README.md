# Automated-Hangouts-Bot-using-Camera-io

---------------------------------------------------------------------------------------------
## What I used:
* Windows 10 mobile phone
     * Install "Camera IO" app and enable motion detection on client PC
* Python
* Windows 10 PC

---------------------------------------------------------------------------------------------
## Basic Overview

* Used Selenium Python module to automatically scan smartphone's database for new images from the "camera io" app and download them to user's hard drive.

* Next I made a Hangouts bot to send texts and upload those previously downloaded pictures to Google Hangouts where I can access them from anywhere in the world.

* File_deleter.py is optional. It will simply delete all pictures form the phone to save space.

---------------------------------------------------------------------------------------------
# Hangouts_Bot.py

Used Selenium Python module to automatically send texts and upload pictures to Google Hangouts from a local file directory. The timing of messages and its content can be pre set and altered dynamically as the user wishes.

---------------------------------------------------------------------------------------------
# Server_file_downloader.py

Used Selenium Python module to access server hosted by smart phone and constantly scan for any new picutures. If a new picture is found, it will be automatically downloaded to the user specified directory on their computer.

---------------------------------------------------------------------------------------------
# File_deleter.py

Used Selenium Python module to access server hosted by smart phone and delete all pictures in order to save internal space on phone's memory. Deletion is fully automated and can also be controlled by the user.


### ***** "Hangouts_Bot.py" and "Server_file_downloader.py" are intended to be run together to increase automation *****
 

