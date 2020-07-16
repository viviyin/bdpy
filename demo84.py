import pandas as pd

data = ['Nangang', 'Taipei', 'Banqiao']
index1 = pd.Index([0, 1, 2])
series1 = pd.Series(data, index=index1)
print(series1)
index2 = [0, 1, 2]
series2 = pd.Series(data, index=index2)
print(series2)
print(2 in index1, 2 in index2)
index3 = pd.Index(['Taipei', 'Taipei', 'Taipei'])
series3 = pd.Series(data, index=index3)
print(series3)
print("get taipei, get result====>")
print(series3['Taipei'])
