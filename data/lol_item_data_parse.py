import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

#챔피언 데이터 db 저장
def create_items():
    with open(f"MATCHS-0.json",'r',encoding='UTF8') as outfile:
        items=json.load(outfile)
        one_thousand={'champ_items':[]}
        request_data={'champ_items':[]}

        for idx,value in enumerate(items['game']):
            item_champ = [0]*7
            for i in range(len(items['game'][idx]['participants'])):
                championId = items['game'][idx]['participants'][i]['championId']
                
                item_champ[0] = items['game'][idx]['participants'][i]['stats']['item0']
                item_champ[1] = items['game'][idx]['participants'][i]['stats']['item1']
                item_champ[2] = items['game'][idx]['participants'][i]['stats']['item2']
                item_champ[3] = items['game'][idx]['participants'][i]['stats']['item3']
                item_champ[4] = items['game'][idx]['participants'][i]['stats']['item4']
                item_champ[5] = items['game'][idx]['participants'][i]['stats']['item5']
                item_champ[6] = items['game'][idx]['participants'][i]['stats']['item6']

                for num in range(7):
                    one_thousand['champ_items'].append({
                        'char_id':championId,
                        'item_id':item_champ[num],
                        'item_cnt':0
                    })
    count = 0
    for line in one_thousand['champ_items']:
        print(line)
        cnt = 0
        checkInfo = 0
        championId = line['char_id']
        item_champ = line['item_id']
        for line2 in one_thousand['champ_items']:
            if line['char_id']==line2['char_id'] and line['item_id'] == line2['item_id']:
                cnt+=1
        for check in request_data['champ_items']:
            if line['char_id']==check['char_id'] and line['item_id'] == check['item_id']:
                checkInfo = 1
            if line['item_id']==0:
                checkInfo = 2
        if checkInfo == 0 :
            request_data['champ_items'].append({
                'char_id':championId,
                'item_id':item_champ,
                'item_cnt':cnt
            })
        print(request_data)
        count+=1

        print(count)
        print()

    response = requests.post(API_URL + 'lol-item-list/', data=json.dumps(request_data), headers=headers)
    print(response.text)

if __name__ == '__main__':
   create_items()