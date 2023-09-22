import os
from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/')
def index():
    return '<h1>Static Resource</h1>'

@app.route('/static')
def static_resource():                      # 함수명에는 키워드이름으로  쓰면 에러!
    print(app.root_path)                    # 해당 파일 위치가 root_path (D:\WorkSpace\02.DataAnalysis\07.FlaskWeb)
    img_file = os.path.join(app.root_path, 'static/img/cat.jpg')
    # static resource가 Cache로 인하여 즉시 변경이 안되는 경우도 있음
    mtime = int(os.stat(img_file).st_mtime)      # 마지막으로 변경된 시간
    return render_template('04.static.html', mtime=mtime)       # html에서 mtime을 변수로 사용가능

if __name__ == '__main__':
    app.run(debug=True)