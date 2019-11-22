
from rest_framework import status
from rest_framework.decorators import api_view
# from api.models import Profile
# from api.serializers import ProfileSerializer
from rest_framework.response import Response
import requests

@api_view(['GET'])
def users(request):
    
    gameIds = []
    gameList = []
    api_key = "RGAPI-c1079d63-cde2-4305-89d1-fd3e4151988e"
    datas = {'userInfo':[],'matchList':[],'userProfile':[]}
    if request.method == 'GET':
        userId = request.GET.get('key',None)
        summoner_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(userId, api_key)
        user_profile = requests.get(summoner_url).json()
        id = user_profile['id']
        accountId = user_profile['accountId']
        puuid = user_profile['puuid']
        name = user_profile['name']
        profileIconId = user_profile['profileIconId']
        revisionDate = user_profile['revisionDate']
        summonerLevel = user_profile['summonerLevel']
        # 유저 정보 받기
        user_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}".format(id, api_key)
        request_user = requests.get(user_url).json() 
        # 유저 매치 정보들 받기
        findmatch_url = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?endIndex=3&beginIndex=0&api_key={}".format(accountId, api_key)
        request_findmatch = requests.get(findmatch_url).json()
        for i in request_findmatch['matches']:
            gameIds.append(i['gameId'])
        for i in gameIds:
            gameId = i
            match_url = "https://kr.api.riotgames.com/lol/match/v4/matches/{}?api_key={}".format(gameId, api_key)
            request_matchs = requests.get(match_url).json()
            gameList.append(request_matchs)
        datas['userInfo'] = request_user
        datas['matchList'] = gameList
        datas['userProfile'] = user_profile
        return Response(data=datas, status=status.HTTP_200_OK)

    
