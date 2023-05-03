from flask import Flask , render_template
import random

app = Flask(__name__)



@app.route('/garam') # decorator route를 '/'로
def garam(): # 사용자가 어떤 path를 입력하지 않고 들어올때 retrun으로 응대해라
    return '''<!doctype html>
    <html>
        <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            <li><a href="/read/1/">html</a></li>
            <li><a href="/read/2/">css</a></li>
            <li><a href="/read/3/">js</a></li>
        </ol>
        <h2>Welcome</h2>
        Hello, web
        </body>
    </html>
    ''' 

@app.route('/hello') # 사용자가 /hello로 입력했을때 return으로 응대
def hello():
    return render_template('01.hello.html')


# variable rules
@app.route('/read/<id>')
def read():
    return 'Read' + id  

if __name__ == '__main__': 
    app.run(debug=True) 
