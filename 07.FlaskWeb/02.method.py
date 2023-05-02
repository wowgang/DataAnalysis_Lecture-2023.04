from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

@app.route('/login', methods=['GET', 'POST']) # methods복수
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:   # method가 POST /post입력값을 값고 아이디,비번이 맞음그와맞는것으로 틀리면 그거와 맞는것으로 ...들어가는
        return '환영합니다.' # get이나 post나 동일한이름을 가져가는게 요즘 추세...? / 웹이서 확인을 누르니까 환영합니다가됨 url로도 서버에서도 메소드 처리가능 메소드로도 처리가능이라는데 무슨말인지

# method에 맞게 내가 원하는거를 가져갈수있다..


if __name__ == '__main__': 
    app.run(debug=True)



