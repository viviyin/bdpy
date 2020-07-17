import pandas
import os
from matplotlib import pyplot, rc

CSV_PATH = "data/data98.csv"
XLS_PATH = "data/data98.xlsx"
print(os.getcwd())
df1 = pandas.read_csv(CSV_PATH, skiprows=4, index_col="Country Name")
print(df1.shape)
print(df1.head())
print(df1.tail())
print(df1.columns)
df1.to_excel(XLS_PATH, sheet_name="population")
print(df1['1960'].mean())
print('1970, population average={}'.format(df1['1970'].mean()))
df1['join_1980_1990'] = df1['1980'] + df1['1990']
print(df1.columns)
ausData = df1[df1['Country Code'] == 'AUS']
print(ausData.shape)
font = {'family': "Courier New"}
rc('font', **font)
print(pyplot.style.available)
pyplot.style.use('dark_background')
years = ['1960', '1970', '1980', '1990']
ausData.plot(kind='bar', y=years, figsize=(12, 6), fontsize=24)
pyplot.show()
