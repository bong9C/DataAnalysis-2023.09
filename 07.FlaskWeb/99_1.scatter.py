import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>산점도 그리기</h1>
                <button onclick="location.href='/scatter'">실행</button>'''


@app.route('/scatter', methods=['GET','POST'])
def scatter():
    if request.method == 'GET':
        return render_template('99_1.scatter.from.html')
    else:
        num = int(request.form['num'])
        avg = float(request.form['avg'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        xs = np.random.normal(avg, std, num)      # 평균, 표준편차, 갯수
        ys = np.random.uniform(min,max, num)      # 최소, 최대, 갯수
        plt.figure()
        plt.scatter(xs, ys)
        filename = os.path.join(app.static_folder, 'img/scatter_01.png')
        plt.savefig(filename)
        # return render_template('99_1.scatter.res.html', avg=avg, std=std, min=min, max=max)
        params = {'avg':avg, 'std':std, 'min':min, 'max':max} # 딕셔너리로 파라메터를 전달
        return render_template('99_1.scatter.res.html', params=params)  # 딕셔너리로 파라메터를 전달
    

if __name__ == '__main__':
    app.run(debug=True)   
