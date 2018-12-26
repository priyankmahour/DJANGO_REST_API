import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='jsoncbv/'
resp=requests.delete(BASE_URL+ENDPOINT)
data=resp.json()
print('#'*50)
print("DTA FROM DJANGO APP : ")
print(data)
print(type(data))
