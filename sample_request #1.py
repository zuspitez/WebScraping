import requests
# from bs4 import BeautifulSoup
# import pandas as pd

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print(page.status_code)
print(page.content)