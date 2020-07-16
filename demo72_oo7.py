class Fib(object):
    def __init__(self, max_number):
        self.max = max_number
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.n = self.n + 1
            self.a, self.b = self.b, self.a + self.b
            return r
        raise StopIteration()


print(type(Fib(10)))
for i in Fib(10):
    print(i)
