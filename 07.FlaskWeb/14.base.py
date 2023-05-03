import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask , render_template, request
import map_util as mu # 내가 만든 파일import한거
import interpark_util as inter


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/base')
def base():
    return render_template('14.base.html')

# Home carousel
@app.route('/carousel')
def carousel():
    return render_template('13.carousel.html')

# 산점도
@app.route('/scatter', methods=['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('09.산점도.html')
    else:
        num = int(request.form['num'])
        mean = float(request.form['mean'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        xs = np.random.normal(loc=mean, scale=std, size=num)
        ys = np.random.uniform(min, max, num)
        plt.figure()
        plt.scatter(xs, ys)
        filename = os.path.join(app.static_folder, 'img/scatter.png') 
        plt.savefig(filename)
        return render_template('09.산점도_res.html')
    

# HotPlace
@app.route('/hotPlaces', methods=['GET', 'POST'])
def hotPlaces():
    if request.method == 'GET': # parameter읽기
        return render_template('10.HotPlaces.html')
    else:
        # client가 입력한 장소 알아내기
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        
        # 우리가만든 함수 모듈로 불러온것
        mu.hot_places(places, app) 
        return render_template('10.HotPlaces_res.html') # 지도여기에 보여줘라
    
# Interpark
@app.route('/interpark')
def interpark():
    book_list = inter.interparkutil() 
    return render_template('11.interpark.html', book_list=book_list)


# Progress Bar
@app.route('/progress')
def progress():
    return render_template('13.progressbar.html')



if __name__ == '__main__': 
    app.run(debug=True)

