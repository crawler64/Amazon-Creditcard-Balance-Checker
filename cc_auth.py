# RUN THIS FILE FIRST BEFORE YOU USE cc_check.py
# ENTER YOU Credentials in popup of Chromium

WebsiteURL = 'https://amazon.lbb.de/security/login'

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#if you want to change your userfolder, please do so: But you also need to change this in the cc_check.py
chrome_options.add_argument("user-data-dir=selenium") 
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.wait = WebDriverWait(driver, 10)
driver.get(WebsiteURL)

#assert "Enter your credentials" in driver.title
driver.wait
time.sleep(180)
driver.quit()
