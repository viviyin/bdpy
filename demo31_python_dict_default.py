lists = ['s', 's', 'm', 'l', 'xl', 's', 'm', 'l', 'l', 'xl', 's', 'ss', 's', 'm', 'l', 'xl']

total = {}

for item in lists:
    total.setdefault(item, 0)
    total[item] += 1

print(f'total={total}')
