import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_teamData(cnt):
    if cnt ==10000:
        return
    with open(f'./MATCHS-{cnt}.json', 'r', encoding='UTF8') as json_file:
        data = json.load(json_file)
    request_data = {'gameResult' : []}
    for i in range(len(data['game'])):
        teamData ={'0':{}, '1':{},'gameDuration':data['game'][i]['gameDuration']}
        for j in range(2):
            teamData[str(j)].update(data['game'][i]['teams'][j])
        request_data['gameResult'].append(teamData)
    response = requests.post(API_URL + 'lol-addTeamData-list/', data=json.dumps(request_data), headers=headers)
    print(response.text)
    cnt+=1000
    create_teamData(cnt)

if __name__ == '__main__':
    cnt=0
    create_teamData(cnt)
