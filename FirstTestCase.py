
#selenium Version-4

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://infocampus.co.in/job/login.php")
# driver.find_element(By.NAME,"email").send_keys("subratmohanty2309@gmail.com")
# driver.find_element(By.NAME,"pass").send_keys("subu2309")
# driver.find_element(By.CSS_SELECTOR ,'button[type="submit"].btn').click()
# fine_h2 = driver.find_element(By.TAG_NAME , "h2")
# success = fine_h2.text
# expected_success ="Current Trending Jobs Opening"
# if success == expected_success :
#     print("Successfully ")
# else:
#     print("Not Successfully")
# driver.close()



from selenium.webdriver.chrome.service import Service
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver_servuces = Service("C:\Driver\chromedriver.exe")
obj = webdriver.Chrome(service=driver_servuces)
obj.get("https://www.linkedin.com/login/")
obj.find_element(By.ID , "username").send_keys("8249596972")
obj.find_element(By.ID, "password").send_keys("Subu2309")
obj.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button').click()











# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Edge()
# driver.get("https://www.linkedin.com/login/")
# driver.find_element(By.ID , "username")

