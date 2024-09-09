import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
time.sleep(4)
browser.get('http://amazon.com/')
time.sleep(5)
browser.find_element(By.XPATH,"/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/input").send_keys("mobile")

