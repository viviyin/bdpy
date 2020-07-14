import requests

base_url = 'https://bdpy.firebaseio.com/%s.json'

r1 = requests.put(base_url % 'data1_string1', json='hello firebase!!!')
print(r1.status_code, r1.content)
r2 = requests.put(base_url % 'data2_chinese1', json='使用中文的資料hello firebase!!!')
print(r2.status_code, r2.content)
r3 = requests.put(base_url % 'data3_list1', json=[500, '500', '五百'])
print(r3.status_code, r3.content)
