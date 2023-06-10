import requests

url = 'https://example.com'
response = requests.get(url)
data = response.text

# Process the data
print(data[:100])