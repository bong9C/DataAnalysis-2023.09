from flask import Flask, render_template, request

app = Flask(__name__)
                    # htp://127.0.0.1:5000/ (/ 생략)
@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드 
def index():
    return '<h1>파라메터 전달값 받기</h1>'

# localhost:5000/area?pi=3.14&radius=10 => area 에 파이값과 레디우스 값을 전달 한 것
@app.route('/area')
def area():
    pi = request.args.get('pi', '3.14159')      # default 값을 지정할 수 있음 
    radius = request.values['radius']           # GET/POST 모두 사용할 수 있음
    result = float(pi) * float(radius) ** 2
    return f'<h1>pi={pi}, radius={radius}, area={result}</ul>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:       # POST이면
        uid = request.form['uid']
        pwd = request.values['pwd']
        return f'<h1>uid={uid}, pwd={pwd} <h1>환영합니다.</h1>'

@app.route('/sample', methods=['GET', 'POST'])
def sample():
    if request.method == 'GET':
        return render_template('02.sample.html')
    else:       # POST이면
        a = int(request.form['a'])
        b = int(request.form['b'])
        return f'<h1>a={a}, b={b}, a*b = {a*b}</h1>'
    

# localhost: 5000/user/james, ;ocalhost:5000/user/maria
@app.route('/user/<uname>')
def user(uname):        # uname 타입 string ( 파라메터로 넘어 오는 값은 전부 string다. )
    return f'<h1>uname = {uname}</h1>'

# localhost:5000/square/12
@app.route('/square/<int:number>') # 여기서 타입변환을 주면 44번에서는 인트(타입변환) 안줘도 됨
def square(number):     # number 타입 string ( 파라메터로 넘어 오는 값은 전부 string다. )
    return f'<h1>{number} ** 2 = {number ** 2} </h1>' # ( 근데 인트로 바꿔주기도 함.)      

# localhost:5000/circle/3.14/and/10.0 ( 실수이기 때문에 뒷자리를 실수로 넣어줘야함, 아니며 radius 를 int로 바꿔주어야 함.)
@app.route('/circle/<float:pi>/and/<float:radius>')
def circle(pi,radius):
    result = pi * radius ** 2
    return f'<h1>pi={pi}, radius={radius}, area={result}</h1>'

 # Form으로 받을때는 request!!  반드시 기억!!!

if __name__ == '__main__':
    app.run(debug=True)