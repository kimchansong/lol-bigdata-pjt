import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder
# 데이터읽기
with open(f"./MATCHS-RGAPI-9999047c-e9e4-4bf3-a231-ca24ccb79445.json", 'r', encoding='UTF8') as jsonfile:
    data =json.load(jsonfile)
# game 안에 데이터 접근
gamedata = data['game']

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

    print(data_team2)
    # first로 시작하는 변수는 T/F 값을 가지고 있어 인코딩 필요
    # 라벨링하기 !!!
    # True나 False 값이 6개
    # df = pd.data_team2

    # 왜안ㅇ돼??????????????????????????????????????????????
    # le = LabelEncoder()
    # df_encoded = data_team2.apply(le.fit_transform)
    # print(df_encoded)

    # data_team2.apply(LabelEncoder().fit_transform)
    # print(data_team2)
    # for i in range(0,6):
    #     le = LabelEncoder()
    #     # 0번째, 1번째 .. 5번째 열 뽑기
    #     y = list(data_team2.iloc[:,i])
    #     le.fit(y)
    #     print(le.classes_)
        # print(y)
        # fit 메서드를 실행하면 분포 모수를 객체내에 저장
        # fit(self, y) : Fit label encoder
        # le.fit(y)
        # print(y)
        # 학습용 데이터를 입력으로 하여 transform 메서드를 실행하면 학습용 데이터를 변환
        # transform(self, y) : Transform labels to normalized encoding.
        # y2 = le.transform(y)
        # print(le.classes_)
        # print(y2)
        # data_team.iloc[:,i] = y2
    for i in range(0,6):
        y = list(data_team2.iloc[:,i])
        if True in y:
            y2 = 1
        elif False in y:
            y2 = 0
        data_team.iloc[:,i+2] = y2
    print(data_team.iloc[0])
    break