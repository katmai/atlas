import requests
from PIL import Image
from io import BytesIO

def generate_river_image(prompt):
    url = 'https://api.unsplash.com/search/photos?query=' + prompt + '&client_id=YOUR_ACCESS_KEY'
    response = requests.get(url)
    image_url = response.json()['results'][0]['urls']['regular']
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()
