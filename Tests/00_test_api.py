#!/bin/python3


import requests
import json


API_URL = 'http://0.0.0.0:3001/saludo/Javier'

#Test POST request

response = requests.request("GET", API_URL)

print(response.status_code)
print(response.text)

if response.status_code != 200 :
    print('se activo un fail')
    exit(1)


