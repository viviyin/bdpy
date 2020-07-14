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

remoteCourses = filter(lambda x: x.remote is True, courses)
print(type(remoteCourses))
print(remoteCourses)
pprint([x for x in remoteCourses])
#
coursesWillOpen = filter(lambda x: x.attendee >= 10, courses)
# pprint([x for x in coursesWillOpen])
print("now iterate:::")
print(next(coursesWillOpen))
print(next(coursesWillOpen))
print(next(coursesWillOpen))
print(next(coursesWillOpen))
# print(next(coursesWillOpen))
