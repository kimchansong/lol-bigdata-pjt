import requests
import time



def set_SUMMONER(cnt,key):
    file = open(f"SUMMONER-{key}.dat",'w',encoding='UTF8')
    f1 = open(f"./LEAGUE-EXP-V4_20190918.dat", 'r', encoding='UTF8')
    while True:
        try:
            line = f1.readline()
            if line == "":
                break
            cnt+=1
            if cnt%100 == 0:
                time.sleep(120)
            summonerName = line.split('::')[0]
            url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(summonerName,key)
            r = requests.get(url).json()
            print(r)
            file.writelines('::'.join([r['name'],r['accountId']]))
            file.write('\n')
        except KeyError as e:
            print(e)
            continue
    return cnt

