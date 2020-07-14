class Person:
    def __init__(self, age):
        self.age = age


p1 = Person(5)
print(f'p1 id={hex(id(p1))}, p1.age id={hex(id(p1.age))},p1.age={p1.age}')
p1.age = 6
print(f'p1 id={hex(id(p1))}, p1.age id={hex(id(p1.age))} ,p1.age={p1.age}')

x1 = 6
print(f'x1 id={hex(id(x1))}')
print(f'x1==p1.age?{p1.age == x1}, x1 is p1.age?{p1.age is x1}')

a1 = ['a', 'b', 'c']
a2 = a1
a3 = ['a', 'b', 'c']
print(a1 == a2, a1 == a3)
print(a1 is a2, a1 is a3)
