import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "lxml")

div_notes = soup.find_all('div', {'role':'note'})
div_links = []

for div in div_notes:
    anchors = div.find_all('a')
    div_links.extend(anchors)

div_urls = [urljoin(base_site, l.get('href')) for l in div_links]
print(div_urls)