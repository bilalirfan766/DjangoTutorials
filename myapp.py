import json

import requests

URL = "http://127.0.0.1:8000/api/link"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
def post_data():

    data = {"name": "shahveer", "roll": 188, "city": "lhr"}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()
