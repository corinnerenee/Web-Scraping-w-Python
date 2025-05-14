import requests
from bs4 import BeautifulSoup

quotes = []

page = requests.get('https://quotes.toscrape.com')

soup = BeautifulSoup(page.text, 'html.parser')

soup.find_all('div', class_ =  'quote')