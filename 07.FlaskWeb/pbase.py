from flask import Flask , render_template, request
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import melon_util as mu
import youtuberank_util as yr

app = Flask(__name__) 

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/base')
def base():
    return render_template('prototype/pbase.html')

@app.route('/melon')
def melon():
    melon_list = mu.melonutil()
    return render_template('prototype/melon.html', melon_list=melon_list)

@app.route('/youtube_ranking')
def youtuberank():
    youtube_list = yr.youtuberankutil()
    return render_template('prototype/youtuberank.html', youtube_list=youtube_list)

@app.route('/y20')
def y20():
    youtube_list = yr.youtuberankutil()
    return render_template('prototype/y20.html',youtube_list=youtube_list )

@app.route('/yc10')
def yc10():
    youtube_list = yr.youtuberankutil()
    a = pd.read_csv("static/카테고리10.csv", sep=",")
    dic=[]
    for i in range(10):
        dic.append(a.iloc[i][0])
        dic.append(a.iloc[i][1])
    names = dic[::2]
    values = dic[1::2]
    my_dict = {names[i]: values[i] for i in range(len(names))}
    return render_template('prototype/yc10.html',youtube_list=youtube_list, my_dict=my_dict, names=names,values=values )

if __name__ == '__main__': 
    app.run(debug=True)