from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


driver= webdriver.Chrome()
url="https://www.thesparksfoundationsingapore.org/"
driver.get(url)

# TestCase 1: Title
print("TestCase #1:")
if(driver.title):
    print("Title Verification Successful: ",driver.title)
else:
    print("Title Verification Failed!\n")


#TestCase 2: Home button
print("TestCase #2:")
try: 
    link = driver.find_element_by_link_text("The Sparks Foundation")
    link.click()    
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

# TestCase 3: Check if navbar appears
print("TestCase #3:")
try:

    link=driver.find_element_by_class_name("navbar")
    link.click()
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")   


# TestCase 4: Check if logo appears
print("TestCase #4:")
try:

    driver.find_elements_by_xpath("logo_small.png")    
    print("logo Verification Successful!\n")
except NoSuchElementException:
    print("logo Verification Failed!\n")   

#TestCase 5: About Us Page
print("TestCase #5:")
try:
    link=driver.find_element_by_link_text('About Us')
    link.click()
    time.sleep(3)
    link=driver.find_element_by_link_text('Vision, Mission and Values')
    link.click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

#TestCase 6: Policies and Code
print('TestCase #6:')
try:
    link=driver.find_element_by_link_text('Policies and Code')
    link.click()
    time.sleep(3)
    link= driver.find_element_by_link_text("Policies")
    link.click()
    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)   

#TestCase 7: Links page
print('TestCase #7:')
try:
    link=driver.find_element_by_link_text('LINKS')
    link.click()
    time.sleep(3)
    link=driver.find_element_by_link_text("Software & App")
    link.click()
    time.sleep(3)
    link=driver.find_element_by_link_text('Visit LINKS @TSF')
    link.click()
    time.sleep(3)
    print('Links Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')
    time.sleep(3)

#TestCase 8: Join us page
print('TestCase #8:')
try:
    link=driver.find_element_by_link_text('Join Us')
    link.click()
    time.sleep(3)
    link=driver.find_element_by_link_text("Why Join Us")
    link.click()
    time.sleep(3)
    link=driver.find_element_by_link_text('Why Join Us')
    link.click()
    time.sleep(3)
    print('Join us Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')
    time.sleep(3) 

#TestCase 9:   Check the Contact us Page
print("TestCase #9:")
try:
    link=driver.find_element_by_link_text("Contact Us")
    link.click()
    time.sleep(3)
    info = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)
   
    # print(info.text)
    if(info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')
   
    # assert driver.page_source.find("+65-8402-859, info@thesparksfoundation.sg")
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")   

#TestCase 10: Programs page
print('TestCase #10:')
try:
    link=driver.find_element_by_link_text('Programs')
    link.click()
    time.sleep(3)
    link=driver.find_element_by_link_text("Student Scholarship Program")
    link.click()
    time.sleep(3)
    link=driver.find_element_by_link_text('Student Mentorship Program')
    link.click()
    time.sleep(3)
    print('Programs Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')
    time.sleep(3)         
