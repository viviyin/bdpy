import graphviz as gv
import functools
import itertools

graph = functools.partial(gv.Graph, format='pdf')
digraph = functools.partial(gv.Digraph, format='pdf')
g3 = graph()
g4 = digraph()
print(type(g3), type(g4))


def add_nodes(g, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            g.node(n[0], **n[1])
        else:
            g.node(n)
    return g


def add_edges(g, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            g.edge(*e[0], **e[1])
        else:
            g.edge(*e)
    return g


companies = ['ucom', 'G-Jun', 'Da-Ya']
edges = [p for p in itertools.combinations(companies, 2)]
g3 = add_nodes(g3, companies)
g3 = add_edges(g3, edges)
g3.render('graph/demo65_g3')

n1 = ('A', {'label': 'ucom'})
n2 = ('B', {'label': '巨將'})
n3 = ('C', {'label': 'DaYa'})
n4 = ('D', {})
g4_nodes = [n1, n2, n3, n4]
e1 = (('A', 'B'), {'label': 'head quarter in Taipei'})
e2 = (('A', 'C'), {'label': 'multimedia is hot'})
e3 = (('B', 'C'), {'label': '競爭對手'})
e4 = (('B', 'D'), {})
g4_edges = [e1, e2, e3, e4]
g4 = add_nodes(g4, g4_nodes)
g4 = add_edges(g4, g4_edges)
g4.render('graph/demo65_g4')


def apply_styles(g, styles):
    g.graph_attr.update(('graph' in styles and styles['graph']) or {})
    g.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    g.edge_attr.update(('edges' in styles and styles['edges']) or {})
    return g


# 'rankdir' ==> 'TB','BT','LR', 'RL'
styles = {'graph': {'label': 'computer school',
                    'fontsize': '24',
                    'fontcolor': '#448800',
                    'bgcolor': '#C0FFEE',
                    'rankdir': 'LR'},
          'nodes': {'fontname': 'Microsoft YaHei Normal',
                    'shape': 'rectangle',
                    'color': 'red',
                    'fillcolor': '#FFC0EE',
                    'style': 'filled'},
          'edges': {'style': 'dotted',
                    'color': '#002288',
                    'arrowhead': 'open',
                    'fontname': 'Microsoft YaHei Normal',
                    'fontsize': '24',
                    'penwidth': '7'}}
g5 = apply_styles(g4, styles)
g5.render('graph/demo65_g5')
