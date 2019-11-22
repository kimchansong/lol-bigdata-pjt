import requests
from datetime import datetime

now = datetime.now()
nowDate = now.strftime('%Y%m%d')
file = open(f"ChampName_{nowDate}.dat",'w',encoding='UTF8')
url ="http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
res = requests.get(url).json()

for name in res['data']:
    file.write(name)
   # revisionDate = datetime.utcfromtimestamp(revision).strftime('%Y-%m-%d %H:%M')
   # file.writelines('::'.join([name]))
    file.write('\n')
file.close()
