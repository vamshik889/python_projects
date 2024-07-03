import time, datetime
from selenium import webdriver

from selenium.webdriver.common.by import By
import time

print("sample test case started")
#driver = webdriver.Chrome(r"C:\Users\vaMshi\Downloads\chromedriver_win32\chromedriver.exe")
# driver=webdriver.firefox()
driver=webdriver.Edge(executable_path=r"C:\Users\vaMshi\Downloads\edgedriver_win64\msedgedriver.exe")
# maximize the window size
driver.maximize_window()
# navigate to the url
driver.get("https://www.google.co.in/")
# identify the Google search text box and enter the value

driver.find_element(By.XPATH, "//textarea[@id='APjFqb']" ).send_keys("Hello")

time.sleep(10)