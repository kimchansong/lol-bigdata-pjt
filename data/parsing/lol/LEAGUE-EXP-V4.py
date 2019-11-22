import requests
import datetime
import time
now = datetime.datetime.now()
nowDate = 20190910

teer = ["CHALLENGER","GRANDMASTER","MASTER"]
teernum = ["I"]
file = open(f"LEAGUE-EXP-V4_{nowDate}.dat",'w',encoding='UTF8')
cnt =1

# teer = ["DIAMOND"]
# teernum = ["I", "II", "III", "IV"]

for t in teer:
    for tn in teernum:
        page =1
        while True :
            url = f"https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/{t}/{tn}?page={page}&api_key=RGAPI-c1079d63-cde2-4305-89d1-fd3e4151988e"
            page+=1
            cnt+=1
            res = requests.get(url).json()
            if res==[]:
                break
            if page%20==0:
                time.sleep(1)
            if cnt%100==0:
                time.sleep(120)
            print("---------------------------------------------------------------------------------",cnt)
            for r in res:
                print(r['summonerName'])
                print(r)
                leaguePoints = str(r['leaguePoints'])
                wins = str(r['wins'])
                losses = str(r['losses'])
                veteran = str(r['veteran'])
                inactive = str(r['inactive'])
                freshBlood = str(r['freshBlood'])
                hotStreak = str(r['hotStreak'])

                print(r['summonerName'])
                file.writelines('::'.join([r['summonerName'],r['tier'],r['rank'],r['summonerId'],r['leagueId'],leaguePoints,wins,losses,veteran,inactive,freshBlood,hotStreak]))
                file.write('\n')
            