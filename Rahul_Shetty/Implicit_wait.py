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


driver.implicitly_wait(5) # max time of 5seconds it waits for all the elements to locates
#Implicity wait is a Global timeout

#*Exceptional case for Implicity wait is when we are trying to get the find elements as list at this case it won't wait as in the first step we will get empty list and driver thinks that the expected list is retrieved and it will fail
#eg: remove time.sleep from line 22 and test will fail

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class = 'products']/div")
print(len(results))
for result in results:
    result.find_element(By.XPATH,"div/button").click()    #here result is nothing but parent tag (i.e //div[@class = 'products']/div) and by chaining we are clicking the button element
                                                            #we are not using driver.find element in above step where it will search on whole web page, if we use within parent element like above it searches only within parent element

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
print("Apply clicked")
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)