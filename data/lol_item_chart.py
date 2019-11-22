import requests
import json
API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}
#챔피언 데이터 db 저장
def create_pickbans():
    result = {}
    item_dict = {'itempick':[]}
    request_data = {'itempick':[]}
    with open(f"./MATCHS-0.json",'r',encoding='UTF8') as outfile:
        itempicks=json.load(outfile)
    
    for i in range(len(itempicks['game'])):
        pick_id = [0]*7
        for j in range(len(itempicks['game'][i]['participants'])):
            pick_id[0] = itempicks['game'][i]['participants'][j]["stats"]["item0"]
            pick_id[1] = itempicks['game'][i]['participants'][j]["stats"]["item1"]
            pick_id[2] = itempicks['game'][i]['participants'][j]["stats"]["item2"]
            pick_id[3] = itempicks['game'][i]['participants'][j]["stats"]["item3"]
            pick_id[4] = itempicks['game'][i]['participants'][j]["stats"]["item4"]
            pick_id[5] = itempicks['game'][i]['participants'][j]["stats"]["item5"]
            pick_id[6] = itempicks['game'][i]['participants'][j]["stats"]["item6"]
            
            for k in range(7):
                # 수정한 부분 pick_id 가 set으로 들어가서 에러가남
                # set이란 중복없는 값을 가진 데이터 형태 요렇게 생김{1,2,3}
                # 수정전 item_dict['itempick'].append({pick_id[k]})
                item_dict['itempick'].append(pick_id[k])

        # print(item_dict)
    count=0
    for i in item_dict['itempick']:
        count+=1
        id = i
        print(id)
        print("hihi")
        cnt = 0
        check = 0
        for k in request_data['itempick']:
            if id == k['item_id']:
                check=1

        if check == 0:
            for j in item_dict['itempick']:
                if id==j :
                    cnt+=1
            request_data['itempick'].append({
                'item_id':id,
                'item_cnt':cnt
            })
            # print(request_data)
        print(count)
    print(request_data)
    response = requests.post(API_URL + 'lol-item-chart-list/', data=json.dumps(request_data), headers=headers)
    print(response.text)

if __name__ == '__main__':
    create_pickbans()