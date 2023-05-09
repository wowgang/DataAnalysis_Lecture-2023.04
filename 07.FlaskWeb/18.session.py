# 15 복사함
import os, random, json
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask , render_template, request, redirect, session, flash
import map_util as mu # 내가 만든 파일import한거
import interpark_util as inter
import sigsin_util as sigsin
import genie_util as genie
from weather_util import get_weather, get_weather_by_coord
import image_util as iu
from user import user_bp
# from user_module.user import user_bp

app = Flask(__name__)
app.secret_key = 'qwert12345'   # session은 밖에서보면 암호화
app.config['SESSION_COOKIE_PATH'] = '/'

app.register_blueprint(user_bp, url_prefix='/user')

# 구버전
@app.before_first_request
def before_first_request():
    global quote,quotes  # quotes 함수 밖에서도 사용가능변수가됨 / 전역변수
    global addr
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as f:
        quotes = f.readlines()
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    addr = '수원시 장안구'
    session['addr'] = addr



# flask 2.3에서는 이 코드만 사용 가능
# 최초의 요청을 받기전에 실행
# with app.app_context():
#     global quote,quotes  # quotes 함수 밖에서도 사용가능변수가됨 / 전역변수
#     global addr
#     filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
#     with open(filename, encoding='utf-8') as f:
#         quotes = f.readlines()
#     quote = random.sample(quotes, 1)[0]
#     session['quote'] = quote
#     addr = '수원시 장안구'

# for AJAX
@app.route('/change_quote')
def change_quote():
    global quote
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    return quote

@app.route('/change_addr')
def change_addr():
    global addr 
    addr = request.args.get('addr')
    session['addr'] = addr
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

# redirect -> url로 가라
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
    return render_template('prototype/naso.html', menu=menu, weather=get_weather(app),
                           quote=quote, addr=addr)

# Interpark
@app.route('/interpark')
def interpark():
    book_list = inter.interparkutil() 
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/interpark.html', book_list=book_list, menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)

@app.route('/geniechart')
def geniechart():
    genie_list = genie.genieutil() 
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/geniechart.html', genie_list=genie_list, menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)

@app.route('/genie_jquery')
def genie_jquery():
    genie_list = genie.genieutil() 
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/user/genie_jquery.html', genie_list=genie_list, menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)


@app.route('/sigsin',methods=['GET', 'POST'])
def sig():
    if request.method == 'GET':
        menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
        return render_template('prototype/sigsin.html', menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)
    else:
        menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
        place = request.form['places']
        sigsin_list = sigsin.sigsinutil(place)
        return render_template('prototype/sigsin.html', sigsin_list=sigsin_list, menu=menu, 
                           weather=get_weather(app),quote=quote, addr=addr)


@app.route('/hotPlaces', methods=['GET', 'POST'])
def hotPlaces():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    if request.method == 'GET': # parameter읽기
        return render_template('prototype/hotPlaces.html',menu=menu, weather=get_weather(app),quote=quote, addr=addr)
    else:
        # client가 입력한 장소 알아내기
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        
        # 우리가만든 함수 모듈로 불러온것
        mu.hot_places(places, app) # 지도여기에 보여줘라
        return render_template('prototype/hotPlaces_res.html', menu=menu, 
                               weather=get_weather(app),quote=quote, addr=addr) 
    
    
    
@app.route('/schedule')
def schedule():
    try:
        _ = session['uid']
    except:
        flash('스케줄을 확인하려면 로그인하여야 합니다.')
        return redirect('/user/login')
    
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('prototype/schedule.html',  menu=menu, weather=get_weather(app),
                           quote=quote, addr=addr)





if __name__ == '__main__': 
    app.run(debug=True)

