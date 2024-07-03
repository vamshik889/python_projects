from selenium import webdriver  #here selenium is package and Selenium is one of the class in it

from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import expected_conditions as EC
import time

from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\vaMshi\Downloads\edgedriver_win64\msedgedriver.exe")  #"""A Service class that is responsible for the starting and stopping of `msedgedriver`.
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.NAME,"username").send_keys("tomsmith")
driver.find_element(By.NAME,"password").send_keys("SuperSecretPassword!")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
success_message = driver.find_element(By.XPATH,"//div[@class='flash success']").text  # css selector is #flash (use #id for css of any element)
assert "logged" in success_message
print(success_message)

# if "You logged into a secure area!" in success_message:
#     print(success_message)
#     assert True
# driver.find_element(By.LINK_TEXT,"Elemental Selenium").click()  #Link text - first confirm whether the element is a anchor tag or not
time.sleep(5)