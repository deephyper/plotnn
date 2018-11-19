from keras.utils.vis_utils import model_to_dot
from graphviz import Digraph
import networkx as nx
from networkx.drawing.nx_agraph import read_dot, write_dot

def convert(name):
    d = {}
    with open(f'{name}.dot', 'r') as f, open(f'{name}-new.dot', 'w') as fn:
        l = f.readline()
        while l != "":
            if 'label' in l:
                id_ = int(l.split()[0])
                op_ = l.split()[2].split('\\')[0]
                if 'Dense' in l or 'Input' in l:
                    n_ = int(l.split()[-1].split(')')[0])
                    op_ = 'InputDense' if 'Input' in l else 'Dense'
                    name = f"\"{id_}[{op_}({n_})]\""
                else:
                    name = f"\"{id_}[{op_}]\""
                d[id_] = name
            elif '->' in l:
                id1 = int(l.split()[0])
                id2 = int(l.split()[-1][:-1])
                nl = f'{d[id1]} -> {d[id2]};\n'
                fn.write(nl)
            else:
                fn.write(l)
            l = f.readline()

def get_num_units(g, name):
    if 'Dense' in name:
        d = list(name).index('(')
        f = list(name).index(')')
        return int(name[d+1:f])
    elif 'Concatenate' in name or 'Dropout' in name:
        return 1

def build(name):
    path = f'{name}-new.dot'
    G = read_dot(path)

    d = {}
    for n in G.nodes:
        if not(n in d):
            d[n] = {
            'num_units': min(10, get_num_units(G, n)),
            'succ_str': list(G.successors(n))[:10]
        }


    g = Digraph('g', filename=f'{name}-build.gv')
    g.graph_attr.update(splines="false", nodesep='1', ranksep='2')
    g.attr(arrowShape="none")

    for e in d:
        with g.subgraph(name=f'cluster_{e}') as c:
            c.attr(color="white")

            for i in range(d[e]['num_units']):
                name_d = f'{e}_{i}'
                if 'Input' in e:
                    color = "#33cc33"
                    c.node(name_d, shape="circle", style="filled", color=color, fontcolor=color)
                elif 'Dropout' in e:
                    color = "#ffcc00"
                    c.node(name_d, shape="rect", style="filled", color=color, fontcolor=color)
                elif 'Concatenate' in e:
                    color = "#993300"
                    c.node(name_d, shape="rect", style="filled", color=color, fontcolor=color)
                elif len(d[e]['succ_str']) == 0: # OUTPUT
                    color = "#ff0000"
                    c.node(name_d, shape="circle", style="filled", color=color, fontcolor=color)
                else:
                    color = "#3498db"
                    c.node(name_d, shape="circle", style="filled", color=color, fontcolor=color)
                for s in d[e]['succ_str']:
                    if 'Dense' in s:
                        for j in range(d[s]['num_units']):
                            name_a = f'{s}_{j}'
                            g.edge(name_d, name_a)
                    else:
                        for j in range(d[s]['num_units']):
                            name_a = f'{s}_{j}'
                            g.edge(name_d, name_a)
    g.view()



def model_visualize(model, name="graph"):
    # Keras model to dot file
    dot_graph = model_to_dot(model, show_shapes=True)
    dot_graph.write(f"{name}.dot", 'dot')

    # Convert dot to specific dot representation
    convert(name)

    # Build to graphvize
    build(name)
