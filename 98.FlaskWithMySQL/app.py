from flask import Flask , render_template, request, redirect
import db.kpop_dao as kd

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask with MySQL'

@app.route('/song/list')
def song_list():
    songs = kd.get_song_list(20)
    return render_template('01.song_list.html', songs=songs)

@app.route('/song/insert', methods=['GET', 'POST'])
def song_insert():
    if request.method == 'GET':
        return render_template('02.song_insert.html')
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        kd.insert_song((title, lyrics))
        return redirect('/song/list')

@app.route('/song/update/<sid>', methods=['GET', 'POST'])
def song_update():
    if request.method == 'GET':
        return render_template('03.song_update.html')
    else:
        pass

@app.route('/gg/list')
def gg_list():
    groups = kd.get_girl_group_list(20)
    return render_template('11.gg_list.html', groups=groups)

@app.route('/gg/insert', methods=['GET', 'POST'])
def gg_insert():
    if request.method == 'GET':
        return render_template('12.gg_insert.html')
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        kd.insert_song((title, lyrics))
        return redirect('/song/list')

if __name__ == '__main__': 
    app.run(debug=True) # 디버그를 트루로 둬서 서버가 코드바꾸고 저장하면 자동으로 재시작함 100로는 아님



