import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_teamData():
   
    request_data = {'gameResult' : []}
    
    response = requests.get(API_URL + 'lol-win-variable/', data=json.dumps(request_data), headers=headers)
    print(response.text)


if __name__ == '__main__':
    create_teamData()
