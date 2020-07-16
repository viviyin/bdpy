def someFunction2():
    x = 1007
    y = 70
    z = 50
    y = yield x
    yield x + y + z


f1 = someFunction2()
print(next(f1))
print(f1.send(100))


def function3():
    a = 1
    for i in range(10):
        a += 1
        yield a
    pass


print([i for i in function3()])


def fib2(max):
    prev, curr = 0, 1
    count = 0
    while count < max:
        count += 1
        yield curr
        prev, curr = curr, curr + prev


print(list(fib2(10)))
