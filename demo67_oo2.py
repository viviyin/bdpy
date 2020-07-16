class Car:
    vendor = 'Lexus'
    valid = True


c1 = Car()
c2 = Car()
print(Car.valid, c1.valid, c2.valid)
Car.function = True
print(Car.function, c1.function, c2.function)
c1.color = 'RED'
c2.capacity = 7
print(c1.color, c1.vendor, c1.valid, c1.function)
print(c2.capacity, c2.vendor, c2.valid, c2.function)
print(dir(c1))