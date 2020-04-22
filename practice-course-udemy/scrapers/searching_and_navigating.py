import requests
from bs4 import BeautifulSoup

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "html.parser")

# find method in BeautifulSoup
# find returns 'None' if no element found
head = soup.find('head')
print(head)
print("\n")

# find_all method in BeautifulSoup 
# find_all returns empty list if no element found
links = soup.find_all('a')
print(isinstance(links, list))
print("\n")

## table tag

table = soup.find('tbody')
td = table.find_all('td')
print(td)
print("\n")

## Navigating the tree
print(table.contents)
print("\n")

## Searching by attributes
print(table.parent)
print("\n")
