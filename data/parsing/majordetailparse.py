import requests
import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

url = "http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=bd27b34d36bb7f9852ba8ff9f68ac521&svcType=api&svcCode=MAJOR_VIEW&contentType=json&gubun=univ_list&majorSeq=29"
file = open(f"majordetail_{nowDate}.dat",'w',encoding='UTF8')
res = requests.get(url).json()

r = res['dataSearch']['content'][0]

# 졸업 후 진출분야
enter_field = []
for g in r['enter_field']:
    enter_field.append([g['gradeuate'],g['description']])
enterfield=''
for i in range(len(enter_field)):
    if i == len(enter_field)-1:
        enterfield += enter_field[i][0]+'|'+enter_field[i][1]
    else:
        enterfield += enter_field[i][0]+'|'+enter_field[i][1]+"||"

# 개설 대학
university = []
for u in r['university']:
    university.append([u['schoolName'],u['campus_nm'],u['majorName']])
univ=''
for i in range(len(university)):
    if i == len(university)-1:
        univ += university[i][0]+'|'+university[i][1]+'|'+university[i][2]
    else:
        univ += university[i][0]+'|'+university[i][1]+'|'+university[i][2]+"||"

# 학과 남녀 성비
gender = []
for g in r['chartData'][0]['gender']:
    gender.append([g['item'],g['data']])
gen=''
for i in range(len(gender)):
    if i == len(gender)-1:
        gen += gender[i][0]+'|'+gender[i][1]
    else:
        gen += gender[i][0]+'|'+gender[i][1]+"||"

# 주요교과목
main_subject = []
for g in r['main_subject']:
    main_subject.append([g['SBJECT_NM'],g['SBJECT_SUMRY']])
subject=''
for i in range(len(main_subject)):
    if i == len(main_subject)-1:
        subject += main_subject[i][0]+'|'+main_subject[i][1]
    else:
        subject += main_subject[i][0]+'|'+main_subject[i][1]+"||"

# 성별 취업률
employment_rate = []
for g in r['chartData'][0]['employment_rate']:
    employment_rate.append([g['item'],g['data']])
employrate=''
for i in range(len(employment_rate)):
    if i == len(main_subject)-1:
        employrate += employment_rate[i][0]+'|'+employment_rate[i][1]
    else:
        employrate += employment_rate[i][0]+'|'+employment_rate[i][1]+"||"

# 졸업 후 상황
after_graduation = []
for g in r['chartData'][0]['after_graduation']:
    after_graduation.append([g['item'],g['data']])
aftergraduation=''
for i in range(len(after_graduation)):
    if i == len(after_graduation)-1:
        aftergraduation += after_graduation[i][0]+'|'+after_graduation[i][1]
    else:
        aftergraduation += after_graduation[i][0]+'|'+after_graduation[i][1]+"||"

# 졸업 후 첫직장 평균임금
avg_salary = []
for g in r['chartData'][0]['avg_salary']:
    avg_salary.append([g['item'],g['data']])
salary=''
for i in range(len(avg_salary)):
    if i == len(avg_salary)-1:
        salary += avg_salary[i][0]+'|'+avg_salary[i][1]
    else:
        salary += avg_salary[i][0]+'|'+avg_salary[i][1]+"||"

interest=r['interest'].splitlines()[0]
proper=r['property'].splitlines()[0]

file.writelines('::'.join([r['major'],r['summary'],enterfield,r['job'],univ,gen,subject,employrate,r['qualifications'],aftergraduation,salary,interest,proper,r['department']]))
file.write('\n')