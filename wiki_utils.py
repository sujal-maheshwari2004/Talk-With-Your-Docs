import wikipedia
import requests
from bs4 import BeautifulSoup

wikipedia.set_user_agent('MyApp/1.0')

def search_wikipedia(query: str) -> str:
    try:
        results = wikipedia.search(query)
        if results:
            page = wikipedia.page(results[0])
            return page.url
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
        pass
    return None

def scrape_wikipedia_page(url: str) -> dict:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', {'id': 'firstHeading'}).text
        content = soup.find('div', {'id': 'mw-content-text'})
        if content:
            paragraphs = content.find_all('p')
            page_content = '\n'.join([para.text for para in paragraphs])
            return {'title': title, 'content': page_content}
    return None
