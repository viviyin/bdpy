import collections
from pprint import pprint
from itertools import groupby

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=12, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=20, remote=False)
courses = (poop, bdpy, pykt, andbiz, aiocv)
pprint(courses)
print("sort by field")
sorted_courses = sorted(courses, key=lambda x: x.field)
pprint(sorted_courses)
print("***explain group by***")
for p in groupby(sorted_courses, lambda x: x.field):
    print(type(p))
    print(p[0], type(p[0]), type(p[1]))
    print([e for e in p[1]])
print("***explain group by***")
print("***explain group by***")
#for p in groupby(courses, lambda x: x.field):
for p in groupby(sorted_courses, lambda x: x.field):
    print(p[0])
    print("....", [e for e in p[1]])
print("***explain group by***")