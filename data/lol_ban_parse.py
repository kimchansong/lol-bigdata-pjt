import requests
import json
API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}
#챔피언 데이터 db 저장
def ban_couting():

    ban_dict={}

    with open(f"./MATCHS-0.json",'r',encoding='UTF8') as outfile:
        matchdata=json.load(outfile)
    with open(f'./champion_kr.json','r',encoding='UTF8') as outfile2:
        champion = json.load(outfile2)
        championlist = {}
        for k,v in champion['data'].items():
            championlist[v['key']] = v['name']
        request_data={'bancount':[]}
        for match_id in range(len(matchdata['game'])):
            for i in range(len(matchdata['game'][match_id]['participants'])):
                idx = matchdata['game'][match_id]['participants'][i]['participantId']-1
                if 0<=idx <=4:
                    char_id = matchdata['game'][match_id]['participants'][i]['championId']
                    ban_id = matchdata['game'][match_id]['teams'][0]['bans'][idx]['championId']
                elif 5<=idx <=9:
                    char_id = matchdata['game'][match_id]['participants'][i]['championId']
                    ban_id = matchdata['game'][match_id]['teams'][1]['bans'][idx%5]['championId']
                if ban_id == -1:
                    pass
                else:
                    ban_dict_key = (char_id,ban_id,championlist[str(char_id)],championlist[str(ban_id)])
                if ban_dict_key in ban_dict.keys():
                    ban_dict[ban_dict_key] += 1
                else:
                    ban_dict[ban_dict_key] = 1
    for k,v in ban_dict.items():
        print(k[0],k[1],k[2],k[3],v)
        request_data['bancount'].append({
            'name':k[2],
            'char_id':k[0],
            'ban_char_id':k[1],
            'cnt':v,
        })
        print(request_data)
    response = requests.post(API_URL + 'lol-ban-count-list/', data=json.dumps(request_data), headers=headers)
    print(response.text)
if __name__ == '__main__':
    ban_couting()