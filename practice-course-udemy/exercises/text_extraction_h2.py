import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "lxml")

headings = soup.find_all('h2')
print(headings)
print("\n")
heading_text = [a.text for a in headings if a.text != None]
print(heading_text)