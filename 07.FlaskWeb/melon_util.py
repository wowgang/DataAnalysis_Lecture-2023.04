import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
 
def melonutil():
    url = 'https://www.melon.com/chart/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url,headers=header)
    soup = BeautifulSoup(result.text,'html.parser')
    trs = soup.select('tr.lst50,tr.lst100')
    tr = trs[0]

    lines = []
    for tr in trs:
        rank = tr.select_one('.rank').get_text()
        title = tr.select_one('div.ellipsis.rank01 > span > a').get_text().strip()
        artist = tr.select_one('div.ellipsis.rank02 > a').get_text().strip()
        album = tr.select_one('.ellipsis.rank03 > a').get_text().strip()
        img = tr.select_one('.image_typeAll > img')['src']
        lines.append({ '순위': rank, '제목':title, '아티스트':artist, '앨범':album, '이미지':img})
    return lines 