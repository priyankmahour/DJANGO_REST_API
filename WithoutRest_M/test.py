import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resourse(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
id=input("Enter the id of employee : ")
get_resourse(id)
