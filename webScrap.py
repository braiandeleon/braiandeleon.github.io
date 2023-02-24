import requests
from bs4 import BeautifulSoup

url = 'shopExample.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('li')
for product in products:
    image = product.find('img')['src']
    name = product.find('h3').text
    price = product.find('p').text
    print('Name:', name)
    print('Price:', price)
    print('Image:', image)
