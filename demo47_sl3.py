import itertools

a1 = list('ABCD')
a2 = list('54321')
a3 = list('efgh')
a4 = list('甲乙')
result = itertools.chain(a1, a2, a3, a4)
print(result)
print([t for t in result])

result2 = itertools.permutations(a1, 2)
print([t for t in result2])
print([t for t in result2])
result3 = itertools.combinations(a1, 2)
result_tuple = tuple(t for t in result3)
print([p for p in result_tuple])
print([p for p in result_tuple])
