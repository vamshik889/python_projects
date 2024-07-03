from selenium import webdriver  #here selenium is package and Selenium is one of the class in it
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

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class = 'products']/div")
print(len(results))
product_names=[]
for result in results:
    product = result.find_element(By.XPATH,"h4").text  #extracting the names of products and appending to list
    product_names.append(product)
    result.find_element(By.XPATH,"div/button").click()    #here result is nothing but parent tag (i.e //div[@class = 'products']/div) and by chaining we are clicking the button element
                                                            #we are not using driver.find element in above step where it will search on whole web page, if we use within parent element like above it searches only within parent element
print(product_names)
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)

#sum validation
list = []
sum = 0
amount_3 = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
for amount in amount_3:
    sum+=int(amount.text)
print(sum)
# for amount in amount_3:
#     list.append(amount.text)
# for i in list:
#     ans+=int(i)
# print(ans)

total = driver.find_element(By.CSS_SELECTOR,".totAmt").text

assert sum == int(total)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
print("Apply clicked")
wait = WebDriverWait(driver,10)   #wait object
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)