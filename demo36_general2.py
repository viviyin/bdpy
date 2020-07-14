import collections
import time
from pprint import pprint
import multiprocessing
import os

# print("start a process")
course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=12, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=20, remote=False)
courses = (poop, bdpy, pykt, andbiz, aiocv)


# pprint(courses)


def transform(x):
    print(f'process record:{x.name} with process id:{os.getpid()}')
    time.sleep(3)
    result = {'name': x.name, 'income:': x.attendee * 5000}
    print(f'process record done:{x.name} with process id:{os.getpid()}')
    return result


if __name__ == '__main__':
    start = time.time()
    # pool = multiprocessing.Pool(processes=2,maxtasksperchild=1)
    pool = multiprocessing.Pool(processes=2)
    print(f"now we run with process:{pool._processes}")
    result = pool.map(transform, courses)
    end = time.time()
    print(f'total time:{end - start:.3f} seconds')
    pprint(tuple(result))
