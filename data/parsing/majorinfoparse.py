import requests
import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

url = "http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=18ce0465dc3e05e278bdc01fc6af4504&svcType=api&svcCode=MAJOR&contentType=json&gubun=univ_list&subject=100391"
file = open(f"majorinfo_{nowDate}.dat",'w',encoding='UTF8')
res = requests.get(url).json()

# 계열::세부학과명::학과코드::학과
for r in res['dataSearch']['content']:
    file.writelines('::'.join([r['lClass'],r['facilName'],r['majorSeq'],r['mClass']]))
    file.write('\n')