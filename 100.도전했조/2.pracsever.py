import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask , render_template, request
import likebase_copy as lc

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/first', methods=['GET', 'POST'])
def first():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        artist = request.form['artist']
        title = request.form['title']

        songs = lc.search_songs(title, artist, app)

        return render_template('result.html', songs=songs)
@app.route()

if __name__ == '__main__': 
    app.run(debug=True)