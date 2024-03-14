import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver

# Inspired from here: https://realpython.com/beautiful-soup-web-scraper-python/
URL = "https://mec.aamc.org/msar-ui/#/landing"

driver = webdriver.Chrome()


page = driver.get(URL)
print(page)

# page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="content-container")
print(results)

# cards = soup.find_all("mat-card", class_="mat-mdc-card mdc-card ng-star-inserted")
# print(cards)

