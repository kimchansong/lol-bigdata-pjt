import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_users():
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    request_data = {'profiles': []}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }
    cnt = 0
    for line in user_data.readlines():
        cnt+=1
        if cnt<=16: 
            continue
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
        occupation = occupation_map[int(occupation)]

        request_data['profiles'].append({
            'username': username,
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

        # if len(request_data['profiles']) >= num_users:
        #     break

    response = requests.post(API_URL + 'auth/signup-many/', data=json.dumps(request_data), headers=headers)
    print(response.text)

def create_jobInformation(){
    information = open('./jobInfo_20190829.dat', 'r', encoding='UTF-8')
    
}

def create_movies():
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')

    # rate 데이터를 하나의 배열에 계속 어펜드 하면서 담아둔다.
    # 저장된 레이트 데이터를 가지고
    # 무비 데터를 생성할 때 사용한다.
    request_data1 = {'ratings': []}
    for line in rating_data.readlines():
        [username, movieid, rate, timestamp] = line.split('::')
        timestamp = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        request_data1['ratings'].append({
            'username': username,
            'movieid': movieid,
            'rate': rate,
            'time': timestamp
        })

    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    request_data = {'movies': []}
    for line in movie_data.readlines():
        cnt=0
        sum=0
        [id, title, genres] = line.split('::')
        for line1 in request_data1['ratings'] :
            if id==line1['movieid']:
                print(id)
                cnt+=1
                sum+=int(line1['rate'])
        if cnt==0:
            likes = 0
        else:
            likes = sum/cnt
        genres = genres[:-1].split('|')
        request_data['movies'].append({
            'id': id,
            'title': title,
            'genres': genres,
            'likes' : likes
        })

    response = requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)
    print(response.text)



def create_ratings(num_users):
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')
    request_data = {'ratings': []}
    cnt = 0
    for line in rating_data.readlines():
        [userid, movieid, rate, timestamp] = line.split('::')
        timestamp = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        username = 'user'+userid

        request_data['ratings'].append({
            'username': username,
            'movieid': movieid,
            'rate': rate,
            'time': timestamp
        })
    response = requests.post(API_URL + 'ratings/', data=json.dumps(request_data), headers=headers)
    print(response.text)

if __name__ == '__main__':
    # num_users = 15
    # create_movies()
    # create_users()
    # create_ratings(num_users)
    # create_movies1()
    create_jobInformation()
