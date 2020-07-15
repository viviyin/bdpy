import requests

base_url = 'https://bdpy-aa8cc.firebaseio.com/%s.json'

r1 = requests.put(base_url % 'data1_string1', json='hello firebase!!!')
print(r1.status_code, r1.content)
r2 = requests.put(base_url % 'data2_chinese1', json='使用中文的資料hello firebase!!!')
print(r2.status_code, r2.content)
r3 = requests.put(base_url % 'data3_list1', json=[500, '500', '俉百'])
print(r3.status_code, r3.content)
object4 = {'course_name': "BDPY", "duration": 35, "score": 7.5, "test": None,
           'period': ['Sat', 'Sun']}
r4 = requests.put(base_url % 'data4_object', json=object4)
print(r4.status_code, r4.content)
print(r4.json())
