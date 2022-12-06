# AWScraping

**Implementation of web scraping The Hindu Newspaper**
	By Using Selenium, Firefox, and geckodriver in python.

**Files and their respective actions**
	`paper.py` - main file to run our web scrapping
	`sections.py` - to extract a particular section's content
	`article_content.py` - to extract each article's content present in a section

## How to run the code
	python3 -u paper.py

## Tinkering
1. Important things to remember are that the `geckodriver.exe` file should be present inside the same folder this particular github repo has been extracted to, if not please change the value of `path` variable in every .py file accordingly.
2. After running the scripts paper content will be saved in `paper.csv` file in the same folder.  