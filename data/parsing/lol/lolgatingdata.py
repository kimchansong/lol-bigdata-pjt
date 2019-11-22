import json
import time
from roleml import roleml
from datetime import datetime

import pandas as pd
import requests
import json
from sklearn.preprocessing import LabelEncoder

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

file = open("new_dataset.csv",'w',encoding='UTF8')

request_data = {"naviedata":[]}

file.writelines(','.join(["Bot1","Bot2","Bot3","Bot4","Bot5","fBlood","fT","fD","fB","TK","DK","BK","Win"]))
file.write('\n')

request_data["naviedata"].append("Bot1,Bot2,Bot3,Bot4,Bot5,fBlood,fT,fD,fB,TK,DK,BK,Win")
team1 = ""
team2 = ""

datanames =["MATCHS-52000.json","MATCHS-53000.json","MATCHS-54000.json","MATCHS-55000.json","MATCHS-56000.json","MATCHS-57000.json","MATCHS-58000.json","MATCHS-59000.json","MATCHS-60000.json" ]

for dataname in datanames:
    # print(f"./{dataname}")
    # break
    with open(f"./{dataname}", 'r', encoding='UTF8') as jsonfile:
        data =json.load(jsonfile)
        data2 = data['game']

        for i in range(len(data2)):
            data3 = data2[i]['teams']
            data4 = data2[i]['participants']
            # print(data3)
            for k in range(len(data4)):
                if k<5:
                    num = data4[k]['championId']
                    file.write(str(num))
                    file.write(',')
                    team1 = team1 + str(num) + ","

            if data3[0]['firstBlood']:
                fBlood = 1;
            else:
                fBlood = 0;
            if data3[0]['firstTower']:
                fT = 1;
            else:
                fT = 0;
            if data3[0]['firstDragon']:
                fD = 1;
            else:
                fD = 0;
            if data3[0]['firstBaron']:
                fB = 1;
            else:
                fB = 0;
            TK = data3[0]['towerKills']
            DK = data3[0]['dragonKills']
            BK = data3[0]['baronKills']

            if data3[0]['win'] == "Win":
                win = "yes";
            else:
                win = "no";

            file.writelines(','.join([str(fBlood),str(fT),str(fD),str(fB),str(TK),str(DK),str(BK),str(win)]))
            file.write('\n')
            team1 = team1 + ','.join([str(fBlood),str(fT),str(fD),str(fB),str(TK),str(DK),str(BK),str(win)])
            request_data["naviedata"].append(team1)
            team1 = ""

            for k in range(len(data4)):
                if k>=5:
                    num = data4[k]['championId']
                    file.write(str(num))
                    file.write(',')
                    team2 = team2 + str(num) + ","

            if data3[1]['firstBlood']:
                fBlood = 1;
            else:
                fBlood = 0;
            if data3[1]['firstTower']:
                fT = 1;
            else:
                fT = 0;
            if data3[1]['firstDragon']:
                fD = 1;
            else:
                fD = 0;
            if data3[1]['firstBaron']:
                fB = 1;
            else:
                fB = 0;
            TK = data3[1]['towerKills']
            DK = data3[1]['dragonKills']
            BK = data3[1]['baronKills']
            if data3[1]['win'] == "Win":
                win = "yes";
            else:
                win = "no";
            file.writelines(','.join([str(fBlood),str(fT),str(fD),str(fB),str(TK),str(DK),str(BK),str(win)]))
            file.write('\n')
            team2 = team2 + ','.join([str(fBlood),str(fT),str(fD),str(fB),str(TK),str(DK),str(BK),str(win)])
            request_data["naviedata"].append(team2)
            team2 = ""

    response = requests.post(API_URL + 'lol-navie-data-list/', data=json.dumps(request_data), headers=headers)
# print(request_data["naviedata"][1])
# print(request_data["naviedata"][2])
# print(request_data["naviedata"][3])
# print(request_data["naviedata"][4])
