import csv

sampleFile1 = open('data/data1.csv')
sampleReader = csv.reader(sampleFile1)
sampleData = list(sampleReader)
sampleFile1.close()

print(type(sampleFile1))
print(type(sampleReader))
print(type(sampleData))

for row in sampleData:
    print(row)
    for c in row:
        print(c)
