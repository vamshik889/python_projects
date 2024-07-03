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
driver.maximize_window()
driver.implicitly_wait(5)


#Frames : Embedded html on top of parent html

driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH,"//a[text()='Frames']").click()
driver.find_element(By.LINK_TEXT,"iFrame").click()

driver.switch_to.frame("mce_0_ifr")   # Switching to iframe - Use iframe ID or name, here we used ID
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Entered the text in iframe")
print(driver.find_element(By.CSS_SELECTOR,"#tinymce").text)

driver.switch_to.default_content()   #switch back to the browser scope from iframe
print(driver.find_element(By.TAG_NAME,"h3").text)





