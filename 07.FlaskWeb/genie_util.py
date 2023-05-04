import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def genieutil():

    url = 'https://www.genie.co.kr/chart/top200'
    result = requests.get(url)
    header = {'User-Agent': 'Mozilla/5.0'}
    result = requests.get(url, headers=header) # header 내가 로봇이 아니라는걸...말해주는?
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    tr = trs[0]
    rank = tr.select_one('.number').get_text().split('\n')[0].strip()
    img = 'https:' + tr.select_one('.cover > img')['src']
    try:
        title = tr.select_one('.title.ellipsis').get_text().strip() #19금아닌것
    except:
        title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip() # 19금

    artist = tr.select_one('.artist.ellipsis').string.strip() 
    album = tr.select_one('.albumtitle.ellipsis').text.strip()

    now = datetime.now()
    ymd = now.strftime('%Y%m%d')
    hh = now.strftime('%H')

    lines = []
    base_url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y'
    for page in range(1, 5): # 진척률 4페이지 반복
        url = f'{base_url}&ymd={ymd}&hh={hh}&pg={page}'
        result = requests.get(url, headers=header) # header 내가 로봇이 아니라는걸...말해주는?
        soup = BeautifulSoup(result.text, 'html.parser')
        trs = soup.select('tr.list')
        for tr in trs:
            rank = tr.select_one('.number').get_text().split('\n')[0].strip()
            img = 'https:' + tr.select_one('.cover > img')['src']
            try:
                title = tr.select_one('.title.ellipsis').get_text().strip() #19금아닌것
            except:
                title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip() # 19금
            artist = tr.select_one('.artist.ellipsis').string.strip()
            album = tr.select_one('.albumtitle.ellipsis').text.strip() 
            lines.append({'rank':rank, 'img':img, 'title':title, 'artist':artist, 'album':album})
    return lines