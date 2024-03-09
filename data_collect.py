import requests
from bs4 import BeautifulSoup

base_url = "https://finance.yahoo.com/quote/XOM/history"
query_string = (
    "?period1=1520553600"
    "&period2=1709942400"
    "&interval=1d"
    "&filter=history"
    "&frequency=1d"
    "&includeAdjustedClose=true"
)
URL = base_url + query_string
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

stocks_info = []