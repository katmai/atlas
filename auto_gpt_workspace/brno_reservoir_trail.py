#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = 'https://www.alltrails.com/trail/czech-republic/south-moravian/stezka-brnenska-prehrada'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

trail_distance = soup.find('span', {'class': 'detail-data'}).text
trail_difficulty = soup.find('span', {'class': 'detail-data'}).find_next_sibling('span').text

print('Distance: ' + trail_distance)
print('Difficulty: ' + trail_difficulty)
