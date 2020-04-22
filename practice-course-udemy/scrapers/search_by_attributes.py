import requests
from bs4 import BeautifulSoup

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "html.parser")

# Searching by attributes
print(soup.find('div', id= 'siteSub'))
print("\n")

# Passing attributes as function parmeters

# Example1 - Here class_ has been used since class is a builtin keyword
print(soup.find_all('a', class_= 'mw-jump-link'))
print("\n")

# Example2 - Further refining
print(soup.find('a', class_= 'mw-jump-link', href = '#p-search'))
print("\n")

# Placing the attributes in a dictionary:
# Example-1:
print(soup.find('a', attrs={ 'class':'mw-jump-link', 'href': '#p-search'}))
print("\n")

# Example-2:
print(soup.find('div', {'id': 'footer'}))
print("\n")
