from selenium import webdriver  #here selenium is package and webdriver is one of the class in it

from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import expected_conditions as EC
import time

from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\vaMshi\Downloads\edgedriver_win64\msedgedriver.exe")  #"""A Service class that is responsible for the starting and stopping of `msedgedriver`.
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://demoqa.com/")
print(0)
time.sleep(10)
driver.find_element(By.XPATH,"//h5[text()='Forms']").click()
print("Forms clicked")
#ID, Xpath, css selector, classname, name, linktext
driver.find_element(By.XPATH,"//span[text()='Practice Form']").click()  #Xpath
print("practice form selected")
time.sleep(5)
driver.find_element(By.ID, "firstName").send_keys("Vamshi") # ID
driver.find_element(By.ID, "lastName").send_keys("Krishna") # ID
driver.find_element(By.CSS_SELECTOR, "input[id ='userEmail']").send_keys("vamshi.v@gmail.com")  #CSS Selector
print("Email entered")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@value = 'Male']").click()

#Xpath = //tagnamep[@attribute='value']
# CSS Selector = tagname[attribute='value']    #difference is we will have // and @ in xpath but not in Css selector
# .text will grab the text from the element

# * To Generate the CSS for just use .clssaname OR #id which will be the CSS selector
