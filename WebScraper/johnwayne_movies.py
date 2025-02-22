import requests
from bs4 import BeautifulSoup

url = "https://editorial.rottentomatoes.com/guide/all-clint-eastwood-movies-ranked/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'
}


url_response = requests.get(url, headers=headers)

webpage_soup = BeautifulSoup(url_response.content, 'html.parser')

h2_elements = webpage_soup.find_all('h2')

count = 1
for h2 in h2_elements:
    a_elements = h2.find_all('a')
    for a in a_elements:
        if len(str(count)) == 1:
            count_str = f"0{count}"
        else:
            count_str = str(count)
        print(f"[] {count_str} - {a.text}")
    count += 1
    
    # if not title[1].isdigit():
    #     title = f'0{title}'
    # title = title.replace('.', ' -')
    # title = f'[] {title}'
    # print(title)
    