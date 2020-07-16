import pandas as pd

data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
        'year': [2018, 2017, 2019, 2020],
        'slide': [200, 250, 230, 300]}
df3 = pd.DataFrame(data, columns=['course', 'slide', 'year', 'instructor'],
                   index=['p1', 'p2', 'p3', 'p4'])
print(df3)
print(df3.loc['p1'])
print('slice by index name')
print(df3.loc[['p1', 'p3']])
df3['year'] = 2021
print(df3)
print('assign by a list')
df3['year'] = [2021, 2021, 2020, 2020]
print(df3)