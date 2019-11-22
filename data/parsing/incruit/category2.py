import requests
from bs4 import BeautifulSoup

url = "https://oapi.saramin.co.kr/guide/code-table2"

res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')

mid_picks = soup.select('#midCodelist > table.tbl > tbody > tr > td')

location_mid = {}

for i in range(0,len(mid_picks),2):
    idx = mid_picks[i].text
    location_mid[idx] = mid_picks[i+1].text

bot_picks = soup.select('#botCodelist > table.tbl > tbody > tr > td')

location_bot = {}

for i in range(0,len(bot_picks),2):
    idx = bot_picks[i].text
    location_bot[idx] = bot_picks[i+1].text

# print(location_bot)

location_dict = {}

# for lkey, lval in location_mid.items():
#     for key, val in location_bot.items():
#         if key[:3]==lkey[:3]:
#             loaction_dict[lkey]
