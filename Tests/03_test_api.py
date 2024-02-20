import requests
import json

API_URL=

payload = json.dumps({

    "vx": [2014, 2015, 2016, 2017,2018, 2019],
    "vy": [530, 560, 590, 620, 650, 680],
    "x": 2020
    })

headers = { 'Content-Type': 'application/json' }

response = requests.request("POST", API_URL, headers=headers, data=payload)

print(response.status_code)
print(response.text)


if response.status_code != 200 :
    print('se activo un fail')
    exit(1)

