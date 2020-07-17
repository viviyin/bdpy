import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
a1 = np.array(l1)
a2 = np.array(l2)
print(a1 + a2)
print(a1 * a2)
print(a1.dot(a2))
a3 = np.array([[1, 2], [3, 4]])
a4 = np.array([[5, 6], [7, 8]])
print(a3)
print(a4)
print(a3.dot(a4))
print(a4.dot(a3))
print(a3.transpose())
a5 = np.array([[1, 2, 3], [4, 5, 6]])
print(a5)
print(a5.transpose())
