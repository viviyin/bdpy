def someFunction():
    a = 1
    b = 1
    yield a
    b = a + b
    yield b


f1 = someFunction()

print(type(someFunction))
print(type(someFunction()))
print(type(f1))
print(next(f1))
print(next(f1))
# print(next(f1))
print(next(someFunction()))
print(next(someFunction()))
print(next(someFunction()))
print(next(someFunction()))

