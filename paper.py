from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.firefox.service import Service
import pandas as pd
import datetime
import os
import time
from sections import get_page

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.headless=True

website = "https://www.thehindu.com/todays-paper/"
path = r"./geckodriver.exe"

service = Service(executable_path=path)
driver = webdriver.Firefox(options=options, service=service)

driver.get(website)

events_values = ['TH_Regional', 'TH_National', 'TH_Edit', 'TH_Foreign', 'TH_Business', 'Sports']

dataframes=[]
for value in events_values:
	print(value)
	dataframes.append(get_page(value))

driver.quit()

result=pd.concat(dataframes)
result.to_csv('paper.csv')