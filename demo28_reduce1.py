import collections
from pprint import pprint
from functools import reduce

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=12, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=20, remote=False)
courses = (poop, bdpy, pykt, andbiz, aiocv)
pprint(courses)

# pprint([{'name': c.name, 'income': c.attendee * 8000} for c in courses])
income_list = tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses)
pprint(income_list)
total_income = reduce(lambda acc, x: acc + x['income'], income_list, 0)
print(total_income)
print(sum(t['income'] for t in income_list))