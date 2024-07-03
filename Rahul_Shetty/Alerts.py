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





name = "Vamshi"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.NAME,"enter-name").send_keys(name)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
""" #id will be the CSS selector in above step"""
time.sleep(3)

#Switch to alert mode as alerts wont be having any html tags to perfrom the activities

alert = driver.switch_to.alert  #alert obj is created, now we can use this obj to handle the alerts
alert_text = alert.text
print(alert_text)
assert name in alert_text  # validation whether the name is present in the alert or not
alert.accept()  # to accept the alert, which is positive

#alert.dismiss()  # to dismiss the alert
