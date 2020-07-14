str1 = "ABCDEFG1234567abcdefg"
print("%-10s==" % str1)
print("%-10s==" % str1[:3])
for i in range(0, 10):
    print("%*s==" % (-i, str1[:3]))

print("{:10s}==".format(str1))
print("{:10s}==".format(str1[:3]))
print("{:{}s}==".format(str1[:3], 10))
for i in range(1, 10):
    print("{:{}s}==".format(str1[:3], i))
