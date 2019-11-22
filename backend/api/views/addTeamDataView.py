from rest_framework import status
from rest_framework.decorators import api_view
from api.models import champion, gameResult, TeamData
from api.serializers import TeamData_serializers
from rest_framework.response import Response
import time

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
        return Response(status=status.HTTP_200_OK)
    if request.method == 'POST':
        result = request.data.get('gameResult', None)

        if gameResult!= None:
            insertgameResult(result)

        # print(champion)
        return Response(status=status.HTTP_200_OK)

def insertgameResult(result):
    for i in range(len(result)):
        gameduration = result[i]['gameDuration']
        team1_Win = result[i]['0']['win']
        team1_firstBlood = result[i]['0']['firstBlood']
        team1_firstTower = result[i]['0']['firstTower']
        team1_firstInhibitor = result[i]['0']['firstInhibitor']
        team1_firstBaron = result[i]['0']['firstBaron']
        team1_firstDragon = result[i]['0']['firstDragon']
        team1_firstRiftHerald = result[i]['0']['firstRiftHerald']
        team1_towerKills = result[i]['0']['towerKills']
        team1_inhibitorKills = result[i]['0']['inhibitorKills']
        team1_baronKills = result[i]['0']['baronKills']
        team1_dragonKills = result[i]['0']['dragonKills']
        team1_vilemawKills = result[i]['0']['vilemawKills']
        team1_riftHeraldKills = result[i]['0']['riftHeraldKills']
        team1_dominionVictoryScore = result[i]['0']['dominionVictoryScore']
        team2_Win = result[i]['1']['win']
        team2_firstBlood = result[i]['1']['firstBlood']
        team2_firstTower = result[i]['1']['firstTower']
        team2_firstInhibitor = result[i]['1']['firstInhibitor']
        team2_firstBaron = result[i]['1']['firstBaron']
        team2_firstDragon = result[i]['1']['firstDragon']
        team2_firstRiftHerald = result[i]['1']['firstRiftHerald']
        team2_towerKills = result[i]['1']['towerKills']
        team2_inhibitorKills = result[i]['1']['inhibitorKills']
        team2_baronKills = result[i]['1']['baronKills']
        team2_dragonKills = result[i]['1']['dragonKills']
        team2_vilemawKills = result[i]['1']['vilemawKills']
        team2_riftHeraldKills = result[i]['1']['riftHeraldKills']
        team2_dominionVictoryScore = result[i]['1']['dominionVictoryScore']
        TeamData(gameduration=gameduration,team1_Win=team1_Win, team1_firstBlood = team1_firstBlood , team1_firstTower=team1_firstTower, team1_firstInhibitor=team1_firstInhibitor, team1_firstBaron = team1_firstBaron,
        team1_firstDragon = team1_firstDragon, team1_firstRiftHerald = team1_firstRiftHerald,team1_towerKills=team1_towerKills,team1_inhibitorKills=team1_inhibitorKills,
        team1_baronKills=team1_baronKills,team1_dragonKills=team1_dragonKills,team1_vilemawKills=team1_vilemawKills,team1_riftHeraldKills=team1_riftHeraldKills,team1_dominionVictoryScore=team1_dominionVictoryScore,
        team2_Win=team2_Win, team2_firstBlood = team2_firstBlood , team2_firstTower=team2_firstTower, team2_firstInhibitor=team2_firstInhibitor, team2_firstBaron = team2_firstBaron,
        team2_firstDragon = team2_firstDragon, team2_firstRiftHerald = team2_firstRiftHerald,team2_towerKills=team2_towerKills,team2_inhibitorKills=team2_inhibitorKills,
        team2_baronKills=team2_baronKills,team2_dragonKills=team2_dragonKills,team2_vilemawKills=team2_vilemawKills,team2_riftHeraldKills=team2_riftHeraldKills,team2_dominionVictoryScore=team2_dominionVictoryScore
        ).save()
