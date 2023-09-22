from flask import Flask, render_template

app = Flask(__name__)
                    # htp://127.0.0.1:5000/ (/ 생략)
@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드 
def index():
    return '<h1>Hello Flask</h1><h2>Flask 좋아요!!!</h2>'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')
    
@app.route('/sub/hello')
def sub_hello():
    return render_template('sub/01.hello.html')

if __name__ == '__main__':
    app.run(debug=True)