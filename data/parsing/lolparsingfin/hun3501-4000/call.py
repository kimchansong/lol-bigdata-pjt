from MATCHS import * 
from FINDMATCH import * 
from SUMMONER import * 

cnt = 0
key = "RGAPI-1f69fa17-c243-4348-898a-5bcebbdfc92e"
cnt = set_SUMMONER(cnt,key)
cnt = set_findmatch(cnt,key)
cnt = set_start(cnt,key)
print("good")