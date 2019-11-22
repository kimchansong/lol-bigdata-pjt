from MATCHS import * 
from FINDMATCH import * 
from SUMMONER import * 

cnt = 0
key = "RGAPI-c0655252-3b8e-4d72-8494-729ed8a3d16d"
cnt = set_SUMMONER(cnt,key)
cnt = set_findmatch(cnt,key)
cnt = set_start(cnt,key)
print("good")