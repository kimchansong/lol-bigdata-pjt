from rest_framework import status
from rest_framework.decorators import api_view
from api.models import champion, gameResult
from api.serializers import champion_serializers, gameResult_serializers
from rest_framework.response import Response

from sklearn import datasets
from sklearn.cluster import KMeans
from operator import itemgetter
from sklearn.metrics import pairwise_distances_argmin
# import api_view
import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sb
import time
# import surprise

@api_view(['GET','POST'])
def champion_data(request):
    if request.method == 'GET':
        gameResults = gameResult.objects.all()
        gameResultsUser = gameResults.values("userId")
        gameResultsGame = gameResults.values("championId")
        
        for i in gameResultsUser:
            Results = gameResult.objects.all()    
            Results = Results.filter(userId=i['userId'])
            for i in gameResultsGame:
                Results = Results.filter(championId=i['championId'])
            print(Results)
            time.sleep(3)
        # gameResultstest = gameResult.order_by("userId")
        # print(gameResults)
        
        
        #1챔피언 승률

        #2kda


        # df  = pd.DataFrame(gameResults, columns=["id","userId","championId","win","kills","death","assists"])

        return Response(status=status.HTTP_200_OK)
    if request.method == 'POST':
        # numbers = ['one', 'two', 'three', 'four', 'five']
    
        # for i,n in enumerate(numbers):
        #     print(numbers[i])

        chamipons = request.data.get('champion', None)
        userDB = request.data.get('user', None)
        # print(type(chamipons))
        # print(chamipons)
        if chamipons != None:
            insertChampion(chamipons)
        if userDB != None:
            insertGameResult(userDB)

        # print(champion)
        return Response(status=status.HTTP_200_OK)

def insertGameResult(userDB):
    for i in range(len(userDB['top']['championId'])):
        for j in userDB.keys():
            userId = userDB[j]['userId'][i]
            championId = userDB[j]['championId'][i]
            win = userDB[j]['win'][i]
            kills = userDB[j]['kills'][i]
            death = userDB[j]['death'][i]
            assists = userDB[j]['assists'][i]
        gameResult(userId=userId, line = j , championId=championId, win=win, kills = kills, death = death, assists = assists).save()
    

def insertChampion(chamipons):
    for i,v in enumerate(chamipons):
            id = chamipons[i]['id']
            key = chamipons[i]['key']
            name = chamipons[i]['name']
            title = chamipons[i]['title']
            blurb = chamipons[i]['blurb']
            attack = chamipons[i]['attack']
            defense = chamipons[i]['defense']
            magic = chamipons[i]['magic']
            difficulty = chamipons[i]['difficulty']
            tags = chamipons[i]['tags']
            partype = chamipons[i]['partype']
            hp = chamipons[i]['hp']
            hpperlevel = chamipons[i]['hpperlevel']
            mpperlevel = chamipons[i]['mpperlevel']
            movespeed = chamipons[i]['movespeed']
            armor = chamipons[i]['armor']
            armorperlevel = chamipons[i]['armorperlevel']
            spellblock = chamipons[i]['spellblock']
            spellblockperlevel = chamipons[i]['spellblockperlevel']
            attackrange = chamipons[i]['attackrange']
            hpregen = chamipons[i]['hpregen']
            hpregenperlevel = chamipons[i]['hpregenperlevel']
            mpregen = chamipons[i]['mpregen']
            mpregenperlevel = chamipons[i]['mpregenperlevel']
            crit = chamipons[i]['crit']
            critperlevel = chamipons[i]['critperlevel']
            attackdamage = chamipons[i]['attackdamage']
            attackdamageperlevel = chamipons[i]['attackdamageperlevel']
            attackspeedperlevel = chamipons[i]['attackspeedperlevel']
            attackspeed = chamipons[i]['attackspeed']

            champion(id=id, key=key, name=name, title=title, blurb= blurb, attack= attack, defense= defense, magic= magic, difficulty= difficulty,
            tags= tags,partype= partype,hp= hp,hpperlevel= hpperlevel,mpperlevel= mpperlevel,movespeed= movespeed,armor= armor,armorperlevel= armorperlevel,
            spellblock= spellblock,spellblockperlevel= spellblockperlevel,attackrange= attackrange,hpregen= hpregen,hpregenperlevel= hpregenperlevel,
            mpregen= mpregen,mpregenperlevel= mpregenperlevel,crit= crit,critperlevel= critperlevel,attackdamage= attackdamage,attackdamageperlevel=attackdamageperlevel,
            attackspeedperlevel=attackspeedperlevel,attackspeed=attackspeed).save()