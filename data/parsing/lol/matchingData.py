import json
import time
from roleml import roleml
from datetime import datetime

import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder

file = open("new_dataset.csv",'w',encoding='UTF8')

file.writelines(','.join(["Bot1","Bot2","Play"]))
file.write('\n')


with open(f"./MATCHS-RGAPI-9999047c-e9e4-4bf3-a231-ca24ccb79445.json", 'r', encoding='UTF8') as jsonfile:
    data =json.load(jsonfile)
    # game 안에 데이터 접근
    data2 = data['game']
    # 리스트 돌리면서 데이터 확인!
    rating = {}
    duorating = [[0]*500 for i in range(500)]
    for i in range(len(data2)):
        team1_df = pd.DataFrame()
        team2_df = pd.DataFrame()
        data3 = data2[i]['participants']
        for j in data3:
            if f'{j["championId"]}' in rating.keys():
                if j["stats"]["win"] :
                    rating[f'{j["championId"]}'][0] = rating[f'{j["championId"]}'][0] +1
                else:
                    rating[f'{j["championId"]}'][1] = rating[f'{j["championId"]}'][1] +1
                    #  print(rating)
            else:
                rating[f'{j["championId"]}'] = [0,0,0]
                if j["stats"]["win"] :
                    rating[f'{j["championId"]}'][0] = rating[f'{j["championId"]}'][0] +1
                else:
                    rating[f'{j["championId"]}'][1] = rating[f'{j["championId"]}'][1] +1

    for i in rating:
        win = rating[i][0]
        loss = rating[i][1]
        rating[i][2] = win/(win+loss)*100
        # print(rating[i][2]*100,"%")


    # print(rating)

with open(f"../../MATCHS-0.json", 'r', encoding='UTF8') as data_file:
    f1 = json.load(data_file)
with open(f"./TIMELINE-0.json", 'r', encoding='UTF8') as data_file:
    f2 = json.load(data_file)
with open(f"./MATCHS-RGAPI-c0655252-3b8e-4d72-8494-729ed8a3d16d.json", 'r', encoding='UTF8') as jsonfile:
    data =json.load(jsonfile)

data2 = data['game']
cnt=0
Kerror = 0
Ierror = 0
duorating = [[0]*600 for i in range(600)]
rating = {}
for idx,v in enumerate(f1['game']):
    try:
        cnt+=1
        a = f1['game'][idx]
        b = (f2['timeline'][idx])
        c = f1['game'][idx]['gameDuration']
        data3 = data2[idx]['participants']
        # print(cnt)
        if c <= 720:
            continue

        line = roleml.predict(a, b)
        # print(line)
        bot1 = 0
        supp1 = 0
        bot2 = 0
        supp2 = 0
        win1 = 0
        win2 = 0
        for num in data3:
            n =  num.get("participantId")

            check = num.get("stats")
            #1이면 승리 0이면 패배
            if n<=5 and check.get("win"):
                win1 = 1
            if n>5 and check.get("win"):
                win2 = 1

            if n <= 5 and line.get(n) == 'supp':
                supp1 = num.get("championId")
            # print(n)
            if n <= 5 and line.get(n) == "bot":
                bot1 = num.get("championId")

            if n > 5 and line.get(n) == 'supp':
                supp2 = num.get("championId")
            # print(n)
            if n > 5 and line.get(n) == "bot":
                bot2 = num.get("championId")


        # print(bot1,supp1,win1,"vs",bot2,supp2,win2)
        #승0000패0000
        #둘다 널이 아니면 추가
        if bot1 > 0 and supp1 >0 :
            # print(type(bot1))
            # print(type(supp1))
            if win1 ==1: #승리
                duorating[bot1][supp1] += 10000
                duorating[supp1][bot1] += 10000
                file.writelines(','.join([str(bot1),str(supp1),"yes"]))
                file.write('\n')
            else:
                duorating[bot1][supp1] += 1
                duorating[supp1][bot1] += 1
                file.writelines(','.join([str(bot1),str(supp1),"no"]))
                file.write('\n')
        if bot2 >0 and supp2 >0:
            if win2 ==1: #승리
                duorating[bot2][supp2] += 10000
                duorating[supp2][bot2] += 10000
                file.writelines(','.join([str(bot2),str(supp2),"yes"]))
                file.write('\n')
            else:
                duorating[bot2][supp2] += 1
                duorating[supp2][bot2] += 1
                file.writelines(','.join([str(bot2),str(supp2),"no"]))
                file.write('\n')
    except KeyError as e:
        Kerror+=1
        print(e)
        continue
    except IndexError as e:
        Ierror+=1
        print(e)
        continue

for i in range(0, 600):
    for j in range(0, 600):
        point = duorating[i][j]
        winpoint = point//10000
        losspoint = point%10000
        if winpoint > 0 or losspoint >0:
            rat = winpoint/(winpoint+losspoint) *100
        #    print(i,j,duorating[i][j],point,winpoint,losspoint,rat)
            duorating[i][j] = rat

test = pd.DataFrame(duorating)
print(test)
