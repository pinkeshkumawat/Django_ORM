import requests
import json

URL1 = "http://127.0.0.1:8000/api1/"
URL2 = "http://127.0.0.1:8000/api2/"

headers = {'content-Type': 'application/json'}


def get(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    res = requests.get(url=URL2, headers=headers, data=json_data)
    print(res.json())

get()


def post():
    data = {
        'name': 'Pinkesh',
        'age': 24,
        'dept_id': 6
    }
    json_data = json.dumps(data)
    res = requests.post(url=URL2, headers=headers, data=json_data)
    print(res.json())


#post()
#get()














