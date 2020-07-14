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

nameAndCategory = map(lambda x: {'name': x.name, 'field': x.field}, courses)
print(type(nameAndCategory))
print(nameAndCategory)
pprint(tuple(nameAndCategory))
