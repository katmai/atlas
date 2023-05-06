import requests
from bs4 import BeautifulSoup


def scrape_rock_info(url: str) -> str:
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', {'class': 'wikitable sortable'})
            rows = table.find_all('tr')

            rock_info = []

            for row in rows:
                cells = row.find_all('td')
                if len(cells) > 0:
                    rock_name = cells[0].text.strip()
                    rock_type = cells[1].text.strip()
                    rock_info.append(f'{rock_name}: {rock_type}')

            return '\n'.join(rock_info)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return ''


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_rock_types'
    rock_info = scrape_rock_info(url)

    if rock_info:
        with open('rock_info.txt', 'w') as f:
            f.write(rock_info)
    else:
        print('Error: Could not retrieve webpage')