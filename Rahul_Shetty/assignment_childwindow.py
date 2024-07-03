from selenium import webdriver  #here selenium is package and Selenium is one of the class in it
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#Problem statement : Using window handles grab the email from child window and use in parent window to login


options = webdriver.EdgeOptions()
# Add argument to start Edge browser maximized
options.add_argument("--start-maximized")
# Set preferences using a dictionary
prefs = {"user_experience_metrics.personalization_data_consent_enabled": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,"a[class='blinkingText']").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
time.sleep(3)
full_text = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
print(full_text)
#extract the email from the paragraph
words = full_text.split(sep=" ")
print(words)
email=""
for word in words:
    if "@" in word:
        email+=word
        break
print(email)
driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR,"input[id='username']").send_keys(email)
driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys("learning")
driver.find_element(By.CSS_SELECTOR,"input[value='user']").click()
time.sleep(3)
driver.find_element(By.ID,"okayBtn").click()
time.sleep(3)
dropdown = Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
dropdown.select_by_index(1)
print("Teacher is selected")
driver.find_element(By.CSS_SELECTOR,"#terms").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
time.sleep(5)
error_message = driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-danger col-md-12']").text
print(error_message)















