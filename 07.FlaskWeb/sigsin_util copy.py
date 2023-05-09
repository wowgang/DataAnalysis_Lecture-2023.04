import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup

def sigsinutil():

    base_url = 'https://www.siksinhot.com/search'
    url = f'{base_url}?keywords={quote("장안문")}'
    result = requests.get(url)
    html = result.text
    soup = BeautifulSoup(result.text, 'html.parser')
    lis = soup.find_all('li')
    lis = soup.select_one('.localFood_list').find_all('li')
    li = lis[0]
    img = li.find('img')['src']
    li.select_one('.textBox').get_text()
    title = li.select_one('.textBox > h2').get_text()
    score = li.select_one('.textBox > .score').get_text()
    atags = li.select('.cate > a')
    location = atags[0].get_text()
    menu = atags[1].get_text()

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
