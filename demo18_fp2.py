import collections

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
print(type(course))
print(course)
poop = course(name='poop', field='python', attendee=10, remote=False)
print(poop)
print(poop.attendee, poop.remote, poop.name, poop.field)
# poop.name='iOS'
