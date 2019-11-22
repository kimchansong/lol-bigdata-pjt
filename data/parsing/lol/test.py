import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_champion():
    champion = open('./test.json','rb').read()
    ch = json.loads(champion)
    request_data ={'champion':{
    'char_id':[],'name_kr':[],'name_eng':[],'info_attack':[],'info_defence':[],
    'info_magic':[],'info_difficulty':[],'info_tag':[],'attack_range':[]
    }}
    for i,v in ch['data'].items():
        print(ch['data'][i]['name'])
        # if i=="name":
        #     print(ch['data'][i])
        # print(i,v)
        # print(ch['data'])
        # request_data['champion']['char_id'].append(ch['data']['key'][i])
        # request_data['champion']['name_kr'].append(ch['data']['name'][i])
        # request_data['champion']['name_eng'].append(ch['data']['id'][i])
        # request_data['champion']['info_attack'].append(ch['data']['attack'][i])
        # request_data['champion']['info_defence'].append(ch['data']['defence'][i])
        # request_data['champion']['info_magic'].append(ch['data']['magic'][i])
        # request_data['champion']['info_difficulty'].append(ch['data']['difficulty'][i])
        # request_data['champion']['info_tag'].append(ch['data']['tags'][i])
        # request_data['champion']['attack_range'].append(ch['data']['attack_range'][i])
    # response = requests.post(API_URL + 'lol-attack-info/', data=json.dumps(request_data), headers=headers)
    # print(response.text)

if __name__ == '__main__':
   create_champion()
#    centers, labels = find_clusters(X, 4)
#    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')