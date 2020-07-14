x1 = 2
x2 = 4
x3 = 6
print(x1 & x2, x2 & x3)

y1 = True
y2 = False
z = y1 and y2
print(z)
z = y1 and y1
print(z)

y2s = [True, False, 3.14, 500, 'hello world', 5 + 3j, None]
print("now print in and order")
for y2 in y2s:
    z = y1 and y2
    print(z)
print("now print in or order")
y1 = False
for y2 in y2s:
    z = y1 or y2
    print(z)
