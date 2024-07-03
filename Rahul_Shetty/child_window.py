from selenium import webdriver  #here selenium is package and Selenium is one of the class in it
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.EdgeOptions()
# Add argument to start Edge browser maximized
options.add_argument("--start-maximized")
# Set preferences using a dictionary
prefs = {"user_experience_metrics.personalization_data_consent_enabled": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"button[id='tabButton']").click()
time.sleep(4)

windows_opened = driver.window_handles   # retrieve all the windows opened as list
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.ID,"sampleHeading").text)
driver.close()   # child window will be closed as the control is there in it
driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.ID,"tabButton").text)
time.sleep(5)