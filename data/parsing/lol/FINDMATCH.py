import requests
import threading
import time
import random
from datetime import datetime
import cassiopeia as cass
now = datetime.now()
nowDate = now.strftime('%Y%m%d')
file = open(f"FINDMATCH-_{nowDate}.dat",'w',encoding='UTF8')
f1 = open("./SUMMONER-_20190919.dat", 'r', encoding='UTF8')


def set_start():
    # cass.set_riot_api_key("RGAPI-c1079d63-cde2-4305-89d1-fd3e4151988e")
    # cass.set_default_region("KR")
    # summoner = cass.get_summoner(name="중소기업김대표")
    # print(summoner.account_id)
    # print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
    #                                                                       level=summoner.level,
    #                                                                       region=summoner.region))
    cnt = 1
    while True:
        try:
            line = f1.readline()
            if line == "":
                break;
            cnt+=1
            if cnt%100 == 0:
                time.sleep(120)
            accountId = line.split('::')[1]
            beginindex = 0
            endindex = 100
            key = "RGAPI-c1079d63-cde2-4305-89d1-fd3e4151988e"
            while True:
                beginidx = str(beginindex)
                endidx = str(endindex)
                url = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?queue=420&season=13&endIndex={}&beginIndex={}&api_key={}".format(accountId,endidx,beginidx,key)
                print(url)
                r = requests.get(url).json()
                print(r)
                break;
                if r['status']['matches'] == []:
                    break;
                print("here")
                print(r['status']['matches'])
                # file.writelines('::'.join([r['name'],r['accountId']]))
                # file.write('\n')
                beginindex+=100
                endindex+=100
        except KeyError as e:
            print(e)
            continue


set_start()
