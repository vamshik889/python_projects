from selenium import webdriver  #here selenium is package and Selenium is one of the class in it
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.edge.service import Service
service_obj = Service(r"C:\Users\vaMshi\Downloads\edgedriver_win64\msedgedriver.exe")  #"""A Service class that is responsible for the starting and stopping of `msedgedriver`.
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
# print(driver.title) # title property to seee the title of the webpage
# print(driver.current_url) # to see the current Url of the webpage
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.back()
# driver.refresh()
# driver.minimize_window()
#driver.close() #to close the browser
