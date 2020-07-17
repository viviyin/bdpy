import pandas as pd

data1 = pd.read_csv('data/demo100.csv')
print(data1.head())
print(data1.columns)
print(data1.info())
print(data1.describe())
groupedData1 = data1[['處分字號', '違反勞動基準法條款', '違反法規內容']].groupby(['違反勞動基準法條款']).count()
print(groupedData1.head())
sortedData1 = groupedData1.sort_values('處分字號', ascending=False)
print("------------------------")
print(sortedData1.head(n=20))
groupedByTwoColumn = data1[['處分字號', '違反勞動基準法條款', '違反法規內容']].\
    groupby(['違反勞動基準法條款', '違反法規內容']).count()
print(groupedByTwoColumn.head())
sortedWithTwoColumn = groupedByTwoColumn.sort_values('處分字號', ascending=False)
print(sortedWithTwoColumn.head(n=20))