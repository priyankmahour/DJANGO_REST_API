import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resourse(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
#id=input("Enter the id of employee : ")
#get_resourse(id)

def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())
#get_all()



def create_resource():
    new_emp={
               'eno':7,
               'ename':'dunny',
               'esal':13400,
               'eaddr':'M.P.'
            }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#create_resource()


def update_resource(id):
    new_emp={
               'ename':'kunny',
               'esal':1900
            }
    resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
update_resource(8)
