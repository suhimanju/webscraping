import requests
from bs4 import BeautifulSoup

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "html.parser")

# Searching by attributes
soup.find('div', id= 'siteSub')

# Extracting data form the HTML tree

# Example1 - Here class_ has been used since class is a builtin keyword
tag = soup.find('a', class_= 'mw-jump-link')
print(tag.name)
print("\n")
# Getting/Accessing the attribute value 

# Example-1
print(tag['class'])
print("\n")

# Example-2 - Recommended way to use as program is not interrupted
print(tag.get('class'))
print("\n")

# repr() function should the official string representation of an object
repr(tag.get('id'))
print("\n")

# Get all attributes of the tag into a dictionary
print(tag.attrs)
print("\n")

# Extracting the text (.string vs .text)
print(tag.string)
print(tag.text)

# Example - this is where .text plays vital role
paragraph = soup.find_all('p')[1]
print(paragraph)

print(paragraph.parent.text)
print("\n")

# prints all the texts in the html document 
# But BeautifulSoup doesn't interpret javascript 
print(soup.text)

## .stripped_strings generator:
for s in paragraph.stripped_strings:
    print(repr(s))