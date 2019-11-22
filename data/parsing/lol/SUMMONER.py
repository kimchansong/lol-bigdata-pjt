import requests
import threading
import time
from datetime import datetime
now = datetime.now()
nowDate = now.strftime('%Y%m%d')
file = open(f"SUMMONER-_{nowDate}.dat",'w',encoding='UTF8')
f1 = open("./LEAGUE-EXP-V4_20190918.dat", 'r', encoding='UTF8')


def set_start():
    cnt = 1
    while True:
        try:
            line = f1.readline()
            if line == "":
                break;
            cnt+=1
            if cnt%100 == 0:
                time.sleep(120)
            summonerName = line.split('::')[0]
            key = "RGAPI-c1079d63-cde2-4305-89d1-fd3e4151988e"
            url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(summonerName,key)
            r = requests.get(url).json()
            print(r)
            file.writelines('::'.join([r['name'],r['accountId']]))
            file.write('\n')
        except KeyError as e:
            print(e)
            continue


set_start()
