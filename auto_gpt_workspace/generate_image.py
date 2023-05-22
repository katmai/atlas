# Import the necessary libraries
import openai
import requests
import json

# Set up the OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# Set up the prompt and parameters
prompt = "Generate an image of a cat"
params = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1,
    "size": 512,
    "response_format": "url"
}

# Call the OpenAI API to generate the image
response = openai.Completion.create(**params)

# Get the URL of the generated image
url = response.choices[0].text

# Download the image
image_data = requests.get(url).content

# Save the image to a file
with open("output.png", "wb") as f:
    f.write(image_data)