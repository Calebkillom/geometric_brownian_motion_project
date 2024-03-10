from bs4 import BeautifulSoup
import requests

base_url = "https://www.marketwatch.com/investing/stock/xom/options"
query_string = (
    "?mod=mw_quote_tab"
)

URL = base_url + query_string

req = requests.get(URL)

soup = BeautifulSoup(req.content, "html.parser")

print(soup.title)