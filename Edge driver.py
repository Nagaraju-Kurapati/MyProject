import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
time.sleep(2)
browser.get('https://www.orangehrm.com/')
browser.find_element(By.NAME,"EmailHomePage").send_keys("kurapatinagaraju547@gmail.com")
time.sleep(3)


