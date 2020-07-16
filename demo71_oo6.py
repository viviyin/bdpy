class Object1:
    def __init__(self, limit):
        print("object create successfully")
        self.count = 0
        self.limit = limit

    def __iter__(self):
        print("start to iterate")
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        else:
            print("iterate")
            raise StopIteration()


o1 = Object1(5)
for i in o1:
    print(i)
o2 = Object1(3)
print(next(o2))
print(next(o2))
print(next(o2))
#print(next(o2))
