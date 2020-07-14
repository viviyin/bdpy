import requests

URL1 = "https://bugzilla.mozilla.org/rest/bug/35"

result1 = requests.get(URL1)
print(result1.status_code, type(result1.content), result1.content)
print(type(result1.json()))
bugs = result1.json()["bugs"]
firstBug = bugs[0]
print(firstBug['assigned_to_detail'])
print(firstBug['cc_detail'])
print(type(firstBug['cc']))
cc_list = firstBug['cc']
for cc in cc_list:
    print(cc)
