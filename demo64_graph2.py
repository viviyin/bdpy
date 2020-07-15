import graphviz as gv
import itertools

g1 = gv.Graph(format='svg')

# teams = list('ABCDEF')
teams = ['Apple', 'Banana', 'Citron', 'Kiwi']
for t in teams:
    g1.node(t)
# competes = itertools.combinations(teams, 2)
competes = itertools.permutations(teams, 2)
edges = tuple(competes)

for e1, e2 in edges:
    g1.edge(e1, e2)

print(g1.source)
g1.render('graph/demo64')
