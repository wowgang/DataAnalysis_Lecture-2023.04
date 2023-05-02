from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

# localhost:5000/area?pi=3.14&radius=5
@app.route('/area') # 아무런 얘기가 없으면 GET 방식
def area():
    pi = request.args.get('pi', '3.141592') # http://localhost:5000/area?radius=10
    radius = request.values['radius']
    a = float(pi) * float(radius) ** 2
    return f'<h1>pi={pi}, radius={radius}, area={a}</h1>'


@app.route('/login', methods=['GET', 'POST']) # methods복수
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:   # method가 POST /post입력값을 값고 아이디,비번이 맞음그와맞는것으로 틀리면 그거와 맞는것으로 ...들어가는
        uid = request.form['uid']
        pwd = request.values['pwd']
        return f'<h1>uid={uid}, pwd={pwd}</h1>' # get이나 post나 동일한이름을 가져가는게 요즘 추세...? / 웹이서 확인을 누르니까 환영합니다가됨 url로도 서버에서도 메소드 처리가능 메소드로도 처리가능이라는데 무슨말인지

# method에 맞게 내가 원하는거를 가져갈수있다..
# values는 get , post둘다 사용가능 귀찮으면 values를 사용해라


if __name__ == '__main__': 
    app.run(debug=True)



