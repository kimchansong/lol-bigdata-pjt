import requests
import json
API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}
#챔피언 데이터 db 저장
def create_pickbans():
    result = {}
    ban_dict ={}
    pick_dict ={}
    request_data = {'pickban':[]}
    with open(f"./MATCHS-0.json",'r',encoding='UTF8') as outfile:
        banpicks=json.load(outfile)
    with open(f'./champion_kr.json','r',encoding='UTF8') as outfile2:
        champion = json.load(outfile2)
    for i in range(len(banpicks['game'])):
        for j in range(len(banpicks['game'][i]['teams'])):
            for k in range(len(banpicks['game'][i]['teams'][j]['bans'])):
                ban_id = banpicks['game'][i]['teams'][j]['bans'][k]["championId"]
                if ban_id in ban_dict.keys():
                    ban_dict[ban_id] += 1
                else:
                    ban_dict[ban_id] = 1
        for j in range(len(banpicks['game'][i]['participants'])):
            pick_id = banpicks['game'][i]['participants'][j]["championId"]
            if pick_id in pick_dict.keys():
                pick_dict[pick_id] += 1
            else:
                pick_dict[pick_id] = 1
    for i in ban_dict.keys():
        result[i] = [0,ban_dict[i],0]
    for j in pick_dict.keys():
        if j in result.keys():
            result[j][0] = pick_dict[j]
        else:
            result[i] = [pick_dict[i],0,0]
    for i in champion["data"].keys():
        result_key = int(champion["data"][i]["key"])
        if result_key in result.keys():
            result[result_key][2] = i
        else:
            result[result_key] = [0,0,i]
    print(result)
    
    count=0
    for k,v in result.items():
        count+=1
        request_data['pickban'].append({'id':k,'name':v[2],'pickcount':v[0],'bancount':v[1]})
        # if count == 10:
        #     break
        print(count)
    response = requests.post(API_URL + 'lol-pickban-list/', data=json.dumps(request_data), headers=headers)

if __name__ == '__main__':
 create_pickbans()