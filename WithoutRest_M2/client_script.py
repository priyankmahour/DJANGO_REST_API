import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resourse(id=None):
    data={}
    if id is not None:
       data={
             'id':id
            }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#get_resourse()
#get_resourse(2)

def create_resourse():
    data={
            'rno':6,
            'name':'ssehwag',
            'marks':27,
            'age':19
         }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

create_resourse()
