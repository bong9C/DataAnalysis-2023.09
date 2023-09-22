import os 
from flask import Flask, render_template

app = Flask(__name__)
                    # htp://127.0.0.1:5000/ (/ 생략)
@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드 
def index():
    return '<h1>Static Resource</h1>'

@app.route('/static')
def static_recource():
    print(app.root_path)            # D:/WorkSpace/02.DataAnalysis/07.FlaskWeb
    img_file = os.path.join(app.root_path, 'static/img/cat.jpg')  # FlaskWab 에 Static 가 있는 곳이 root 임
    return render_template('04.static.htma')


 if __name__ == '__main__':
    app.run(debug=True)   