import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
 

def convert(s):
    s = s.replace('억','').replace('개','').replace(',','').replace('만','0000')
    return int(s)

def youtuberankutil():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver', options=options)

    lines = []
    for page in range(1,11):
        url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=' + str(page)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        time.sleep(2)
        trs = soup.select('.aos-init')
        tr = trs[0]

        for tr in trs:
            rank =int(tr.select_one('.info_rank').get_text().strip())
            category=tr.select_one('.category').get_text().strip()[1:-1]
            title = tr.select_one('h1 > a').get_text().strip()
            subscriber = convert(tr.select_one('.subscriber_cnt').get_text().strip())
            view = convert(tr.select_one('.view_cnt').get_text().strip())
            video = convert(tr.select_one('.video_cnt').get_text().strip())
            lines.append({'순위':rank,'카테고리':category,'채널명':title,'구독자수':subscriber,
                        '조회수':view,'비디오':video})
    driver.close()
    return lines