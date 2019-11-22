import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

#챔피언 데이터 db 저장
def create_champion():
    champion = open('./champion_kr.json','rb').read()
    ch = json.loads(champion)
    request_data ={'champion':{
    'char_id':[],'name_kr':[],'name_eng':[],'info_attack':[],'info_defence':[],
    'info_magic':[],'info_difficulty':[],'info_tag':[],'attack_range':[]
    }}
    for i,v in ch['data'].items():
        request_data['champion']['char_id'].append(ch['data'][i]['key'])
        request_data['champion']['name_kr'].append(ch['data'][i]['name'])
        request_data['champion']['name_eng'].append(ch['data'][i]['id'])
        request_data['champion']['info_attack'].append(ch['data'][i]['info']['attack'])
        request_data['champion']['info_defence'].append(ch['data'][i]['info']['defense'])
        request_data['champion']['info_magic'].append(ch['data'][i]['info']['magic'])
        request_data['champion']['info_difficulty'].append(ch['data'][i]['info']['difficulty'])
        request_data['champion']['attack_range'].append(ch['data'][i]['stats']['attackrange'])
        tag = ""
        for k in ch['data'][i]['tags']:
            k+=" "
            tag+=k
        request_data['champion']['info_tag'].append(tag)
    
    response = requests.post(API_URL + 'lol-attack-info/', data=json.dumps(request_data), headers=headers)
    print(response.text)

if __name__ == '__main__':
   create_champion()
#    centers, labels = find_clusters(X, 4)
#    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')