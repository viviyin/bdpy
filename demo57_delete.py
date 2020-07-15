import requests
base_url = 'https://bdpy-aa8cc.firebaseio.com/%s.json'

r1 = requests.delete(base_url % 'data1_string1')
print(f"return status code={r1.status_code}, content={r1.content}")
r3 = requests.delete(base_url % 'data3_list1')
r4 = requests.delete(base_url % 'data4_object')
r5 = requests.delete(base_url % 'demo5_ticket')