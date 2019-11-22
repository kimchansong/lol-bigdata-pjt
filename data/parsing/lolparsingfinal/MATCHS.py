import requests
import time
import json


def set_start(cnt,key):
    with open(f"MATCHS-{cnt}.json",'w',encoding='UTF8') as outfile:
        f1 = open(f"./FINDMATCH.dat", 'r', encoding='UTF8')
        test = {'game':[]}
        check = {}
        count = 0
        tmp = key[:]
        keyIdx = 0
        while True:
            try:
                while count<cnt:
                    matchId = f1.readline()
                    count += 1
                matchId = f1.readline()
                if matchId == "":
                    break
                count +=1
                if matchId in check.keys():
                    continue
                else:
                    check[matchId] = matchId
                cnt+=1
                matchId = int(matchId)
                url = "https://kr.api.riotgames.com/lol/match/v4/matches/{}?api_key={}".format(matchId,tmp[keyIdx])
                r = requests.get(url)
                while str(r)!="<Response [200]>":
                    keyIdx +=1
                    keyIdx %=3
                    url = "https://kr.api.riotgames.com/lol/match/v4/matches/{}?api_key={}".format(matchId,tmp[keyIdx])
                    r = requests.get(url)
                r = r.json()
                print(cnt)
                test['game'].append(r)
                if cnt%1000==0:
                    json.dump(test, outfile,indent="\t")
                    set_start(cnt,key)
                    return cnt
            except KeyError as e:
                print(e)
                continue
        json.dump(test, outfile,indent="\t")
def set_next(cnt,key):

    with open(f"TIMELINE-{cnt}.json",'w',encoding='UTF8') as outfile:
        f1 = open(f"./FINDMATCH.dat", 'r', encoding='UTF8')
        f2 = open(f"./FINDMATCH-next-debug.dat", 'w', encoding='UTF8')
        test = {'timeline':[]}
        check = {}
        count = 0
        tmp = key[:]
        keyIdx = 0
        while True:
            try:
                while count<cnt:
                    matchId = f1.readline()
                    count += 1
                matchId = f1.readline()
                if matchId == "":
                    break
                if matchId in check.keys():
                    continue
                else:
                    check[matchId] = matchId
                cnt+=1
                matchId = int(matchId)
                url = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/{}?api_key={}".format(matchId,tmp[keyIdx])
                r = requests.get(url)
                while str(r)!="<Response [200]>":
                    keyIdx +=1
                    keyIdx %=3
                    url = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/{}?api_key={}".format(matchId,tmp[keyIdx])
                    r = requests.get(url)
                r = r.json()
                print(cnt)
                test['timeline'].append(r)
                if cnt%1000==0:
                    json.dump(test, outfile,indent="\t")
                    set_next(cnt,key)
                    return cnt
            except KeyError as e:
                print("error!")
                print(e)
                continue
        json.dump(test, outfile,indent="\t")
        return cnt



