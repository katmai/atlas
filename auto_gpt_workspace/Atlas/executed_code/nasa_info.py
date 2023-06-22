import requests
from bs4 import BeautifulSoup

url = 'https://www.nasa.gov/directorates/spacetech/niac/NIAC_funded_studies.html'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for h3 in soup.find_all('h3', {'class': 'title'}):
    print(h3.text)
