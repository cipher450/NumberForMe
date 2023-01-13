
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import csv
from time import sleep
import os
import keyboard
#will have a start menu from whichi thair will be 3 option
#options being :
#Get numbers
#Listen on new sms (On a given url , will retrun that last 3 sms's)
#Exit

#user entre the country from which they want thair number to be from then will gather numbers from diffrent website 
#

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)


url_list =[ 'https://receivesms.cc/'  ]

numbers_list=[]

clear = os.system('cls')


#this is what a link for a given number looks like : https://receivesms.cc/sms/{NUMBER}


def receivesms():
    os.system('cls')
    global url_list
    global numbers_list
    country = input('Which Country ? > ' )
    country=country.lower()
    driver.get(url_list[0])
    num_box = driver.find_elements(By.CLASS_NAME,'number-box')
     #this sleep is because of my internet speed 
    sleep(2)
  

    for box in num_box: 
       
        box_country = box.find_elements(By.CLASS_NAME,'number-title')
        cn = box_country[1].text.lower()
       
        
       
        if country==cn:
            numbers_list.append(box_country[0].text)
            numbers_list.append(box_country[1].find_element(By.TAG_NAME,'a').get_attribute('href'))
            
    

def getsms(link):
    # 
    
    while not keyboard.is_pressed('s'):
        os.system('cls')

        driver.get(link)
        #this sleep is because of my internet speed 
        sleep(2)
        sms_table = driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div/div[1]/div/div/section[2]/div/div[2]')
        row = sms_table.find_elements(By.CLASS_NAME,'body_sms_row')[0]
        print('-----------------------------------')
        print('Time : ' ,row.find_elements(By.TAG_NAME,'li')[0].text)
        print('Sender : ' ,row.find_elements(By.TAG_NAME,'li')[1].text)
        print('Message : ' ,row.find_elements(By.TAG_NAME,'li')[2].text)
        print('-----------------------------------')
        print('Press S to stop')
        sleep(15)



while True:
    os.system('cls')
    print("-----------------")
    print("1 > Get fresh numbers ")
    print("2 > Show numbers ")
    print("3 > Listen for new messages ")
    print("4 > Exit")
    print("-----------------")
    option = input('> ')
    match option:
        case'1':
            receivesms()
        case'2':
            print(numbers_list)
        case'3':
            getsms(input('Entre link > '))
        case '4':
            driver.close()
            break
 
   
