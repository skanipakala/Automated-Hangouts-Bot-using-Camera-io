######################### AUTOMATED CAMERA-IO DATABASE ACCESS SECURITY SYSYTEM #########################

#       Desinged by Sri Kanipakala Version 1.0 [Beta]
#       This is the server file downloadeder that will download new pictures taken from camera-phone

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options



##Constantly read the HTML page source and construct array of all picture ID numbers
def calc(html, ID):
    keepSearching = True
    START_INDEX = 0
    
    while(keepSearching):
        picIndex = html.find('.jpg", "Name"', START_INDEX, len(html))

        if(picIndex !=-1):
            rough = html[picIndex-5:picIndex]      
            bracket = rough.find('] ')
        
            numberID = rough[bracket+2:len(rough)]
            num = int(numberID)
            ID.append(num)            
            START_INDEX = picIndex+15

        else:
            keepSearching = False

    ID.sort()
    return ID


def getStarted():

    oldMax = 0

    ##Bypass Chrome Warning message and Proceed to server IP address and file directory url where files are located
    driver.get('https://192.168.1.11/api/filesystem/apps/files?knownfolderid=Pictures')

    advance_button = driver.find_element_by_id('details-button')
    advance_button.click()

    advance_button2 = driver.find_element_by_id('proceed-link')
    advance_button2.click()
    
    #[Keep commented unless you have Authentication turned on on windows Phone]#

    #PIN = driver.find_element_by_id('pin')
    #PIN.send_keys('b1W3S6')
    #advance_button3 = driver.find_element_by_id('doPair')
    #advance_button3.click()
    #remember = driver.find_element_by_id('persistent')
    #remember.click()

    sleep(3)
    html=''
    
    ## Derive the key name that is common for all pictures in server

    searchName = True
    while(searchName):
        sleep(2)
        driver.refresh()
        html= driver.page_source
        print('[Scanning for NAME]')
        left = html.find("IO")
        right = html.find("Motion]")

        roughString = html[left:right]
        
        if(left != -1):
            collect = roughString.split(" ")
            name = collect[1]
            print('TARGET NAME FOUND --> ', name)
            searchName = False

    ##Initialy when ther are no new files on server
    newMax =0

    ## Continue to fresh the HTML page source until a new file name is found
    while(True):
        
        sleep(2)
        driver.refresh()
        print('[Scanning for new PIC]')
       
        ID = []            
        ID = calc(html, ID)
        newMax = ID[len(ID)-1]              
        
        html= driver.page_source
        
        ## Execute Download command to download ONLY NEWLY ADDED Pics
        if(newMax>oldMax):
            number = oldMax+1

            while(number <= newMax):
                print('[Downloading Pic] ', 'Camera IO ' + name + ' [Motion] ' + str(number) + '.jpg')
                URL = 'https://192.168.1.11/api/filesystem/apps/file?knownfolderid=Pictures&filename=' + 'Camera IO ' + name + ' [Motion] ' + str(number) + '.jpg'
                driver.get(URL)
                number = number+1
                
            oldMax = newMax            

################ PROGRAM DRIVER CODE IS BELOW ################
    
options = webdriver.ChromeOptions()

#Setting following chrome preferences:
#1 Download location (Directory as String)
#2 Turn off safe browsing

preferences = {"download.default_directory":  "X:\securitycam\FRESH", "safebrowsing.enabled": "false"}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=options ,executable_path='C:/chromedriver')

print('Preferences successfully imported...Starting Program')
getStarted()
