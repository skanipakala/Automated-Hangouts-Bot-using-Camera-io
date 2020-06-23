######################### AUTOMATED CAMERA-IO DATABASE ACCESS SECURITY SYSYTEM #########################

#       Desinged by Sri Kanipakala Version 1.0 [Beta]
#       This is the Hangouts BOT that will upload new pictures and send it to you

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep
import os
import sys
from datetime import datetime
import shutil
import schedule
import time


## Construct automated message and send it via Hangouts chat box
def sendUpdate(message_Driver, isFirst, textBoxFrame, textBox):

  toReturn = ''

  if(isFirst):  

    ## New windows to read the battery percentage on windows phone
    message_Driver.execute_script("window.open('');")
    message_Driver.switch_to.window(message_Driver.window_handles[1])
    message_Driver.get('https://192.168.1.11/#Apps%20manager')

    advance_button = message_Driver.find_element_by_id('details-button')
    advance_button.click()

    advance_button2 = message_Driver.find_element_by_id('proceed-link')
    advance_button2.click()
    toReturn = '[LAUNCH SUCCESSFUL] Hangouts and User connection established!\n'

  else:    
    message_Driver.switch_to.window(message_Driver.window_handles[1])

  sleep(1)   
  message_Driver.refresh()
  sleep(1)
  batteryButton = message_Driver.find_element_by_id('batteryHeader')
  batteryNow = batteryButton.get_attribute("aria-label")  
  
  print('[UPDATE STATUS] Notify user that everything is fine   :)')
  
  dateTimeObj = datetime.now()
  timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
  
  toReturn= toReturn + 'Current time is: ' + timestampStr + " " + batteryNow + " "
  
  message_Driver.switch_to.window(message_Driver.window_handles[0])

  message_Driver.switch_to_default_content()
  message_Driver.switch_to_frame(textBoxFrame)
  textBox.send_keys(toReturn)
  textBox.send_keys(Keys.ENTER)
 

    
def start(username,password):  

  ## Import drivers and set up pre-requisites
  driver=webdriver.Chrome('C:/chromedriver.exe')
  driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')

  driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
  driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="identifierNext"]').click()    
  
  driver.implicitly_wait(1)
  
  tryAgain = True  
  while(tryAgain):
    
    try:
      driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)       
    except:
      print('[!] Login Failed... Auto-Retrying NOW')
      tryAgain = True
    else:
      tryAgain = False
      

  driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
  driver.get('https://hangouts.google.com')
  sleep(1)
  
  signInButton= driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[4]/div[3]/div/div/ul/li[3]/div[1]')  
  signInButton.click()
  sleep(1)
 
  driver.switch_to_default_content()
  html= driver.page_source

  ## To switch into iframe panel for "Contacts and Conversations"
  convoIndex = html.find('class="Xyqxtc"')
  crop = html[convoIndex-14 :convoIndex-2]  
  html = ''

  sleep(1)

  driver.switch_to_frame(crop)
  print('[FRAME SWITCH] ', crop)

  sleep(1)

  ## To click on the first chat box in the list of contacts in Hangouts
  icon = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]')
  icon.click()

  driver.switch_to_default_content()
  print('[FRAME SWITCH] Default')

  ## To switch into iframe panel for The POP-UP chat window
  html= driver.page_source
  
  textBoxIndex = html.find('class="Xyqxtc"', convoIndex+50, len(html))
  crop2 = html[textBoxIndex-17: textBoxIndex]
  firstQ = crop2.find('"', 0, 7)
  secondQ = crop2.find('"', 7, len(crop2))  
  crop2 = crop2[firstQ+1:secondQ]
  
  driver.switch_to_frame(crop2)
  print('[FRAME SWITCH] ', crop2)
  html = ''
  
  sleep(1)

## Attempt all to minimize Error
  try:
      textBox = driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div/div[3]/div/div/div[4]/div[2]/div[3]/div/div[2]')
  except:
      print('X-PATH BAD')
  try:
      textBox = driver.find_element_by_css_selector('#\:93\.f')
  except:
      print('css-BAD-OK')
  try:
      textBox = driver.find_element_by_id(':93.f')
  except:
      print('ID-BAD-OK')
  try:
      textBox = driver.find_element_by_class_name('vE dQ editable')
  except:
      print('class name-BAD-OK')


  ## Send the initial message, so boolean == True
  sendUpdate(driver, True, crop2, textBox)
  
  ## Send a periodic message letting user know program is still running successfully
  schedule.every(10).seconds.do(sendUpdate,driver, False, crop2, textBox)
  
  updateAvailable = False
  while(True):

    ##Store all file names in an array for faster access
    array = getNames()
    counter = 0
    
    schedule.run_pending()
   
    sleep(1)
    
    while(counter<len(array)):
    
        uploadButton = driver.find_element_by_xpath('//button[@title = "{}"]'.format('Attach a photo')) 
        uploadButton.click()
 
        driver.switch_to_default_content()
        print('[FRAME SWITCH] Default')        

        html= driver.page_source

        ##Identify frame of the new pop-up download menu and switch to it
        classIndex = html.find('class="Xyqxtc"'  , textBoxIndex+600, len(html))  
        crop3= html[classIndex-19: classIndex]  
        firstA = crop3.find('"', 0, 7)
        secondA = crop3.find('"', 7, len(crop3))
        crop3 = crop3[firstA+1:secondA]  
        driver.switch_to_frame(crop3)
        print('[FRAME SWITCH] ', crop3)
        
        sleep(1)

        ##Identify the smaller-popup box frame and switch to it from parent frame (crop3)
        newFrame = driver.find_element_by_class_name('Yc-mq')
        driver.switch_to_frame(newFrame)

        #Detect file input button and send it the File Directory
        fileInput = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/input')
        print('Detected Picture: ', array[counter])
        fileInput.send_keys(array[counter])
    
        sleep(4)
        
        src = r"X:\securitycam\FRESH"
        dest = r"X:\securitycam\DONE"

        ## Move the newly uploaded picture from "FRESH" to "DONE" to avoid duplicate uploads
        ## "DONE" will serve as an archive folder of all pictures ever uploaded to Hangouts
        try:
          shutil.move(array[counter],dest)
        except:
            print('[IGNORE THIS] file redundant error')


        ## Have to switch back to textBox frame to press the enter key
        driver.switch_to_frame(crop2) 
        textBox.send_keys(Keys.ENTER)
        print('[ALERT!] File Sent On Hangouts!')
    
        sleep(2)
        counter = counter + 1
 

## Scan the specified directory for a array of all file directories
def getNames():
  array = []  
  for root, dirs, files in os.walk('X:\securitycam\FRESH'):
    for singlePic in files:
      if singlePic.endswith('.jpg'):
        picDirectory = os.path.join(root,singlePic)
        print(os.path.join(root,singlePic))
        array.append(picDirectory)
  return array


google_username = 'ENTER YOUR GOOGLE USERNAME HERE @GMAIL.COM IS NOT NEEEDED'
google_password = 'ENTER YOUR PASSWORD FOR GOOGLE ACCOUNT'

start(google_username,google_password)
print('[lAUNCHED] Starting Hangouts BOT photo upload program')
