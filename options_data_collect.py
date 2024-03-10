#!/usr/bin/python3
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

base_url = "https://www.marketwatch.com/investing/stock/xom/options"
query_string = (
    "?mod=mw_quote_tab"
)


URL = base_url + query_string

driver = webdriver.Firefox()
driver.get(URL)
driver.implicitly_wait(10)
driver.implicitly_wait(10)

page_content = driver.page_source
driver.quit()

page = requests.get(URL)

if page.status_code == 200:
    print("Page content successfully fetched.")
else:
    print("Failed to fetch page content. Status code:", page.status_code)
    exit()

soup = BeautifulSoup(page_content, "html.parser")

""" Find all table bodies with class "table__body" """
table_bodies = soup.find_all("tbody", class_="table__body")

for table_body in table_bodies:
    print(table_body)