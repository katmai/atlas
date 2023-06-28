import requests
from bs4 import BeautifulSoup

url = 'https://www.alltrails.com/explore/trail/czech-republic/south-moravian-region/brno-reservoir-trail'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

trail_info = soup.find_all('div', {'class': 'detail-data'})

with open('brno_reservoir_trail_info.txt', 'w') as f:
    for info in trail_info:
        f.write(info.text.strip() + '\n')
