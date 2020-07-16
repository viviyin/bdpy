import pandas as pd
import numpy

series1 = pd.Series([20, 15, 18, 37, 25], index=['mar', 'jan', 'feb', 'may', 'apr'])
series2 = series1.reindex(['jan', 'feb', 'mar', 'apr', 'may', 'jun'])
print(series2)
series3 = pd.Series(['L', 'M', 'S'], index=[0, 5, 10])
print(series3)
series4 = series3.reindex(range(20), method='ffill')
print(series4)
series5 = pd.DataFrame(numpy.arange(16).reshape(4, 4), index=[1, 2, 3, 4],
                       columns=['kotlin', 'swift', 'C++', 'Java'])
print(series5)
series6 = series5.reindex(columns=['objC', 'kotlin', 'Java', 'swift', 'C++'])
print(series6)
