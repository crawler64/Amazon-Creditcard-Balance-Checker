# encoding=utf8  
import sys, getopt

reload(sys)  
sys.setdefaultencoding('utf8')

import re
import ssl
import os
import os.path
from ConfigParser import ConfigParser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# cc.py -d 1/True turns Debug mode on. 
# You can turn this on, to turn on the "file found:" comment, just to check


def main(argv):
   Debug = False
   try:
      opts, args = getopt.getopt(argv,"d:",["dbgpara="])
	
   except getopt.GetoptError:
		Debug = False
		return Debug
	
   for opt, arg in opts:
	if opt in ("-d","--dbgpara"):
		if (arg == 'True') or (arg == '1'):
			Debug = True
	return Debug
 
def init_conf():
	conf = ConfigParser()
	project_dir = os.path.dirname(os.path.abspath(__file__))
	conf.read(os.path.join(project_dir, 'config.ini'))
	
	# Read config Settings - Do not change URLs if no necessary !
	root_directory = conf.get("dirs", "root_dir")
	# This is a function attribute, hence i can access it from "outside"
	init_conf.cc_username = conf.get("auth", "username")
	init_conf.cc_password = conf.get("auth", "password")
	init_conf.cc_url = conf.get("auth", "url")
	
def init_driver():
	# TODO : change this if you have geckodriver in PATH !
    driver = webdriver.Firefox(executable_path=r'C:\Program Files\geckodriver-v0.19.1-win64\geckodriver.exe')
    driver.wait = WebDriverWait(driver, 5)
    return driver


 
def lookup(driver, username, password):
    driver.get(init_conf.cc_url)
    try:
		box_user = driver.wait.until(EC.presence_of_element_located(
			(By.NAME, "user")))
		box_pw = driver.wait.until(EC.presence_of_element_located(
			(By.NAME, "password")))
		button = driver.wait.until(EC.element_to_be_clickable(
			(By.NAME, "bt_LOGON")))
		box_user.send_keys(username)
		box_pw.send_keys(password)
		button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
	Debug = main(sys.argv[1:])
	driver = init_driver()
	init_conf()
	lookup(driver, init_conf.cc_username, init_conf.cc_password)
	time.sleep(2)
	textes = driver.find_elements_by_class_name('tabtext')
	# prints current balance
	print textes[1].text + textes[2].text
	#find logout button
	link_logout = driver.find_element_by_id("nav.logout")
	
	link_logout.click()
	time.sleep(1)
	driver.quit()

