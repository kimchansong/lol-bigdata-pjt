import requests
import time
import json


def set_start(cnt,key):
    with open(f"MATCHS-{key}.json",'w',encoding='UTF8') as outfile:
        f1 = open(f"./FINDMATCH-{key}.dat", 'r', encoding='UTF8')
        test = {'game':[]}
        while True:
            try:
                matchId = f1.readline()
                if matchId == "":
                    break
                print("_________________________________________")
                print(cnt)
                cnt+=1
                if cnt%100 == 0:
                    time.sleep(120)
                matchId = int(matchId)
                url = "https://kr.api.riotgames.com/lol/match/v4/matches/{}?api_key={}".format(matchId,key)
                r = requests.get(url).json()
                test['game'].append(r)
            except KeyError as e:
                print(e)
                continue
        json.dump(test, outfile,indent="\t")
        set_next(cnt,key)
def set_next(cnt,key):
    with open(f"TIMELINE-{key}.json",'w',encoding='UTF8') as outfile:
        f1 = open(f"./FINDMATCH-{key}.dat", 'r', encoding='UTF8')
        test = {'timeline':[]}
        while True:
            try:
                matchId = f1.readline()
                if matchId == "":
                    break;
                cnt+=1
                if cnt%100 == 0:
                    time.sleep(120)
                matchId = int(matchId)
                key = "RGAPI-c1079d63-cde2-4305-89d1-fd3e4151988e"
                url = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/{}?api_key={}".format(matchId,key)
                r = requests.get(url).json()
                test['timeline'].append(r)
            except KeyError as e:
                print(e)
                continue
        json.dump(test, outfile,indent="\t")
        return cnt



