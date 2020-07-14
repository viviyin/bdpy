x1 = 5
y1 = x1
print('x1=', x1, 'y1=', y1)
print('x1 id=', hex(id(x1)), ', y1 id=', hex(id(y1)))
x1 = 6
print('x1=', x1, 'y1=', y1)
print('x1 id=', hex(id(x1)), ', y1 id=', hex(id(y1)))
l1 = [5]
l2 = l1
print('l1=', l1, 'l2=', l2)
print('l1 id=', hex(id(l1)), ' ,l2 id=', hex(id(l2)))
l1[0] = 6
print('l1=', l1, 'l2=', l2)
print('l1 id=', hex(id(l1)), ' ,l2 id=', hex(id(l2)))
