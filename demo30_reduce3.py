import collections
from functools import reduce
from pprint import pprint

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=12, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=20, remote=False)
cplus = course(name='cplus', field='cpp', attendee=25, remote=True)
courses = (poop, bdpy, pykt, andbiz, aiocv, cplus)

pprint(courses)


def reducer(acc, val):
    acc.setdefault(val.field, [])
    acc[val.field].append(val.name)
    return acc


courseByCategory = reduce(reducer, courses, {})

pprint(courseByCategory)
