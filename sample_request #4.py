# using CSS Selectors #

import requests
from bs4 import BeautifulSoup
# import pandas as pd

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print("#1 ", soup.select("div p"))
