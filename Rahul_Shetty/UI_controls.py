from selenium import webdriver  #here selenium is package and Selenium is one of the class in it
from selenium.webdriver.common.by import By
import time
options = webdriver.EdgeOptions()
# Add argument to start Edge browser maximized
options.add_argument("--start-maximized")
# Set preferences using a dictionary
prefs = {"user_experience_metrics.personalization_data_consent_enabled": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# below code is useful when we dont have any value, name, or ID for the element

#Check box

# options = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")  #use find elements to find multiple elements
#print(len(options))
# for i in options:
#     if i.get_attribute("value") == "option2":
#         i.click()
#         print(i.is_selected())  #validation whether the check box is selected or not
#         break

#Radio Button

#1st method:

# radio = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# for i in radio:
#     if i.get_attribute("value") == "radio2":
#         i.click()
#         print(i.is_selected())  #validation whether the check box is selected or not
#         break

#2nd method:

# radio = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# radio[1].click()  # to click the radio button2 by using the index of elements
# print(radio[1].is_selected())


#is_displayed() method to check whether the element is displayed on the UI or not

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,'hide-textbox').click()
time.sleep(5)
assert not driver.find_element(By.ID,"displayed-text").is_displayed()