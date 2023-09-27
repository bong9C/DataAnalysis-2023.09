from flask import Blueprint, render_template, current_app, request
import util.map_util as mu

map_bp = Blueprint('crawl_bp', __name__)

menu = {'ho':0, 'us':0, 'cr':0, 'ma':1, 'sc':0}

@map_bp.route('/station', methods=['GET','POST'])
def station():
    if request.method == 'GET':
        return render_template('map/station_form.html')
    else:
        stations = request.form.getlist('station')
        stations = [station for station in stations if len(station.strip()) != 0]    # 5개미만으로 작성하여도 잘 돌아감
        mu.get_station_map(current_app.root_path, stations)       # static/img/station_map.html 파일 
        return render_template('map/station_form.html')

@map_bp.route('/cctv_pop', methods=['GET', 'POST'])
def cctv_pop():
    if request.method == 'GET': 
        columns = ['CCTV댓수', '최근증가율', '인구수', '내국인', '외국인', '고령자', '외국인 비율', '고령자 비율']
        colormaps = ['RdPu', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
        return render_template('map/cctv_pop_form.html', columns=columns, colormaps=colormaps, menu=menu)
    else:
        column = request.form['column']
        colormap = request.form['colormap']
        mu.get_cctv_pop(current_app.static_folder, column, colormap)
        return render_template('map/cctv_pop_form.html', column=column, colormap=colormap, menu=menu)
if __name__ == '__main__':
    map.run(debug=True)