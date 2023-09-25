from flask import Flask, render_template, request
import os
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/scatter', methods=['GET', 'POST'])
def scatter_res():
    if request.method == 'GET':
        return render_template('99.scatter.html')
    else:       # POST이면
        count = int(request.form['count'])
        min = int(request.form['min'])
        max = int(request.form['max'])
        mean = int(request.form['mean'])
        std = int(request.form['std'])
        
        X = np.random.normal(mean, std, count)      # 정규분포
        Y = np.random.uniform(min, max, count)
        plt.scatter(X,Y)
        
        img_file = os.path.join(app.root_path, 'static/img/scatter_01.png')
        plt.savefig(img_file)
        
        mtime = int(os.stat(img_file).st_mtime)
        print(count, min, max, mean, std)
        return render_template('99.scatter_res.html');

    
if __name__ == '__main__':
    app.run(debug=True)