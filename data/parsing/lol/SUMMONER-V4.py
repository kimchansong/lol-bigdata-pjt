import requests
import threading

from datetime import datetime
now = datetime.now()
nowDate = now.strftime('%Y%m%d')
file = open(f"SUMMONER-V4_{nowDate}.dat",'w',encoding='UTF8')
f = open("C:/Users/multicampus/bigdataproject/bigdata-sub2/data/parsing/lol/LEAGUE-EXP-V4_20190904.dat", 'r', encoding='UTF8')


def set_start():
   line = f.readline()
   summonerId = line.split('::')[4]

   key = "RGAPI-5f9df09e-de01-47fb-9253-092b297545f5"
   url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/{}?api_key={}".format(summonerId,key)
   r = requests.get(url).json()
   if r.get('id') is None:
       id = ''
   else:
       id = r['id']
   if r.get('accountId') is None:
       accountId = ''
   else:
       accountId = r['accountId']
   if r.get('puuid') is None:
       puuid = ''
   else:
       puuid = r['puuid']
   if r.get('name') is None:
       name = ''
   else:
       name = r['name']
   if r.get('profileIconId') is None:
       profileIconId = ''
   else:
       profileIconId = str(r['profileIconId'])
   if r.get('summonerLevel') is None:
       summonerLevel = ''
   else:
       summonerLevel = str(r['summonerLevel'])
   if r.get('revisionDate') is None:
       revisionDate = ''
   else:
       revisionDate =  str(r['revisionDate'])
#    revisionDate = datetime.utcfromtimestamp(revision).strftime('%Y-%m-%d %H:%M')
   file.writelines('::'.join([id,accountId,puuid,name,profileIconId,revisionDate,summonerLevel]))
   file.write('\n')
   print("파씽진행중")
   threading.Timer(1, set_start).start()

set_start()
