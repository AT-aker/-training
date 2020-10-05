import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
html_datd = BeautifulSoup(response.text)
	