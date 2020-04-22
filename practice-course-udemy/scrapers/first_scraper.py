import requests
from bs4 import BeautifulSoup

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "html.parser")

with open('Wiki_response.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

