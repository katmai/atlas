import requests
from bs4 import BeautifulSoup

def get_text_summary(url, question):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    sentences = text.split('. ')
    for sentence in sentences:
        if question in sentence:
            return sentence
    return ''
