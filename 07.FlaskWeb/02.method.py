from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>method 확인<br>/login으로 확인해 보세요'

# login 두가지 메소드 이용
# 1) GET 메소드
# 2) Post 메소드       
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:       # POST이면
        return '<h1>환영합니다.</h1>'

@app.route('/sample', methods=['GET', 'POST'])
def sample():
    if request.method == 'GET':
        return render_template('02.sample.html')
    else:       # POST이면
        return '<h1>샘플입니다.</h1>'

if __name__ == '__main__':
    app.run(debug=True)