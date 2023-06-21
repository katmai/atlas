import requests
from bs4 import BeautifulSoup

url = "https://www.alltrails.com/czech-republic"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="trailList")

trail_elems = results.find_all("div", class_="styles-module__trailCard___2qMHX")

for trail_elem in trail_elems:
    trail_name = trail_elem.find("h3", class_="styles-module__name___2HxOw").text.strip()
    trail_location = trail_elem.find("div", class_="styles-module__location___1J6DZ").text.strip()
    trail_difficulty = trail_elem.find("div", class_="styles-module__difficulty___3Dd0V").text.strip()
    trail_distance = trail_elem.find("div", class_="styles-module__distance___1W6P_").text.strip()
    trail_elevation_gain = trail_elem.find("div", class_="styles-module__elevationGain___1DlKj").text.strip()
    trail_rating = trail_elem.find("div", class_="styles-module__rating___1dPQF").text.strip()
    trail_reviews = trail_elem.find("div", class_="styles-module__reviews___1QG4a").text.strip()

    print(trail_name, trail_location, trail_difficulty, trail_distance, trail_elevation_gain, trail_rating, trail_reviews)
