from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns
iris = open('./MATCH-V4_champ_lane_20190905.dat', 'r', encoding='ISO-8859-1')

# labels = pd.DataFrame(data=char)
# labels.columns=['labels']
data = pd.DataFrame(iris)
data.columns=['ID','Char_id','Lane']

print(data.head())

# feature = data[ ['Char_id','Lane']]
# print(feature.head())


# # 모형 객체를 생성.
# # train data를 가지고 모형 학습
# # data를 가지고 예측 (분류)
# #2.benign(양성), 4.malignant(악성)
 
# model = KMeans(n_clusters=6,algorithm='auto')
# model.fit(feature)
# predict = pd.DataFrame(model.predict(feature))
# predict.columns=['predict']

# # concatenate labels to df as a new column
# r = pd.concat([feature,predict],axis=1)

# print(r)

# centers = pd.DataFrame(model.cluster_centers_,columns=['Char_id','Lane'])
# center_x = centers['Char_id']
# center_y = centers['Lane']

# # scatter plot
# plt.scatter(r['Char_id'],r['Lane'],c=r['predict'],alpha=0.5)
# plt.scatter(center_x,center_y,s=50,marker='D',c='r')
# plt.show()
