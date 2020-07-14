from fractions import Fraction

x1 = 5
x2 = 3.4
print(type(x1))
print(type(x2))
print(2 ** 32)
print(2 ** 64)
print(2 ** 512)
x3 = 3 + 5j
print(type(x3))
x4 = 4 - 2j
print(x3 + x4, x3 - x4, x3 * x4)
print(abs(x3))
print((3 ** 2 + 5 ** 2) ** 0.5)
print(x3.real, x3.imag)
print(x3.conjugate())

print(Fraction(250, 72))
v1 = Fraction(5, 2) + Fraction(7, 3)
print(v1)
print(v1.denominator, v1.numerator)
