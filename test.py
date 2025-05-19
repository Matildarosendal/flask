#!/usr/bin/env python3

import requests

response = requests.get('http://localhost:8080/nums?numbers=4,3,6,5')

print(response.json(), response.status_code)

