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

#get_resourse()
#get_resourse(1)

def create_resourse():
    data={
            'eno':300,
            'ename':'Priyank',
            'esal':4000,
            'eaddr':'UP'
         }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#create_resourse()


def update_resourse(id):
    # data={  'id':id,
    #         'eno':100,
    #         'ename':'sunny',
    #         'esal':8000,
    #         'eaddr':'Bihar'
    #      }
    data={  'id':id,
            'eno':400,
            'esal':70001
         }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
update_resourse(11)


def delete_resourse(id):
    data={
          'id':id
         }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#delete_resourse(3)
