import requests
from bs4 import BeautifulSoup
# import pandas as pd

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print("#1 ", soup.find_all('p')) # all instances #
print("#2 ", soup.find_all('p')[0]) 
print("#3 ", soup.find_all('p')[1].get_text())
print("#4 ", soup.find('p')) # just one instance #
print("#5 ", soup.find('p').get_text()) # just one instance #
print("#6 ", soup.find_all('p', class_='outer-text'))
print("#7 ", soup.find_all(class_='outer-text'))
print("#8 ", soup.find_all(id="first"))