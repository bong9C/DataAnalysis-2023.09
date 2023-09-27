import requests

def get_weather(static_path, lat, lng):
    filename = f'{static_path}/keys/OpenweatherApiKey.txt'
    with open(filename) as file:
        weather_key = file.read()
    base_url = 'https://api.openweathermap.org/data/2.5/onecall'
    lat, lng = 37.5260, 126.8964
    url = f'{base_url}?lat={lat}&lon={lng}&appid={weather_key}&units=metric&lang=kr'
    result = requests.get(url).json()

    temp=result['current']['temp']
    desc = result['current']['weather'][0]['description']
    icon_code = result['current']['weather'][0]['icon']
    icon_url = f'http://api.openweathermap.org/img/w/{icon_code}.png'
    urllib.request.urlretrieve(icon_url, '../static/img/icon.png')
    img = Image.open('../static/img/icon.png')
    plt.imshow(img), plt.axis('off');