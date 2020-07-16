import pandas as pd

data1 = {'poop': {2019: 5, 2020: 8},
         'bdpy': {2018: 5, 2019: 7, 2020: 10}}
df1 = pd.DataFrame(data1)
print(df1)
df2 = df1.T
print(df2)
df3 = pd.DataFrame(data1, index=[2018, 2019, 2020, 2021])
print(df3)
print(type(df3.values))
print(df3.values)
#################
data2 = {'poop': {2019: 5, 2020: 8},
         'bdpy': {2018: 5, 2019: 7, 2020: 'not yet'}}
df4 = pd.DataFrame(data2, index=[2018, 2019, 2020, 2021])
print(df4)
print(type(df4.values), type(df4.values[0, 0]))
print(df4.values)
