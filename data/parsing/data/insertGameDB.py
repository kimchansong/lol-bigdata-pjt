import json
import time
import requests
from roleml import roleml
from datetime import datetime

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}
      
def gameData(cnt):
    if cnt>60000:
        return
    with open(f"./MATCHS-{cnt}.json", 'r', encoding='UTF8') as data_file:
            f1 = json.load(data_file)

    with open(f"./TIMELINE-{cnt}.json", 'r', encoding='UTF8') as data_file1:
            f2 = json.load(data_file1)  
    userDB = {'user' :{
            'top':{
                'championId':[], 'userId':[], 'win':[], 'kills':[], 'death':[], 'assists':[]
            },
            'jungle':{
                'championId':[], 'userId':[], 'win':[], 'kills':[], 'death':[], 'assists':[]
            },
            'mid':{
                'championId':[], 'userId':[], 'win':[], 'kills':[], 'death':[], 'assists':[]
            },
            'bot':{
                'championId':[], 'userId':[], 'win':[], 'kills':[], 'death':[], 'assists':[]
            },
            'supp':{
                'championId':[], 'userId':[], 'win':[], 'kills':[], 'death':[], 'assists':[]
            }
    }}
    for idx,v in enumerate(f1['game']):
        try: 
            c = f1['game'][idx]['gameDuration']
            if c <= 720:
                continue
            a = f1['game'][idx]
            b = f2['timeline'][idx]
            posi = roleml.predict(a, b)
            LeftTeam = f1['game'][idx]['teams'][0]['win']    #승패 여부는 Win Fail로 나옴
            leftTeamWin = False
            
            if LeftTeam =="Win": #teamId 100인 팀이 승리한 경우 1~5번 유저가 이김
                leftTeamWin =True
            for i in range(len(f1['game'][idx]['participants'])):
                index = i+1
                position = posi[index]
                participantId = f1['game'][idx]['participants'][i]['participantId']
                championId = f1['game'][idx]['participants'][i]['championId']
                kills = f1['game'][idx]['participants'][i]['stats']['kills']
                death = f1['game'][idx]['participants'][i]['stats']['deaths']
                assists = f1['game'][idx]['participants'][i]['stats']['assists']
                userId = f1['game'][idx]['participantIdentities'][i]['player']['summonerName']
                win = 0
                if i<5:
                    if leftTeamWin == True:
                        win = 1
                        userDB['user'][position]['championId'].append(championId)
                        userDB['user'][position]['userId'].append(userId)
                        userDB['user'][position]['win'].append(win)
                        userDB['user'][position]['kills'].append(kills)
                        userDB['user'][position]['death'].append(death)
                        userDB['user'][position]['assists'].append(assists)
                    else :
                        win =0
                        userDB['user'][position]['championId'].append(championId)
                        userDB['user'][position]['userId'].append(userId)
                        userDB['user'][position]['win'].append(win)
                        userDB['user'][position]['kills'].append(kills)
                        userDB['user'][position]['death'].append(death)
                        userDB['user'][position]['assists'].append(assists)
                if i>4:
                    if leftTeamWin == True:
                        win = 0
                        userDB['user'][position]['championId'].append(championId)
                        userDB['user'][position]['userId'].append(userId)
                        userDB['user'][position]['win'].append(win)
                        userDB['user'][position]['kills'].append(kills)
                        userDB['user'][position]['death'].append(death)
                        userDB['user'][position]['assists'].append(assists)
                    else : 
                        win = 1
                        userDB['user'][position]['championId'].append(championId)
                        userDB['user'][position]['userId'].append(userId)
                        userDB['user'][position]['win'].append(win)
                        userDB['user'][position]['kills'].append(kills)
                        userDB['user'][position]['death'].append(death)
                        userDB['user'][position]['assists'].append(assists)
        except KeyError as e:
            print(e)
            continue
        except IndexError as e:
            print(e)
            continue
    response = requests.post(API_URL + 'lol-champion-info/', data=json.dumps(userDB), headers=headers)
    print(response.text)
    cnt+=1000
    time.sleep(5)
    gameData(cnt)
if __name__ == '__main__':
    cnt = 0
    gameData(cnt)