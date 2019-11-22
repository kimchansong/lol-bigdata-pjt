import pandas as pd
request_data ={'lols' : {}}

sum_data = {'top':{}, 'mid':{2}, 'botoom':[3]}
for k,v in sum_data.items():
    # print(k,v)
    request_data['lols'][k] = v 

print(request_data)

# request_data ={'lols' : {}}

# df = pd.DataFrame(request_data)
# print(df)

# top = {'char_id':[], 'name':[], 'count':[], 'attackrange':[]}
# jug = {'char_id':[], 'name':[], 'count':[], 'attackrange':[]}
# mid = {'char_id':[], 'name':[], 'count':[], 'attackrange':[]}
# bottom = {'char_id':[], 'name':[], 'count':[], 'attackrange':[]}
# none = {'char_id':[], 'name':[], 'count':[], 'attackrange':[]}