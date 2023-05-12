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
    with open('static/유튜브탑20.csv', encoding='utf-8') as file:
       top20 = file.read()
    pd.DataFrame(top20).to_html()
    return render_template('prototype/y20.html',youtube_list=youtube_list )


if __name__ == '__main__': 
    app.run(debug=True)