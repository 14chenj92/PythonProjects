import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

if __name__ == "__main__":
    url = 'http://example.com'
    data = scrape_website(url)
    print(data)
