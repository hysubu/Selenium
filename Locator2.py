#Using Locator
# Using id to find the elements

# from selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# services_object = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=services_object)
# driver.get('https://www.linkedin.com/')
# driver.find_element(By.ID , 'session_key').send_keys("8249596972")
# driver.find_element(By.ID , 'session_password').send_keys('Subu2309')
# driver.find_element(By.XPATH , '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
# driver.maximize_window()
# driver.implicitly_wait(50)




# ---------------------------------------------------------------------------------------
# Using Name Locator to find the elements

# from selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# services_object = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=services_object)
# driver.get('https://www.linkedin.com/')
# driver.find_element(By.NAME , "session_key").send_keys('8249596972')  # used NAME Attribute
# driver.find_element(By.NAME , "session_password").send_keys('Subu2309') # Here Used NAME Attribute
# driver.find_element(By.XPATH , '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()



# Using Class Name Attribute

# from selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# services_object = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=services_object)
# driver.get('https://www.linkedin.com/')
# used_attribute = driver.find_elements(By.CLASS_NAME,"text-color-text") # Here Used CLASS_NAME  Attribute
# print(len(used_attribute))

