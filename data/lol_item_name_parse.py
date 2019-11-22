import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

#챔피언 데이터 db 저장
def create_items_name():
    url = "http://ddragon.leagueoflegends.com/cdn/9.19.1/data/ko_KR/item.json"
    item_name = requests.get(url).json()
    request_data={'champ_items_name':[]}

    count = 0
    for idx,value in enumerate(item_name['data'].keys()):
        print(idx, value)
        key = value
        name = item_name['data'][value]['name']
        request_data['champ_items_name'].append({
            'name':name,
            'key':key
        })
        print(key)
        print(name)

        count+=1
        print()

    response = requests.post(API_URL + 'lol-item-name-list/', data=json.dumps(request_data), headers=headers)
    print(response.text)

if __name__ == '__main__':
   create_items_name()