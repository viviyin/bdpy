import collections
from pprint import pprint

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=12, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=20, remote=False)
courses = (poop, bdpy, pykt, andbiz, aiocv)
pprint(courses)

print("type 1, use list comprehension")
pprint([c for c in courses if c.attendee >= 10])
print("type 2, convert list comprehension to tuple")
pprint(tuple([c for c in courses if c.attendee >= 10]))
print("type 3, direct from generator to tuple")
pprint(tuple(x for x in courses if x.attendee >= 10))
