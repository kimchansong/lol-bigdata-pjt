%matplotlib as np
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
import json

style.use('seaborn-talk')
krfont = {'family':'NanumGothic','weight':'bold','size':10}
matplotlib.rc('font', **krfont)
matplotlib.reParams['axes.unicode_minus'] = False

# 데이터읽기
with open(f"./MATCHS-RGAPI-9999047c-e9e4-4bf3-a231-ca24ccb79445.json", 'r', encoding='UTF8') as jsonfile:
   data =json.load(jsonfile)
# game 안에 데이터 접근
data2 = data['game']
# 리스트 돌리면서 데이터 확인!
for i in range(len(data2)):
   for k,v in data2[i].items():
       if k == "teams":
           # print(v)
           # break
           pass
       elif k =="participants":
           print(v)
           break
           # print(k)
       elif k =="gameDuration":
           print(k)