import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create():
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

def create_champion():
    with open('./champion_kr.json', 'r', encoding='UTF8') as json_file:
        data = json.load(json_file)
        request_data = {'champion' : []}
        for k in data['data'].keys():
            id = data['data'][k]['id']
            key = data['data'][k]['key']
            name = data['data'][k]['name']
            title = data['data'][k]['title']
            blurb = data['data'][k]['blurb']
            attack = data['data'][k]['info']['attack']
            defense = data['data'][k]['info']['defense']
            magic = data['data'][k]['info']['magic']
            difficulty = data['data'][k]['info']['difficulty']
            tags = data['data'][k]['tags']
            tag = ""
            for i in tags:
                tag =tag + i+" "
            partype = data['data'][k]['partype']
            hp = data['data'][k]['stats']['hp']
            hpperlevel = data['data'][k]['stats']['hpperlevel']
            mpperlevel = data['data'][k]['stats']['mpperlevel']
            movespeed = data['data'][k]['stats']['movespeed']
            armor = data['data'][k]['stats']['armor']
            armorperlevel = data['data'][k]['stats']['armorperlevel']
            spellblock = data['data'][k]['stats']['spellblock']
            spellblockperlevel = data['data'][k]['stats']['spellblockperlevel']
            attackrange = data['data'][k]['stats']['attackrange']
            hpregen = data['data'][k]['stats']['hpregen']
            hpregenperlevel = data['data'][k]['stats']['hpregenperlevel']
            mpregen = data['data'][k]['stats']['mpregen']
            mpregenperlevel = data['data'][k]['stats']['mpregenperlevel']
            crit = data['data'][k]['stats']['crit']
            critperlevel = data['data'][k]['stats']['critperlevel']
            attackdamage = data['data'][k]['stats']['attackdamage']
            attackdamageperlevel = data['data'][k]['stats']['attackdamageperlevel']
            attackspeedperlevel = data['data'][k]['stats']['attackspeedperlevel']
            attackspeed = data['data'][k]['stats']['attackspeed']
            request_data['champion'].append({
                'id':id,
                'key':key,
                'name':name,
                'title':title,
                'blurb':blurb,
                'attack':attack,
                'defense':defense,
                'magic':magic,
                'difficulty':difficulty,
                'tags':tag,
                'partype':partype,
                'hp':hp,
                'hpperlevel':hpperlevel,
                'mpperlevel':mpperlevel,
                'movespeed':movespeed,
                'armor':armor,
                'armorperlevel':armorperlevel,
                'spellblock':spellblock,
                'spellblockperlevel':spellblockperlevel,
                'attackrange':attackrange,
                'hpregen':hpregen,
                'hpregenperlevel':hpregenperlevel,
                'mpregen':mpregen,
                'mpregenperlevel':mpregenperlevel,
                'crit':crit,
                'critperlevel':critperlevel,
                'attackdamage':attackdamage,
                'attackdamageperlevel':attackdamageperlevel,
                'attackspeedperlevel':attackspeedperlevel,
                'attackspeed':attackspeed
            })

    response = requests.post(API_URL + 'lol-champion-info/', data=json.dumps(request_data), headers=headers)
    print(response.text)


if __name__ == '__main__':
    create_champion()
