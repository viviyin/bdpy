import math
import random

print(math.pi, math.log2(2), math.sqrt(5))

for i in range(1, 20):
    print(random.randint(1, 10), end="\t")

banks = ['Fubon', 'Taishin', 'ChinaTrust', 'YuanTai']
for i in range(1, 10):
    print(random.choice(banks))
cards = ['A', 'K', 'Q', 'J', '10']
for i in range(1, 5):
    random.shuffle(cards)
    print(cards)
