# Парсинг сайта auto.ria.com с помощью BeautifulSoup:

from bs4 import BeautifulSoup
import requests

URL = 'https://auto.ria.com/newauto/marka-opel/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
HOST = 'https://auto.ria.com'

r = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(r.text, 'html.parser')

name = soup.find('div', class_='proposition_title').text
cena = soup.find('div', class_='proposition_price').text
url = soup.find('a').get('href')

print(name.strip())
print(cena.strip())
print(url)
