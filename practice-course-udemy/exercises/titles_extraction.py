import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "html.parser")

links = soup.find_all('a')
links = links[0:25]

# Extracting all the links
clean_urls = [l for l in links if l.get('href') != None]
titles = [t.get('title') for t in clean_urls if t.get('title') != None]
print(titles)
