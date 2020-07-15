import requests

base_url = 'https://bdpy-aa8cc.firebaseio.com/%s.json'
r1 = requests.get(base_url % 'data1_string1')
print(r1.status_code, r1.json())
r3 = requests.get(base_url % 'data3_list1')
print(r3.status_code, r3.json())
r4 = requests.get(base_url % 'data4_object')
print(type(r4.json()))
for k, v in r4.json().items():
    print(f"record key={k}, value={v}")

r5 = requests.get(base_url % 'demo5_ticket')
print(type(r5.json()), len(r5.json()))
allRecordDict = r5.json()
for k in allRecordDict:
    print(k)
for v in allRecordDict.values():
    print(v)
for k, v in allRecordDict.items():
    print(f"order id={k}, order list={v}")
