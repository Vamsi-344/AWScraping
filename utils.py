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
	path = r"C:\Users\sethu\Downloads\geckodriver-v0.32.0-win32\geckodriver.exe"

	service = Service(executable_path=path)
	driver = webdriver.Firefox(options=options, service=service)
	driver.get(website)

	content = driver.find_elements(by="xpath", value='//div[@id="content-body-"]/p')

	for num in content:
		p_content= p_content+num.text+'\n'

	driver.quit()

	return p_content

# print(get_content("https://www.thehindu.com/todays-paper/2022-12-05/th_chennai/articleGVDAJHKH1-1440237.ece"))