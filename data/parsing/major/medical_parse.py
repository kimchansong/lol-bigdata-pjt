# 의학계열 학과정보(36개)

import requests
import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

# subject=100396
classurl = "http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=bd27b34d36bb7f9852ba8ff9f68ac521&svcType=api&svcCode=MAJOR&contentType=json&gubun=univ_list&subject=100396&thisPage=1&perPage=600"

classres = requests.get(classurl).json()
classr = classres['dataSearch']['content']
majorlist = []
for c in classr:
    majorlist.append(int(c['majorSeq']))

file = open(f"medical_major_{nowDate}.dat",'w',encoding='UTF8')

# 학과명, 학과개요, 졸업 후 진출분야(진출분야명,진출분야설명), 관련직업, 개설대학(학교명, 캠퍼스명,전공명), 학과 남녀 성비, 주요 교과목, 성별 취업률, 관련자격증, 졸업 후 상황, 졸업 후 첫 직장 평균임금, 흥미적성, 학과특성, 학과세부

for major in majorlist:
    url = f"http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=bd27b34d36bb7f9852ba8ff9f68ac521&svcType=api&svcCode=MAJOR_VIEW&contentType=json&gubun=univ_list&majorSeq={major}"
    res = requests.get(url).json()
    print(major)
    r = res['dataSearch']['content'][0]

    # 학과 개요
    if r['summary'] is None:
        summary = ''
    else: 
        summary = r['summary'].splitlines()[0]

    # 졸업 후 진출분야
    enter_field = []
    if r.get('enter_field') is not None: 
        for g in r['enter_field']:
            if g['description'] is not None:
                description = g['description'].splitlines()[0]
                enter_field.append([g['gradeuate'],description])
    enterfield=''
    for i in range(len(enter_field)):
        if enter_field[i][0] is None:
            enter_field[i][0]=''
        if enter_field[i][1] is None:
            enter_field[i][1]=''
        if i == len(enter_field)-1:
            enterfield += enter_field[i][0]+'$'+enter_field[i][1]
        else:
            enterfield += enter_field[i][0]+'$'+enter_field[i][1]+"|"

    # 개설 대학
    university = []
    if r.get('university') is not None:
        for u in r['university']:
            university.append([u['schoolName'],u['campus_nm'],u['majorName']])
    univ=''
    for i in range(len(university)):
        if university[i][0] is None:
            university[i][0]=''
        if university[i][1] is None:
            university[i][1]=''
        if university[i][2] is None:
            university[i][2]=''
        if i == len(university)-1:
            univ += university[i][0]+'$'+university[i][1]+'$'+university[i][2]
        else:
            univ += university[i][0]+'$'+university[i][1]+'$'+university[i][2]+"|"

    # 학과 남녀 성비
    gender = []
    if r['chartData'][0].get('gender') is not None:
        for g in r['chartData'][0]['gender']:
            gender.append([g['item'],g['data']])
    gen=''
    for i in range(len(gender)):
        if gender[i][0] is None:
            gender[i][0]=''
        if gender[i][1] is None:
            gender[i][1]=''
        if i == len(gender)-1:
            gen += gender[i][0]+'$'+gender[i][1]
        else:
            gen += gender[i][0]+'$'+gender[i][1]+"|"

    # 주요교과목
    main_subject = []
    if r.get('main_subject') is not None:
        for g in r['main_subject']:
            if g['SBJECT_SUMRY'] is not None:
                sbject_summary = g['SBJECT_SUMRY'].splitlines()[0]
                main_subject.append([g['SBJECT_NM'],sbject_summary])
    subject=''
    for i in range(len(main_subject)):
        if main_subject[i][0] is None:
            main_subject[i][0]=''
        if main_subject[i][1] is None:
            main_subject[i][1]=''
        if i == len(main_subject)-1:
            subject += main_subject[i][0]+'$'+main_subject[i][1]
        else:
            subject += main_subject[i][0]+'$'+main_subject[i][1]+"|"

    # 성별 취업률
    employment_rate = []
    if r['chartData'][0].get('employment_rate') is not None:
        for g in r['chartData'][0]['employment_rate']:
            employment_rate.append([g['item'],g['data']])
    employrate=''
    for i in range(len(employment_rate)):
        if employment_rate[i][0] is None:
            employment_rate[i][0]=''
        if employment_rate[i][1] is None:
            employment_rate[i][1]=''
        if i == len(main_subject)-1:
            employrate += employment_rate[i][0]+'$'+employment_rate[i][1]
        else:
            employrate += employment_rate[i][0]+'$'+employment_rate[i][1]+"|"

    # 졸업 후 상황
    after_graduation = []
    if r['chartData'][0].get('after_graduation') is not None:
        for g in r['chartData'][0].get('after_graduation'):
            after_graduation.append([g.get('item'),g.get('data')])
    aftergraduation=''
    for i in range(len(after_graduation)):
        if after_graduation[i][0] is None:
            after_graduation[i][0]=''
        if after_graduation[i][1] is None:
            after_graduation[i][1]=''
        if i == len(after_graduation)-1:
            aftergraduation += after_graduation[i][0]+'$'+after_graduation[i][1]
        else:
            aftergraduation += after_graduation[i][0]+'$'+after_graduation[i][1]+"|"

    # 졸업 후 첫직장 평균임금
    avg_salary = []
    if r['chartData'][0].get('avg_salary') is not None:
        for g in r['chartData'][0]['avg_salary']:
            avg_salary.append([g['item'],g['data']])
    salary=''
    for i in range(len(avg_salary)):
        if avg_salary[i][0] is None:
            avg_salary[i][0]=''
        if avg_salary[i][1] is None:
            avg_salary[i][1]=''
        if i == len(avg_salary)-1:
            salary += avg_salary[i][0]+'$'+avg_salary[i][1]
        else:
            salary += avg_salary[i][0]+'$'+avg_salary[i][1]+"|"

    if r.get('interest') is None:
        interest = ''
    else:
        interest=r['interest'].splitlines()[0]
    if r.get('property') is None:
        proper = ''
    else:
        proper=r['property'].splitlines()[0]

    if r.get('major') is None:
        r['major'] = ''
    if r.get('job') is None:
        r['job'] = ''
    if r.get('qualifications') is None:
        r['qualifications'] = ''
    if r.get('department') is None:
        r['department'] = ''

    file.writelines('::'.join([r['major'],summary,enterfield,r['job'],univ,gen,subject,employrate,r['qualifications'],aftergraduation,salary,interest,proper,r['department']]))
    file.write('\n')