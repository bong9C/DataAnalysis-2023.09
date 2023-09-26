import requests, json, os, folium      # requests 인터넷으로 자료를 받아서 가지고 올 때 사용 
import pandas as pd
from urllib.parse import quote 

def get_station_map(root_path, stations):
    filename = os.path.join(root_path, 'static/keys/도로명주소apikey.txt')
 # filename='../04.지도시각화/keys/도로명주소apikey.txt'
    with open(filename) as file:
        road_key = file.read()

    base_url = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
    params1 = f'confmKey={road_key}&currentPage=1&countPerPage=10'
    # params2 = f'keyword={quote("영등포역")}&resultType=json'
    # url = f'{base_url}?{params1}&{params2}'  => 아래 18번에서 만들어짐으로 필요 없는 코드.
    road_addr_list = []
    for station in stations:
        params2 = f'keyword={quote(station)}&resultType=json'
        url = f'{base_url}?{params1}&{params2}'
        result = requests.get(url)
        if result.status_code == 200:
            res = json.loads(result.text)
            road_addr_list.append(res['results']['juso'][0]['roadAddr'])
        else:
            print(result.status_code)
    df = pd.DataFrame({'이름': stations, '주소': road_addr_list})


    # 위도, 경도 좌표 구하기 ( 카카오 로컬 참고 )
    filename = os.path.join(root_path, 'static/keys/카카오apikey.txt')
    with open('keys/카카오apikey.txt') as file:
                kakao_key = file.read()
    base_url = 'https://dapi.kakao.com/v2/local/search/address.json'
    header = {'Authorization': f'KakaoAK {kakao_key}'}

    lat_list, lng_list = [], []
    for i in df.index:
        url = f'{base_url}?query={quote(df["주소"][i])}'
        result = requests.get(url, headers=header).json()
        lat_list.append(float(result['documents'][0]['y']))
        lng_list.append(float(result['documents'][0]['x']))
    df['위도'] = lat_list
    df['경도'] = lng_list

    # map 그리기
    map = folium.Map(location=[df.위도.mean(),df.경도.mean()], zoom_start=14) #Center position
    for i in df.index:
        folium.Marker(
            location=[df.위도[i], df.경도[i]],
            tooltip=df.이름[i],
            popup=folium.Popup(df.주소[i], max_width=200)
        ).add_to(map)

    filename = os.path.join(root_path, 'static/img/station_map.html')
    map.save(filename)

    