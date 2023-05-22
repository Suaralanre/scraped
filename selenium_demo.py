#! usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://inventwithpython.com')

# try:
#     elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
#     print(f'Found {elem.tag_name} element with that class name!' )

# except:
#     print('Could not find element with that class name!')

linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')

linkElem.click()