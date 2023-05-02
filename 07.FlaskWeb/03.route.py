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

# 사용자가 localhost:5000/user/admin 라고 주소창에 입력
# 내가 보낸 parameter를 서버로 보낼수있게 해준다는것
@app.route('/user/<uid>') # http://localhost:5000/user/garam
def user(uid):
    return f'<h1>{uid}</h1>'

@app.route('/int/<int:number>') # http://localhost:5000/int/256
def int_fn(number):
    return f'<h1>{number}</h1>'

@app.route('/float/<float:pi>') # http://localhost:5000/float/3.14159
def float_fn(pi):
    return f'<h1>{pi}</h1>'

# 사용자가 localhost:5000/add/4/and/5 라고 주소창에 입력
# 주소영역안에 parameter패싱해주는 방법 ?는 구닥다리
@app.route('/add/<int:a>/and/<int:b>')
def add(a, b):
    return f'<h1>{a} + {b} = {a+b} </h1>'

if __name__ == '__main__': 
    app.run(debug=True) # 디버그를 트루로 둬서 서버가 코드바꾸고 저장하면 자동으로 재시작함 100로는 아님



