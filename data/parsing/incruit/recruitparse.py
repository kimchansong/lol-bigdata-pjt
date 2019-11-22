import requests
from datetime import datetime

now = datetime.now()
nowDate = now.strftime('%Y%m%d')

url = "https://oapi.saramin.co.kr/job-search?access-key=IVp62SFJhpB4OER45uMYji85s6BwKjs2KrPD1p9LQPsAuyUauY5O&keyword=%EC%A7%81%EC%97%85&bbs_gb=0&stock=kospi+kosdaq+nasdaq&sr=directhire&job_type=&edu_lv=&fields=posting-date+expiration-date+keyword-code+count&start=1&count=110"
file = open(f"recruit_{nowDate}.dat",'w',encoding='UTF8')

# 요청 헤더 (Request Header) -> JSON로 응답 : application/json
headers = {'Accept':'application/json; charset=utf-8'}
res = requests.get(url=url, headers=headers).json()

# 공고진행여부, 기업명, 기업정보페이지, 공고제목, 공고링크, 업종코드, 지역코드, 근무형태코드, 업종키워드코드, 직종키워드코드, 경력코드, 경력정보, 학력코드, 키워드, 연봉코드, unique id, 접수시작일, 접수마감일, 마감일코드 
for j in res['jobs']['job']:

    act = str(j['active'])
    c_name = j['company']['detail']['name']

    if j['company']['detail'].get('href') is None:
        c_link = ''
    else: 
        c_link = j['company']['detail'].get('href')

    p_title = j['position']['title']
    p_ind_code = str(j['position']['industry'].get('code'))
    p_lc_code = str(j['position']['location'].get('code'))
    p_jt_code = str(j['position']['job-type'].get('code'))
    p_indkey_code = str(j['position'].get('industry-keyword-code'))
    p_jckw_code = str(j['position'].get('job-category-keyword-code'))
    p_xp_code = str(j['position']['experience-level'].get('code'))
    p_xp_name = j['position']['experience-level'].get('name')
    p_edu_code = str(j['position']['required-education-level'].get('code'))

    if j.get('keyword') is None:
        keyword = ''
    else: 
        keyword = j.get('keyword')

    salary = str(j['salary'].get('code'))
    open_date_ts = int(j['opening-timestamp'])
    print(open_date)
    open_date = datetime.utcfromtimestamp(open_date_ts).strftime('%Y-%m-%d %H:%M')
    exp_date_ts = int(j['expiration-timestamp'])
    exp_date = datetime.utcfromtimestamp(exp_date_ts).strftime('%Y-%m-%d %H:%M')

    if j.get('close_type') is None:
        close_type = ''
    else: 
        close_type = str(j['close_type'].get('code'))
    
    file.writelines('::'.join([act,c_name,c_link,p_title,j['url'],p_ind_code,p_lc_code,p_jt_code,p_indkey_code,p_jckw_code,p_xp_code,p_xp_name,p_edu_code,keyword,salary,j['id'],open_date,exp_date,close_type]))
    file.write('\n')