import pandas as pd
import numpy as np

series1 = pd.Series(range(5), index=['p', 'q', 'r', 's', 't'])
print(series1)
print(series1.index)
print(type(range(5)), series1.values)
#
index1 = pd.Index(['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], dtype='object')
print(type(index1), index1)
print(index1[:3], index1[3:])
print(index1[2:5])

index2 = pd.Index(np.arange(0, 3, 0.1))
print(f"index2={index2}")
print(list(index2))
