import pandas as pd

d1 = {'poop': 35, 'bdpy': 35, 'andbiz3': 35, 'testit': 14}
print(type(d1))
pd1 = pd.Series(d1)
print(type(pd1), pd1)
print('poop' in d1, 'poop' in pd1)
print('poop' not in d1, 'poop' not in pd1)
sorted_list = ['andbiz3', 'testit', 'poop', 'bdpy']
pd2 = pd.Series(d1, index=sorted_list)
print(pd2)
print("list quantity larger than dict..")
full_sorted_list = ['andbiz2', 'andbiz3', 'testit', 'poop', 'bdpy', 'pykt', 'aiocv']
pd3 = pd.Series(d1, index=full_sorted_list)
print(pd3)
print(f"pd3 is NA:\n{pd.isna(pd3)}")
print(f"pd3 is null:\n{pd.isnull(pd3)}")
print("using method")
print(pd3.isna())
print(pd3.isnull())
d2 = {'poop': 'Mark', 'bdpy': None, 'andbiz2': None, 'testit': 'Frank'}
pd4 = pd.Series(d2, index=full_sorted_list)
print(f"full pd4:\n{pd4}")
print(pd4.isna())
print(pd4.isnull())
