import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls058639981/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'
}


url_response = requests.get(url, headers=headers)

webpage_soup = BeautifulSoup(url_response.content, 'html.parser')

elements = webpage_soup.find_all(class_='ipc-title__text')

for element in elements:
    title = str(element.text)
    
    if not title[1].isdigit():
        title = f'0{title}'
    title = title.replace('.', ' -')
    title = f'[] {title}'
    print(title)
    