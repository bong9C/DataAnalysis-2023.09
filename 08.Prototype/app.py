from flask import Flask, render_template, request
from bp.crawling import crawl_bp

app = Flask(__name__)

app.register_blueprint(crawl_bp, url_prefix='/crawling')        # localhost:5000/crawling/*는 crawl bp가 처리

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('home.html', menu=menu)

@app.route('/crawling/melon')
def melon():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    song_list = cu.get_melon_chart()
    return render_template('crawling/melon.html', song_list=song_list, menu=menu)


@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('schedule.html', menu=menu)

@app.route('/siksin')
def siksin():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    place_list = cu.get_siksin_chart()
    return render_template('siksin.html', place_list=place_list, menu=menu)

if __name__ == '__main__':
    app.run(debug=True)