# Using Css Selector

#  find the element using Tag and Id Combination
from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object_service = Service('C:\Driver\chromedriver.exe')
driver = webdriver.Chrome(service=object_service)
driver.get('https://in.linkedin.com/')
driver.find_element(By.CSS_SELECTOR , 'input#session_key').send_keys('8249596972')
driver.find_element(By.CSS_SELECTOR , 'input#session_password').send_keys('Subu2309')



# Using Tag and Class attrobute

# from  selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# object_service = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=object_service)
# driver.get('https://in.linkedin.com/')
# driver.find_element(By.CSS_SELECTOR , 'input.text-color-text').send_keys('8249596972')
# driver.find_element(By.CSS_SELECTOR , 'input.text-color-text').send_keys('Subu2309')




# useing tagname and attribute with value
from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object_service = Service('C:\Driver\chromedriver.exe')
driver = webdriver.Chrome(service=object_service)
driver.get('https://in.linkedin.com/')
driver.find_element(By.CSS_SELECTOR , 'input[id=session_key]').send_keys('8249596972')
driver.find_element(By.CSS_SELECTOR , 'input[id = session_password]').send_keys('Subu2309')

