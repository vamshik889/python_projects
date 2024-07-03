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
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()    #OR driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print(products)
for product in products:
    text = product.find_element(By.XPATH,"div/h4/a").text
    if text == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
print(text)
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//button[@class ='btn btn-success']").click()
print("checkout clicked")
driver.find_element(By.ID,"country").send_keys("ind")
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[text()='India']")))
driver.find_element(By.XPATH,"//a[text()='India']").click()
print("country selected")
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
success_msg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success" in success_msg

