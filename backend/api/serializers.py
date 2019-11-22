from .models import champion,gameResult,name_data, duodata, item_data3, Pickban, TeamData, itempick, Bancount3,naivedata

from rest_framework import serializers

class champion_serializers(serializers.ModelSerializer):

    class Meta:
        model = champion
        fields = ('id', 'key', 'name','title','blurb','attack','defense','magic','difficulty', 'tags','partype','hp','hpperlevel','mpperlevel','movespeed','armor','armorperlevel','spellblock','spellblockperlevel','attackrange','hpregen','hpregenperlevel','mpregen','mpregenperlevel','crit','critperlevel','attackdamage','attackdamageperlevel','attackspeedperlevel','attackspeed')
class item_serializers(serializers.ModelSerializer):

    class Meta:
        model = item_data3
        fields = ('id','char_id','item_id','item_cnt')

class gameResult_serializers(serializers.ModelSerializer):

    class Meta:
        model = gameResult
        fields = ('id','line','userId','championId','win','kills','death','assists')

class duodata_serializers(serializers.ModelSerializer):

    class Meta:
        model = duodata
        fields = ('id','Bot1','Bot2','Play')

class Pickban_serializers(serializers.ModelSerializer):

    class Meta:
        model = Pickban
        fields = ('id','name','pickcount','bancount')

class TeamData_serializers(serializers.ModelSerializer):

    class Meta:
        model = TeamData
        filed = ('id','gameduration','team1_Win','team1_firstBlood','team1_firstTower','team1_firstInhibitor','team1_firstBaron','team1_firstDragon','team1_firstRiftHerald',
        'team1_towerKills','team1_inhibitorKills','team1_baronKills','team1_dragonKills','team1_vilemawKills','team1_riftHeraldKills','team1_dominionVictoryScore',
        'team2_Win','team2_firstBlood','team2_firstTower','team2_firstInhibitor','team2_firstBaron','team2_firstDragon','team2_firstRiftHerald',
        'team2_towerKills','team2_inhibitorKills','team2_baronKills','team2_dragonKills','team2_vilemawKills','team2_riftHeraldKills','team2_dominionVictoryScore'
        )

class item_name_serializers(serializers.ModelSerializer):

    class Meta:
        model = name_data
        fields = ('id','name','key')

class itempick_serializers(serializers.ModelSerializer):

    class Meta:
        model = itempick
        fields = ('item_id','item_cnt')

class bancount_serializers(serializers.ModelSerializer):

    class Meta:
        model = Bancount3
        fields = ("id", "name", "char_id", "ban_char_id", "cnt")

class naive_data_serializers(serializers.ModelSerializer):

    class Meta:
        model = naivedata
        fields = ("id","Bot1","Bot2","Bot3","Bot4","Bot5","fBlood","fT","fD","fB","TK","DK","BK","Win","all")
