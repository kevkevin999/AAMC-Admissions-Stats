import requests
from bs4 import BeautifulSoup
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inspired from here: https://realpython.com/beautiful-soup-web-scraper-python/
URL = "https://mec.aamc.org/msar-ui/#/landing"

driver = webdriver.Chrome()

driver.get(URL)
# html = driver.page_source
time.sleep(2)
# print(html)


# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")
results = driver.find_elements(by=By.CLASS_NAME, value="content-container")
print(results[0].text)

# cards = soup.find_all("mat-card", class_="mat-mdc-card mdc-card ng-star-inserted")
# print(cards)

driver.quit()