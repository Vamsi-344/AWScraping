from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import pandas as pd
import datetime
import os
import time
from selenium.webdriver.firefox.options import Options


options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.preferences.update({'javascript.enabled': False})
options.headless=True

def get_content(website):
	p_content = ""
	path = r"./geckodriver.exe"

	service = Service(executable_path=path)
	driver = webdriver.Firefox(options=options, service=service)
	driver.get(website)

	content = driver.find_elements(by="xpath", value='//div[@id="content-body-"]/p')

	for num in content:
		p_content= p_content+num.text+'\n'

	driver.quit()

	return p_content