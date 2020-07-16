import pandas as pd

data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
        'year': [2018, 2017, 2019, 2020],
        'slide': [200, 250, 230, 300]}
df1 = pd.DataFrame(data)
print(type(data), type(df1))
print(df1)
print('get first 3 records')
print(df1.head(n=3))
print(len(df1))
df2 = pd.DataFrame(data, columns=['course', 'slide', 'year', 'instructor'])
print(df2)
df3 = pd.DataFrame(data, columns=['course', 'slide', 'year', 'instructor'],
                   index=['p1', 'p2', 'p3', 'p4'])
print(df3)
print(df3.columns)
print(df3.index)
print(f"select single column:{type(df3['course'])}")
print(f"select two columns:{type(df3[['course', 'year']])}")
print(df3['course'])
print(df3['course'].values)