from MATCHS import * 
from FINDMATCH import * 
from SUMMONER import * 

cnt = 0
key = "RGAPI-9999047c-e9e4-4bf3-a231-ca24ccb79445"
cnt = set_SUMMONER(cnt,key)
cnt = set_findmatch(cnt,key)
cnt = set_start(cnt,key)
print("good")