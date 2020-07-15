import graphviz as gv

# format='svg'|'pdf'|'png'
g1 = gv.Graph(format='png')

g1.node('A')
g1.node('B')
g1.node('C')
g1.edge('A', 'B')
g1.edge('A', 'C')
g1.edge('A', 'A')
print(g1.source)
g1.render('graph/demo63')