import pandas as pd

collection1 = pd.Series([1000, 800, 500, 300],
                        index=['nangang', 'taipei', 'baoqiao', 'taoyuan'])
collection2 = pd.Series([500, 300, 400],
                        index=['Hsinchu', 'Taichung', 'Tainan'])
collection3 = pd.Series([2000, 1800, 5300, 1300],
                        index=['nangang', 'taipei', 'baoqiao', 'taoyuan'])
collection4 = pd.Series([2500, 1300, 1400],
                        index=['Hsinchu', 'Taichung', 'Tainan'])
print("merge two Series with add")
print(collection1 + collection2)
print("merge two Series with add (same index)")
print(collection1 + collection3)
print(collection2 + collection4)
print("to merge, using append")
collection5 = collection1.append(collection2)
print(f"collection1=\n{collection1}")
print(f"collection5=\n{collection5}")
print(collection5.values)
print(collection5.index)
collection5.name = 'sold'
collection5.index.name = 'station'
print(collection5)
collection5.index = ['taipei', 'Taichung', 'Tainan', 'baoqiao', 'taoyuan', 'nangang', "Hsinchu"]
print(collection5)
