# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from cred import name,website,fullName,phone,msg
import time
import uuid

email = uuid.uuid4().hex + '@gmail.com'
# webdriver.Chrome() will be used

driver = webdriver.Chrome(executable_path='/home/shivam/Downloads/pycharm/chromedriver')

# URL of the website
url = "https://dev.gokwik.co/contact/"

driver.get(url)
#going_to_Contact_page



driver.find_element_by_xpath('//*[@id="companyName"]').send_keys(name)

driver.find_element_by_xpath('//*[@id="website"]').send_keys(website)

driver.find_element_by_xpath('//*[@id="fullName"]').send_keys(fullName)

driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)


driver.find_element_by_xpath('//*[@id="tel"]').send_keys(phone)

driver.find_element_by_xpath('//*[@id="msg"]').send_keys(msg)


time.sleep(2)


driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div/div[2]/div/div[1]/form/div[4]/div/button').click()

time.sleep(2)

