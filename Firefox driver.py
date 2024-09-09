import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
time.sleep(2)
browser.get('https://www.google.co.in/')
browser.find_element(By.ID,"APjFqb").send_keys("cognine technologies")

