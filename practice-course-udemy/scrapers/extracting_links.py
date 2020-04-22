import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "html.parser")

links = soup.find_all('a')
print(links)
print("\n")

link = links[26]
print(link)
print("\n")

print(link.string)
print("\n")

relative_url = link['href']

full_url = urljoin(base_site, relative_url)
print(full_url)

# Extracting all the links
clean_urls = [l for l in links if l.get('href') != None]
relative_urls = [l.get('href') for l in clean_urls]
print(relative_urls)

full_urls = [urljoin(base_site,url) for url in relative_urls if 'wikipedia.org' not in url]
print(full_urls)
print("\n")

internal_links = [url for url in full_urls if 'wikipedia.org' in url]
print(internal_links)