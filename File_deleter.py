######################### AUTOMATED CAMERA-IO DATABASE ACCESS SECURITY SYSYTEM #########################

#       Desinged by Sri Kanipakala Version 1.0 [Beta]
#       This is the server file deleter that will delete all pictures taken from camera-phone in pictures directory

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import sys


## Change to "True" if you have a warning screen on chrome
secureAccess = False

driver = webdriver.Chrome('C:/chromedriver')
driver.get('http://192.168.1.11/#File%20explorer')
sleep(1)

## To bypass secure access webpage
if(secureAccess):
    advance_button = driver.find_element_by_id('details-button')
    advance_button.click()
    advance_button2 = driver.find_element_by_id('proceed-link')
    advance_button2.click()


## Go to the directory URL of all pictures on server
driver.get('http://192.168.1.11/#File%20explorer')
sleep(1)
pictures_Button = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[5]/div/div[4]/div[2]")
print('[+] Picture Directory Found')
pictures_Button.click()
sleep(2)

try:    
    delete_button = driver.find_element_by_xpath('//span[@aria-label="{}"]'.format('delete'))
except:
    print('[!] NO Pictures available to delete in folder\nAUTO-EXIT in 5 seconds...')
    sleep(5)
    driver.close()
    driver.quit()
    sys.exit()

start = input('Commence BULK Delete? Type y=YES  n=NO').lower()
counter = 0

print('\nPress control + C to STOP the program\n')

while(start =='y' or start =='yes' or start =='ok'):

    try:        
        delete_button = driver.find_element_by_xpath('//span[@aria-label="{}"]'.format('delete'))
    except:
        
        print('[ :) ] Check for any errors please')
        print('[SUCCESS] ' + str(counter) + ' files deleted from server!\nAUTO-EXIT in 5 seconds...')
        
        sleep(5)
        driver.close()
        driver.quit()
        sys.exit()
    
    delete_button.click()
    sleep(0.500)
    alertBOX = driver.switch_to.alert
    
    if(alertBOX.text.find('File deletion failed') !=-1):
       print('Something went wrong, close all program instances and chromedriver.exe windows and try again')               
        
    print('[!] WARNING deleting file: ', alertBOX.text)
    
    alertBOX.accept()
    counter+=1
    sleep(0.750)



    
    
    
