import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask , render_template, request
import map_util as mu # 내가 만든 파일import한거
import interpark_util as inter
import sigsin_util as sigsin
import genie_util as genie
from weather_util import get_weather


app = Flask(__name__)


@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('prototype/home.html' , menu=menu, weather=get_weather(app))

@app.route('/naso')
def naso():
    menu = {'ho':0, 'us':1, 'cr':0, 'sc':0}
    return render_template('prototype/naso.html',  menu=menu, weather=get_weather(app))

# Interpark
@app.route('/interpark')
def interpark():
    book_list = inter.interparkutil() 
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/interpark.html', book_list=book_list,  menu=menu, weather=get_weather(app))

@app.route('/geniechart')
def geniechart():
    genie_list = genie.genieutil() 
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/geniechart.html', genie_list=genie_list,  menu=menu, weather=get_weather(app))

@app.route('/sigsin')
def sig():
    sigsin_list = sigsin.sigsinutil()
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/sigsin.html', sigsin_list=sigsin_list,  menu=menu, weather=get_weather(app))

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('prototype/schedule.html',  menu=menu, weather=get_weather(app))





if __name__ == '__main__': 
    app.run(debug=True)

