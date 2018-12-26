import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resourse():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

get_resourse()
