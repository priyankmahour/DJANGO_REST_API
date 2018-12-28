import json
import requests
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


def create_resource():
      new_emp={
             'eno':100,
             'ename':'kunny',
             'esal':99999,
             'eaddr':'U.P.'
            }
      data=json.dumps(new_emp)
      resp=requests.post(BASE_URL+ENDPOINT,data=data)
      print(resp.status_code)
      print(resp.json())
#create_resource()

def update_resource(id):
      new_emp={
             'id':id,
             'esal':9999,
             'eaddr':'U.P.'
            }
      resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
      print(resp.status_code)
      print(resp.json())
#update_resource(11)

def delete_resource(id):
      data={
             'id':id,
            }
      resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
      print(resp.status_code)
      print(resp.json())
delete_resource(6)








# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# #get_all()
#
#
#
# def create_resource():
#     new_emp={
#                'eno':7,
#                'ename':'mummy',
#                'esal':60000,
#                'eaddr':'U.P.'
#             }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# #create_resource()
#
#
# def update_resource(id):
#     new_emp={
#                'ename':'papa',
#                'esal':100000
#             }
#     resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(11)
#
#
# def delete_resource(id):
#     resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
# #delete_resource(7)
