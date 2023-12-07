
# Or Opearter using Xpath

# from selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# object = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=object)
# driver.get('https://automationpanda.com/contact/')
# driver.maximize_window()
# driver.find_element(By.XPATH , "//input[@name ='g3-name' or @class = 'name']").send_keys('subrat mohanty')
# driver.find_element(By.XPATH , "//input[@name ='g3-email' or @class = 'email']").send_keys('subratmohanty2309@gmail.com')
# driver.find_element(By.XPATH, "//button[@class ='wp-block-button__link']").click()


# # And Opeartor
#
# from selenium import  webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# object = Service('C:\Driver\chromedriver.exe')
# driver = webdriver.Chrome(service=object)
# driver.get('https://automationpanda.com/contact/')
# driver.maximize_window()
# driver.find_element(By.XPATH , "//input[@name ='email' and @id = 'subscribe-field']").send_keys('subb@gmail.com')
# driver.find_element(By.XPATH, "//button[@type = 'submit' and  @class='wp-block-button__link']").click()





d={"col":

 [{"Name":"cl1", "length":12,"columnType":"xes", "type" :"string" },
  { "Name": "c12", "length":13, "columnType" :"xyx", "type": "string" },
  {"Name": "c13", "length":14, "columnType":"xyz", "type":"string"}]}

emp   = []
for i in d["col"] :
    emp.append(i["Name"])
print(emp)



