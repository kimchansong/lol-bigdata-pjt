import requests
from roleml import roleml
match = "https://kr.api.riotgames.com/lol/match/v4/matches/3850889229?api_key=RGAPI-ec59e815-4e30-40b5-8a58-9b02c09bf47c"
timeline = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/3850889229?api_key=RGAPI-ec59e815-4e30-40b5-8a58-9b02c09bf47c"
match = requests.get(match).json()
timeline = requests.get(timeline).json()

print(roleml.predict(match, timeline))
test = roleml.predict(match, timeline)

for k,v in test.items():
    print(k,v)