import requests
from bs4 import BeautifulSoup
import pandas as pd

base_site = "https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"

response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, "lxml")

with open('rotton_tomatoes_response.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

divs = soup.find_all('div', {'class': 'article_movie_title'})
headings = [div.find('h2') for div in divs]

movie_names = [heading.find('a').string for heading in headings]
movie_years = [int(year.find('span').string.strip('()')) for year in headings]
movie_score = [score.find('span', class_ = 'tMeterScore').string for score in headings]

common_phrase = "Critics Consensus: "
common_len = len(common_phrase)
consensus = soup.find_all('div', {'class': 'info critics-consensus'})
consensus_text = [con.text[common_len:] if con.text.startswith(common_phrase) else con.text for con in consensus ]

directors = soup.find_all("div", class_ = "info director")
directors_text = [director.text.strip("\nDirected By: ") for director in directors if director != None]

cast_info = soup.find_all("div", class_ = "info cast")

cast = [", ".join([link.string for link in c.find_all("a")]) for c in cast_info]

synopsis = soup.find_all('div', {'class': 'info synopsis'})
# Extracting the text
synopsis_text = [syn.contents[1] for syn in synopsis]

movies_info = pd.DataFrame()

movies_info['Movie Title'] = movie_names
movies_info['Year'] = movie_years
movies_info["Score"] = movie_score
movies_info["Director"] = directors_text
movies_info['Synopsis'] = synopsis_text
movies_info['Cast'] = cast
movies_info['Consensus'] = consensus_text

# Export to CSV and Excel
movies_info.to_csv("movies_info.csv", index = False, header = True)
movies_info.to_excel("movies_info.xlsx", index = False, header = True)

