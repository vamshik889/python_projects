from selenium import webdriver  #here selenium is package and Selenium is one of the class in it
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()

# Add argument to start Edge browser maximized
options.add_argument("--start-maximized")

# Set preferences using a dictionary
prefs = {"user_experience_metrics.personalization_data_consent_enabled": True}
options.add_experimental_option("prefs", prefs)

# Initialize Edge WebDriver with options
driver = webdriver.Edge(options=options)

# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

# service_obj = Service(r"C:\Users\vaMshi\Downloads\edgedriver_win64\msedgedriver.exe")  #"""A Service class that is responsible for the starting and stopping of `msedgedriver`.
# driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
#driver.get("https://rahulshettyacademy.com/angularpractice/")


#Static dropdown -> for this we will use select class
# * if we see any select tags in the html code that means it is a static dropdown and simply by using select class we can handle the options from the dropdown

# dropdown = Select(driver.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']"))  #dropdown(variable) is an object of thge select class here
# time.sleep(3)
# dropdown.select_by_index(0)
# dropdown.select_by_visible_text("Female")
# time.sleep(3)

#Dynamic_Dropdowns

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a") #in CSS selector to traverse into child tag we use space where in xpath we use /
#storing the countries names in a list
print(len(countries))
time.sleep(5)
for country in countries:
    if country.text == "India":
        country.click()
        print("India selected")
        break
time.sleep(5)

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"  #verifying whether the country is selected or not by using get attribute



