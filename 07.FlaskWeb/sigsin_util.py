import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def sigsinutil(places):

    base_url = 'https://www.siksinhot.com/search'
    url = f'{base_url}?keywords={quote(places)}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    lis = soup.select_one('.localFood_list').find_all('li')

    lines = []
    for li in lis: 
        img = li.find('img')['src']
        title = li.select_one('.textBox > h2').get_text()
        score = li.select_one('.textBox > .score').get_text()
        atags = li.select('.cate > a')
        location = atags[0].get_text()
        menu = atags[1].get_text()
        lines.append({'img':img, 'title':title, 'score':score, 'location':location, 'menu':menu})
    return lines
