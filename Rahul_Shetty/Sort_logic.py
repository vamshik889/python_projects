from selenium import webdriver  #here selenium is package and Selenium is one of the class in it
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.EdgeOptions()
# Add argument to start Edge browser maximized
options.add_argument("--start-maximized")
# Set preferences using a dictionary
prefs = {"user_experience_metrics.personalization_data_consent_enabled": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Edge(options=options)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//tr/th[@role ='columnheader'][1]").click()

veggie_list = driver.find_elements(By.XPATH,"//tr/td[1]")  #collecting the browser sorted elements

browser_sorted =[]
for i in veggie_list:          #extracting the text from elementes and appending into list
    browser_sorted.append(i.text)
print(browser_sorted)
sort_copy =browser_sorted.copy()         #creating a new list as we are sorting the browser sorted list using python method

browser_sorted.sort()
assert sort_copy == browser_sorted
