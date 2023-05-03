from flask import Flask , render_template
import random

app = Flask(__name__)

@app.route('/') # decorator route를 '/'로
def index(): # 사용자가 어떤 path를 입력하지 않고 들어올때 retrun으로 응대해라
    return 'Hello Flask' # return은 문자열을 응답해야함

@app.route('/hello') # 사용자가 /hello로 입력했을때 return으로 응대
def hello():
    return render_template('01.hello.html')


# variable rules
@app.route('/read/<id>')
def read():
    return 'Read' + id  

if __name__ == '__main__': 
    app.run(debug=True) 
