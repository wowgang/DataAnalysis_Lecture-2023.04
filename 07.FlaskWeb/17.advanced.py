# 15 복사함
import os, random
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask , render_template, request,redirect
import map_util as mu # 내가 만든 파일import한거
import interpark_util as inter
import sigsin_util as sigsin
import genie_util as genie
from weather_util import get_weather, get_weather_by_coord
import image_util as iu

app = Flask(__name__)
# # 구버전
# @app.before_first_request
# def before_first_request():
#     global quote,quotes  # quotes 함수 밖에서도 사용가능변수가됨 / 전역변수
#     global addr
#     filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
#     with open(filename, encoding='utf-8') as f:
#         quotes = f.readlines()
#     quote = random.sample(quotes, 1)[0]
#     addr = '수원시 장안구'


# flask 2.3에서는 이 코드만 사용 가능
# 최초의 요청을 받기전에 실행
with app.app_context():
    global quote,quotes  # quotes 함수 밖에서도 사용가능변수가됨 / 전역변수
    global addr
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as f:
        quotes = f.readlines()
    quote = random.sample(quotes, 1)[0]
    addr = '수원시 장안구'

# for AJAX
@app.route('/change_quote')
def change_quote():
    global quote
    quote = random.sample(quotes, 1)[0]
    return quote

@app.route('/change_addr')
def change_addr():
    global addr 
    addr = request.args.get('addr')
    return addr

@app.route('/weather')
def weather():
    addr = request.args.get('addr')
    lat, lng = mu.get_coord(addr + '청')
    html = get_weather_by_coord(app, lat, lng)
    return html

@app.route('/change_profile', methods=['POST'])
def change_profile():
    file_image = request.files['image']
    filename = os.path.join(app.static_folder, f'upload/{file_image.filename}')
    file_image.save(filename)
    mtime = iu.change_profile(app, filename)
    return str(mtime)
#####################

@app.route('/user')
def user():
    menu = {'ho':0, 'us':1, 'cr':0, 'sc':0}
    return redirect('/schedule')


@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('prototype/home.html' , menu=menu, weather=get_weather(app), 
                           quote=quote, addr=addr)

@app.route('/naso')
def naso():
    menu = {'ho':0, 'us':1, 'cr':0, 'sc':0}
    return render_template('prototype/naso.html',  menu=menu, weather=get_weather(app),
                           quote=quote, addr=addr)

# Interpark
@app.route('/interpark')
def interpark():
    book_list = inter.interparkutil() 
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/interpark.html', book_list=book_list,  menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)

@app.route('/geniechart')
def geniechart():
    genie_list = genie.genieutil() 
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/geniechart.html', genie_list=genie_list,  menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)

@app.route('/sigsin')
def sig():
    sigsin_list = sigsin.sigsinutil()
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/sigsin.html', sigsin_list=sigsin_list,  menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('prototype/schedule.html',  menu=menu, weather=get_weather(app),
                           quote=quote, addr=addr)





if __name__ == '__main__': 
    app.run(debug=True)

