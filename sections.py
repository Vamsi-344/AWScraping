from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.firefox.service import Service
import pandas as pd
import datetime
import os
import time
from article_content import get_content

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.headless=True

def get_page(page_value):
	website = "https://www.thehindu.com/todays-paper/"
	path = r"./geckodriver.exe"

	service = Service(executable_path=path)
	driver = webdriver.Firefox(options=options, service=service)

	driver.get(website)

	page_nums = []
	titles = []
	sub_texts = []
	links = []
	contents = []

	driver.execute_script(f"changeLayoutDesk(this, '"+page_value+"')")
	button = driver.find_element(by="xpath", value='//a[@id="show-hide-stories"]')
	driver.execute_script("arguments[0].click();", button)

	remaining_stories = driver.find_elements(by="xpath", value='//div[@class="page-num"]//following-sibling::div[@class="title"]/a | //div[@style="display: block;"]//div[@class="title"]/a')
	for i in remaining_stories:
		titles.append(i.text)
		links.append(i.get_attribute("href"))

	num_ele = driver.find_elements(by="xpath", value='//div[@class="page-num"]')
	subtxt_ele = driver.find_elements(by="xpath", value='//div[@class="sub-text"]')

	for num in num_ele:
		page_nums.append(num.text)
	for subtxt in subtxt_ele:
		sub_texts.append(subtxt.text)
	for link in links:
		lol = get_content(link)
		contents.append(lol)

	news_dic = {'Page Num': page_nums ,'Title':titles, 'Sub Text': sub_texts, 'Links': links, 'Contents': contents}
	df = pd.DataFrame(news_dic)
	driver.quit()

	return df