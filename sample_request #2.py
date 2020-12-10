import requests
from bs4 import BeautifulSoup
# import pandas as pd

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print("#1 ", soup.find_all('p')) # all instances #
print("#2 ", soup.find_all('p')[0]) 
print("#3 ", soup.find_all('p')[0].get_text())
print("#4 ", soup.find('p')) # just one instance #
print("#5 ", soup.find('p').get_text()) # just one instance #