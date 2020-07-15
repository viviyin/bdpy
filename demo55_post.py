import requests

base_url = 'https://bdpy-aa8cc.firebaseio.com/%s.json'

url5 = base_url % 'demo5_ticket'

for i in range(20):
    object1 = {'cola': 1 + i, 'coffee': 2 + i}

    r1 = requests.post(url5, json=object1)
    print(r1.status_code, r1.json())
