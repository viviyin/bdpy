str1 = "ABCDEFG1234567abcdefg"
print('%10s==' % str1)
print('%10s==' % str1[:5])
print('%-10s==' % str1[:5])
print('{:10s}=='.format(str1))
print('{:10s}=='.format(str1[:5]))
print('{:>10s}=='.format(str1[:5]))
print('{:<10s}=='.format(str1[:5]))
print('%10s==' % str1)
print('%10s==' % '中文')
