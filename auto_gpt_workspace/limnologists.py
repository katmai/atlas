import requests
from bs4 import BeautifulSoup

def analyze_code(code: str) -> list[str]:
    # Send a request to the URL and get the response
    url = 'https://www.nationalgeographic.org/encyclopedia/river/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the section of the page with information on limnology
        limnology_section = soup.find('section', {'id': 'limnology'})

        # Find all the paragraphs with information on the role of limnologists
        limnologists_paragraphs = limnology_section.find_all('p', text='Limnologists')

        if not limnologists_paragraphs:
            raise Exception('Unable to find information on the role of limnologists.')

        # Extract the text from each paragraph
        limnologists_text = [p.text for p in limnologists_paragraphs]

        # Return the list of extracted text
        return limnologists_text

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except Exception as e:
        raise SystemExit(e)