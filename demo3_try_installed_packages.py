import numpy

print(numpy.__version__)
l1 = ['a', 'b', 'c']
l2 = ['d', 'e']
print(l1 + l2)
l3 = [1, 2, 3]
l4 = [4, 5, 6]
print(l3 + l4)
a3 = numpy.array(l3)
a4 = numpy.array(l4)
print(a3 + a4)
