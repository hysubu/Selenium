
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:\Driver\chromedriver.exe")
object_driver = webdriver.Chrome(service=service_object)
object_driver.get("https://www.linkedin.com/home")
object_driver.find_element(By.XPATH , '//*[@id="session_key"]').send_keys('8249596972')
object_driver.find_element(By.XPATH ,'//*[@id="session_password"]' ).send_keys('Subu2309')
object_driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
object_driver.find_element(By.XPATH , '//*[@id="global-nav-typeahead"]/input').send_keys('subrat mohanty')

result = object_driver.find_element(By.TAG_NAME ,'h2')
print("result" , result.text)

# object_driver.get("https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit")



# if result.text == "Results" :
#     print("success")
# else:
#     print("not success")
object_driver.close()





