import pandas as pd

pd1 = pd.Series([3, 1, 4, 5, 9, -2, 8])
print(type(pd1))
print(pd1)
print(f"Series values={pd1.values}, value type={type(pd1.values)}")
print(f"Series index={pd1.index}, index type={type(pd1.index)}")
pd1_range = pd1.index
for r in pd1_range:
    print(f"get r={r}, value={pd1[r]}")

pd2 = pd.Series([4, 7, -5, 3], index=['Nangang', 'Taipei', 'Banqiao', 'Taoyuan'])
print(type(pd2), pd2)
print(pd2.values, pd2.index)
print(pd2['Taipei'])
for r2 in pd2.index:
    print(f"index={r2}, value={pd2[r2]}")

sub_index = ['Nangang', 'Taipei']
print(type(pd2[sub_index]), pd2[sub_index])
print("print pd2 > 0***")
print(pd2[pd2 > 0])
print("can be polynomial")
print(pd2 ** 2 + 2 * pd2 + 5)
