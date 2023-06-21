import os
os.system("pip install requests beautifulsoup4")
import requests
from bs4 import BeautifulSoup

url = "https://www.alltrails.com/trail/czech-republic/south-moravian/stezka-brnenska-prehrada"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

info = soup.find_all("div", {"class": "text-body"})

distance = ""
elevation_gain = ""

for i in info:
    if "Distance" in i.get_text():
        distance = i.get_text()
    elif "Elevation Gain" in i.get_text():
        elevation_gain = i.get_text()

print(distance)
print(elevation_gain)
