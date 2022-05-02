# encoding=utf8  

#from importlib import reload
import sys, getopt

#reload(sys)  
#sys.setdefaultencoding('utf8')

import re
import ssl
import os
import os.path
import configparser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


# cc.py -d 1/True turns Debug mode on. 
# You can turn this on, to turn on the "file found:" comment, just to check


def main(argv):
	Debug = False
	try:
		opts, args = getopt.getopt(argv,"d:",["dbgpara="])
	except getopt.GetoptError:
		Debug = False
		return Debug
	finally:	
		for opt, arg in opts:
			if opt in ("-d","--dbgpara"):
				if (arg == 'True') or (arg == '1'):
					Debug = True
		return Debug
 
def init_conf():
	conf = configparser.ConfigParser()
	project_dir = os.path.dirname(os.path.abspath(__file__))
	conf.read(os.path.join(project_dir, 'config.ini'))
	
	# Read config Settings - Do not change URLs if no necessary !
	# This is a function attribute, hence i can access it from "outside"
	init_conf.cc_username = conf.get("auth", "username")
	init_conf.cc_password = conf.get("auth", "password")
	init_conf.cc_url = conf.get("auth", "url")
	
def init_driver():
	# TODO : change this if you have geckodriver in PATH ! (Windows version)
    #driver = webdriver.Firefox(executable_path=r'C:\Program Files\geckodriver-v0.19.1-win64\geckodriver.exe')
    #Raspbian Version (Stretch) - chromedriver needed!!
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    #init user-folder for cookies
    chrome_options.add_argument("user-data-dir=selenium")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.wait = WebDriverWait(driver, 5)
    return driver


 
def lookup(driver, username, password):
	driver.get(init_conf.cc_url)
	time.sleep(5)
	try:
		box_user = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
		box_pw = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")
		button = driver.find_element(By.XPATH, "//*[@class='login-container']/form/div[2]/button")
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
	time.sleep(5)
	
	checkString = driver.find_elements(By.XPATH,"//*[@class='dialplate-wheel__content__explainer ng-star-inserted']")[1].text
	if(str.find(checkString,"Verbraucht") != -1):
		textes = driver.find_elements(By.XPATH,"//*[@class='dialplate-wheel__content__small-number ng-star-inserted']")[0].text
		textes = textes.replace("€","")
		myvalue = textes.replace(".","")
		myvalue = myvalue.replace(",",".")
	else:
		textes = driver.find_element(By.XPATH,"//*[@class='dialplate-wheel__content__small-number ng-star-inserted']").text
		textes = textes.replace("€","")
		myvalue = textes.replace(".","")
		myvalue = "-" + myvalue.replace(",",".")
	
	myBalanceInfo = 'Amazon:\t\n' + "CCard: " + myvalue + " EUR"
	print(myBalanceInfo)
	time.sleep(2)
	driver.get("https://amazon.lbb.de/security/logout")
	time.sleep(1)
	driver.quit()

