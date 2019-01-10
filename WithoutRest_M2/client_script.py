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

#create_resourse()



def update_resourse(id=None):
    data={  'id':id,
            'marks':70,
            'age':27
         }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#update_resourse(5) # id is mandatory



def delete_resourse(id=None):
    data={  'id':id,
         }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

delete_resourse(5) # id is mandatory
