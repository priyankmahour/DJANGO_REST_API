import requests
import json

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resourse(id=None):
    data={}
    if id is not None:
        data={ 'id':id  }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

get_resourse()
#get_resourse(1)

def create_resourse():
    data={
            'eno':9,
            'ename':'Su',
            'esal':6000,
            'eaddr':'MP'
         }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#create_resourse()
