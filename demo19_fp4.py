import collections
from pprint import pprint

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
courses = (poop, bdpy)
pprint(courses)

# del courses[0]
# courses.append(bdpy)
pprint(courses)
