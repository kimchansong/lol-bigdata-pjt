import requests
import time
import json

def set_findmatch(cnt, key):
    
    file = open(f"FINDMATCH-{key}.dat",'w',encoding='UTF8')
    file_dedug = open(f"FINDMATCH-{key}.dat",'w',encoding='UTF8')
    f1 = open(f"./SUMMONER-{key}.dat", 'r', encoding='UTF8')
    count = 0
    while True:
        try:
            line = f1.readline()
            if line == "":
                break
            accountId = line.split('::')[1]
            beginindex = 0
            endindex = 100
            while True:
                cnt+=1
                count+=1
                file_dedug.writelines(str(count))
                file_dedug.write('\n')
                if cnt%100 == 0:
                    time.sleep(120)
                beginidx = str(beginindex)
                endidx = str(endindex)
                url = f"https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}?queue=420&season=13&endIndex={endidx}&beginIndex={beginidx}&api_key={key}"
                url = url.replace('\n', "")
                r = requests.get(url).json()
                print(r['matches'])
                if r['matches'] == []:
                    break
                for v in range(len(r['matches'])):
                    file.writelines(str(r['matches'][v]["gameId"]))
                    file.write('\n')
                    
                beginindex+=100
                endindex+=100
        except KeyError as e:
            print(e)
            continue
    return cnt