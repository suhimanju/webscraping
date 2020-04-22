import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_site = "https://www.espncricinfo.com/series/19832/commentary/1220949/royal-challengers-bangalore-vs-kolkata-knight-riders-1st-match-n-indian-premier-league-retrolive-2019-20?innings=2&filter=full"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "html.parser")

match_commentary_content = soup.find('div', {'class':'match-commentary__content'})

commentary_string = match_commentary_content.text
print(commentary_string)