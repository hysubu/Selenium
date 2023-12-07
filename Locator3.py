#Using Link List and Partial LineList


# from selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# services_object = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=services_object)
# driver.get('https://www.naukri.com/companies-hiring-in-india?src=gnbCompanies_homepage_srch')

# driver.find_element(By.LINK_TEXT , 'Jobs').click()



# from selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# services_object = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=services_object)
# driver.get('https://www.naukri.com/companies-hiring-in-india?src=gnbCompanies_homepage_srch')
#
# driver.find_element(By.PARTIAL_LINK_TEXT , 'Jo').click()





# Using Tag name
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
services_object = Service('C:\Driver\chromedriver.exe')
driver = webdriver.Chrome(service=services_object)
driver.get('https://www.naukri.com/')
element = driver.find_elements(By.TAG_NAME, 'li')
print(len(element))
for i in element :
    print(i.text)

