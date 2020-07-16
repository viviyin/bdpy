import pandas as pd

dict1 = {'station': ['Nangang', 'Taipei', 'Banqiao', 'Taoyuan', 'Hsinchu'],
         'order': [1, 2, 3, 4, 5],
         'backOrder': [5, 4, 3, 2, 1]}
df1 = pd.DataFrame(dict1)
print(df1)
print("remove index==2")
print(df1.drop(2))
print("remove multiple")
print(df1.drop([1, 3]))
print("remove column")
print(df1.drop('order', axis=1))
print("remove multiple columns")
print(df1.drop(['order', 'backOrder'], axis=1))
print("[alternative]: remove multiple columns")
print(df1.drop(['order', 'backOrder'], axis='columns'))
df1.drop([1, 4], inplace=True)
print(df1)
