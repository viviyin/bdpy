import requests

base_url = 'https://bdpy-aa8cc.firebaseio.com/%s.json'

url3 = base_url % 'data3_list1'
object3 = {2: '五佰', 3: 500.0, 6: "new"}
r3 = requests.patch(url3, json=object3)
print(r3.status_code, r3.json())

url4 = base_url % 'data4_object'
object4 = {'score': 80, 'instructor': 'David Liao'}
r4 = requests.patch(url4, json=object4)
print(r4.status_code, r4.json())
