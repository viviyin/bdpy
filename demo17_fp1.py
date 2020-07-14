from pprint import pprint

courses = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
           {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
           {'name': 'andbiz3', 'field': 'android', 'attendee': 5, 'remote': False}]
print(type(courses), courses)
pprint(courses)
courses[0]['name'] = 'POOP'
pprint(courses)
courses2 = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
           {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
           {'name': 'andbiz3', 'field': 'android', 'attenden': 5, 'remote': False}]
pprint(courses2)
