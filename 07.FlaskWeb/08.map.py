# 컨트롤러
from flask import Flask, render_template, request
import util.map_util as mu

app = Flask(__name__)
                    # htp://127.0.0.1:5000/ (/ 생략)
@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드 
def index():
    return '''
        <h1>지도 시각화</h1>
        <button onclick="location.href='/station'">지하철역 찾기</button>
    '''


@app.route('/station', method=['GET','POST'])
def station():
    if request.method == 'GET':
        return render_template('08.station_form.html')
    else:
        station_map = mu.get_station_map('station')
        station_map = mu.get_station_map(station)
        # return render_template('08.station_form.html')
        return f'<h3>{station}<h3>'
    
if __name__ == '__main__':
    app.run(debug=True)