import requests
from bs4 import BeautifulSoup

url = "https://oapi.saramin.co.kr/guide/code-table1"

res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')

work_picks = soup.select('#jobTypeCode > table.tbl > tbody > tr > td')

work_type = {}

for i in range(0,len(work_picks),2):
    idx = work_picks[i].text
    work_type[idx] = work_picks[i+1].text

edu_picks = soup.select('#educationLevelCode > table.tbl > tbody > tr > td')

edu_type = {}

for i in range(0,len(edu_picks),2):
    idx = edu_picks[i].text
    edu_type[idx] = edu_picks[i+1].text

salary_picks = soup.select('#salaryCode > table.tbl > tbody > tr > td')

salary_type = {}

for i in range(0,len(salary_picks),2):
    idx = salary_picks[i].text
    salary_type[idx] = salary_picks[i+1].text


print(salary_type)