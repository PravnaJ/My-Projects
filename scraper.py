import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        main_title = soup.find('h1').text.strip() if soup.find('h1') else 'No title found'
        main_paragraph = soup.find('p').text.strip() if soup.find('p') else 'No paragraph found'
        return {
            'title': main_title,
            'paragraph': main_paragraph
        }
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return None