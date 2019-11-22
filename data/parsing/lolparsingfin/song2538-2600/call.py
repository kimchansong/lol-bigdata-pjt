from MATCHS import * 
from FINDMATCH import * 
from SUMMONER import * 

cnt = 0
key = "RGAPI-c1079d63-cde2-4305-89d1-fd3e4151988e"
cnt = set_SUMMONER(cnt,key)
cnt = set_findmatch(cnt,key)
cnt = set_start(cnt,key)
print("good")