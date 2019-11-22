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

# 데이터읽기
with open(f"./MATCHS-RGAPI-9999047c-e9e4-4bf3-a231-ca24ccb79445.json", 'r', encoding='UTF8') as jsonfile:
    data =json.load(jsonfile)
# game 안에 데이터 접근
gamedata = data['game']

game_train = pd.DataFrame()
game_test = pd.DataFrame()

dict_winner2 = {"Win" : 0, "Fail": 1}

# 리스트 돌리면서 데이터 확인!
for i in range(len(gamedata)):
    team1_df = pd.DataFrame()
    team2_df = pd.DataFrame()
    teamsdata = gamedata[i]['teams']
    try:
        # 'ban'이라는 키가 없으면 None을 반환
        teamsdata[0].pop('bans', None)

        # DataFrmae(data,columns=column_list,index=index_list)
        # 인덱스(teamId, win...), 데이터는 100,win,False...
        # DataFrame.T -> 행과 열을 뒤집는 것
        team1 = pd.DataFrame(list(teamsdata[0].values()),index = list(teamsdata[0].keys())).T

        # append -> 데이터프레임끼리 결합
        team1_df = team1_df.append(team1)

    except:
        # 에러발생 시 별도처리
        pass
    team1_df.index = range(len(team1_df))
    try:
        teamsdata[1].pop('bans',None)
        team2 = pd.DataFrame(list(teamsdata[1].values()),index = list(teamsdata[1].keys())).T
        team2_df = team2_df.append(team2)

    except:
        pass
    team2_df.index = range(len(team2_df))
    game_Duration = pd.DataFrame([gamedata[i]['gameDuration']],index=['gameDuration']).T


    # A팀의 정보만으로 이겼을 때와 졌을 대의 특성 알 수 있어서 A팀의 데이터만 사용
    data_team = pd.concat([team1_df,game_Duration],axis=1)

    # 결측값이 들어있는 행 전체(axis=0) 삭제
    data_team = data_team.dropna(axis=0)

    # list(data_team.columns)[2:] -> firstBlood부터 gameDuration까지 리스트
    data_team2 = data_team[list(data_team.columns)[2:]] # 팀이름, 승패 제외 나머지
    game_test = game_test.append(data_team)
    # print
    for i in range(0,6):
        y = list(data_team2.iloc[:,i])
        if True in y:
            y2 = 1
        elif False in y:
            y2 = 0
        data_team2.iloc[:,i] = y2
    
    game_train = game_train.append(data_team2)

# print(game_test)
# print(game_train)

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
plt.title("feature importance")
# barh 가로막대그리기, yerr 에러 바(error bar)를 추가
plt.barh(range(X_train.shape[1]),importances[indices],xerr=std[indices])
# plt.xticks(importances[indices]) # 플롯이나 차트에서 축상의 위치 표시 지점
plt.yticks(range(X_train.shape[1]),newhead)
# plt.xlim(0,1) # x축의 최소값과 최대값 지정
plt.show()

# print("--------------------------------")

# Gradient Boosting classifier
# 앙상블기법의 그래디언트 부스트 : 각 weaker model을 순차적으로 적용해가는 과정에서
# 잘못 분류된 샘플의 error를 optimization 하는 방식으로 진행
# gbc = GradientBoostingClassifier()
# gbc.fit(X_train,Y_train)

# _pred = gbc.predict(X_test)

# print("앙상블-부스팅")
# print('테스트 정확도 = ' + str(accuracy_score(Y_test,Y_pred)))
# print("--------------------------------")
# Xgboost

#xgb로 학습시키기 위해서는 dtypes이 단순하게 int형식이면 안된다. 따라서 데이터 형식을 float로 변환시켜줘야함
# X_train[['towerKills', 'inhibitorKills', 'baronKills', 'dragonKills', 'vilemawKills', 'riftHeraldKills', 'dominionVictoryScore', 'gameDuration']] = X_train[['towerKills', 'inhibitorKills', 'baronKills', 'dragonKills', 'vilemawKills', 'riftHeraldKills', 'dominionVictoryScore', 'gameDuration']].astype('float')

# #xgb로 학습시키기 위해서는 dtypes이 단순하게 int형식이면 안된다. 따라서 데이터 형식을 float로 변환시켜줘야함
# X_test[['towerKills', 'inhibitorKills', 'baronKills', 'dragonKills', 'vilemawKills', 'riftHeraldKills', 'dominionVictoryScore', 'gameDuration']] = X_test[['towerKills', 'inhibitorKills', 'baronKills', 'dragonKills', 'vilemawKills', 'riftHeraldKills', 'dominionVictoryScore', 'gameDuration']].astype('float')

# xgb_model = XGBClassifier()
# xgb_model.fit(X_train,Y_train)
# Y_pred = xgb_model.predict(X_test)
# print("Extreme Gredient Boosting")
# print('테스트 정확도 = ' + str(accuracy_score(Y_test,Y_pred)))#정확도 계산