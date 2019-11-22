from rest_framework import status
from rest_framework.decorators import api_view
from api.models import TeamData
from api.serializers import TeamData_serializers
from rest_framework.response import Response

import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sb

@api_view(['GET', 'POST', 'DELETE'])
def win_variable(request):
    if request.method == 'GET':
        teamdata = TeamData.objects.all()
        game_train = pd.DataFrame(columns=("firstBlood", "firstTower", "firstInhibitor","firstBaron","firstDragon","firstRiftHerald","towerKills","inhibitorKills","baronKills","dragonKills","riftHeraldKills"))
        game_test = pd.DataFrame(columns=("win","firstBlood", "firstTower", "firstInhibitor","firstBaron","firstDragon","firstRiftHerald","towerKills","inhibitorKills","baronKills","dragonKills","riftHeraldKills"))
        dict_winner2 = {"Win" : 0, "Fail": 1}
        cnt = 0
        for i in teamdata:
            if cnt == 1000:
                break
            game_train.loc[cnt] = [i.team1_firstBlood,i.team1_firstTower,i.team1_firstInhibitor,i.team1_firstBaron,i.team1_firstDragon,i.team1_firstRiftHerald,i.team1_towerKills,i.team1_inhibitorKills,i.team1_baronKills,i.team1_dragonKills,i.team1_riftHeraldKills]
            game_test.loc[cnt] = [i.team1_Win,i.team1_firstBlood,i.team1_firstTower,i.team1_firstInhibitor,i.team1_firstBaron,i.team1_firstDragon,i.team1_firstRiftHerald,i.team1_towerKills,i.team1_inhibitorKills,i.team1_baronKills,i.team1_dragonKills,i.team1_riftHeraldKills]
            cnt += 1

        # np.array : 배열생성
        # data_team['win'].map(dict_winner2) 이면 data_team['win'] 데이터에서 Dict 안에 키랑 밸류로 값을 바꿔줌
        # a.tolist() is almost the same as list(a)

        # 데이터를 train과 test로 나누기
        # X:DATA, Y:LABLE
        X_train, X_test, Y_train, Y_test = train_test_split(game_train, np.array(game_test['win'].map(dict_winner2).tolist()), test_size=0.25, stratify=np.array(game_test['win'].map(dict_winner2).tolist()), random_state=123456)
        print("--------------------------------")

        # Random forest 학습
        # n_estimators : 생성할 tree의 개수와
        # oob_score = out of bag score로써 예측이 얼마나 정확한가에 대한 추정치
        # BaggingClassifier의 인자인 oob_score=True로 설정하면 학습이 끝난 후 자동으로 oob 평가를 할 수 있음.

        rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
        rf.fit(X_train, Y_train) #소환사 코드를 float로 바꿔줘야함

        predicted = rf.predict(X_test)
        accuracy = accuracy_score(Y_test, predicted)

        importances = rf.feature_importances_
        std = np.std([tree.feature_importances_ for tree in rf.estimators_],axis=0)
        indices = np.argsort(importances)
        head = list(game_train.columns)
        newhead = []
        for i in indices:
            newhead.append(head[i])
        print("Random forest")
        print(f'Out-of-bag score estimate: {rf.oob_score_:.3}')
        print(f'Mean accuracy score: {accuracy:.3}')
        # plt.title("feature importance911111111111111111111111")
        # # barh 가로막대그리기, yerr 에러 바(error bar)를 추가
        # plt.barh(range(X_train.shape[1]),importances[indices],xerr=std[indices])
        # # plt.xticks(importances[indices]) # 플롯이나 차트에서 축상의 위치 표시 지점
        # plt.yticks(range(X_train.shape[1]),newhead)
        # # plt.xlim(0,1) # x축의 최소값과 최대값
        # plt.show()
        # datas['predicted'] = predicted

        datas = {'accuracy':[],'importances':[],'std':[],'newhead':[],"X_train":[]}
        datas['accuracy'] = accuracy
        datas['importances'] = importances[indices]
        datas['std'] = std[indices]
        datas['newhead'] = newhead
        datas['X_train'] = X_train.shape[1]
        print(datas)

        return Response(data=datas,status=status.HTTP_200_OK)
