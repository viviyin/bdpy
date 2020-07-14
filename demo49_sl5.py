import json

data1 = ['sun', 'mon', 500, 30, None, 4.18]
data2 = {'name': 'BDPY', 'duration': '35hr'}
print(type(data1), type(data2))
result1 = json.dumps(data1)
result2 = json.dumps(data2)
print(type(result1), type(result2))
print(result1)
print(result2)
json1 = json.loads(result1)
json2 = json.loads(result2)
print(type(json1), json1[1])
print(type(json2), json2["name"])
