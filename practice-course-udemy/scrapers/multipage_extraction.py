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

par_text = []
i = 1
for url in div_urls:
    par_resp = requests.get(url)

    if par_resp.status_code == 200:
        print("URL #{0}: {1}".format(i+1,url))
    else:
        print("Status code {0}: Skipping URL #{1}: {2}".format(par_resp.status_code, i+1, url))
        i+=1
        continue
    par_html = par_resp.content
    par_soup = BeautifulSoup(par_html, 'lxml')
    pars = par_soup.find_all("p")
    text = [p.text for p in pars]
    par_text.append(text)
    i+=1

page_text = ["".join(text) for text in par_text]

url_to_text = dict(zip(div_urls, page_text))
