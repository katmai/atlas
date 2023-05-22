# Import necessary libraries
import openai
import requests
import json
import base64
from PIL import Image

# Set up API key
openai.api_key = "YOUR_API_KEY"

# Define function to generate image from text prompt

def generate_image(prompt):
    response = openai.Completion.create(
        engine="image-alpha-001",
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.5,
    )
    image_data = response.choices[0].text
    image_data = image_data.replace("data:image/png;base64,", "")
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    return image
