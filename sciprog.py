#
#                  Library of utilities for 
#                   Scientific Programming
#                 Data Science Master @Unitn
# 
#                   DO NOT MODIFY THIS FILE !
#
#

import unittest
import sys

   

def show_distances():
    import networkx as nx
    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(['a  0','b  1', 'c  1', 'd  2', 'e  3', 'f  -1', 'g  -1'])
    ret.add_edges_from([('a  0','b  1'),('a  0', 'c  1'), ('b  1', 'd  2'),  ('c  1', 'd  2'), ('d  2', 'e  3') 
                      , ('e  3', 'd  2'),
                     ('f  -1', 'g  -1')])
    return ret
    
def dig_to_nx(algolab_digraph):
    """ Convert an Algolab DiGraph into a NetworkX graph and return it. """
    import networkx as nx

    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(algolab_digraph.verteces())
    for sv in algolab_digraph.verteces():
        for tv in algolab_digraph.adj(sv):            
            ret.add_edge(sv, tv)
    return ret

def draw_dig(sciprog_digraph):
    """ Draws a Sciprog DiGraph"""
    
    draw_nx(dig_to_nx(sciprog_digraph))


def get_pydot_mod(obj):
    """ RETURN the pydot module used by object.
        Made this function because there are too many pydot versions around,
        pydot, pydotplus and whatnot
        
        If you need to get the string name, use .__package__  attribute
    """

    import sys, inspect

    mod = inspect.getmodule(obj)
    base, _sep, _stem = mod.__name__.partition('.')
    return sys.modules[base]

    
def draw_nx(G, legend_edges=None, label=''):
    """ Draws a NetworkX graph object. By default, assumes it is a DiGraph.
    
        For required libraries, see 
        https://datasciprolab.readthedocs.io/en/latest/exercises/matrix-networks/matrix-networks-solution.html#Required-libraries
    
        legend_edges example:
        
            legend_edges = [
                {'label':'ciao',
                 'color':'red'},
                {'label':'mondo',
                 'color':'blue'}

            ]
    
    """
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from IPython.display import Image, display
    import networkx as nx
    
    # fix graphviz path for anaconda in windows ...
    import os
    if os.name == 'nt':
        graphviz_path = 'C:\\Users\\' + os.getlogin() + '\\Anaconda3\\Library\\bin\\graphviz'
        if os.path.exists(graphviz_path) and "PATH" in os.environ and (graphviz_path not in os.environ["PATH"]) :
            os.environ["PATH"] += ';' + graphviz_path
    
    
    if not 'node' in G.graph:
        G.graph['node'] = {}
    if not 'edge' in G.graph:
        G.graph['edge'] = {}
    if not 'graph' in G.graph:
        G.graph['graph'] = {}

    def merge(d2, d1):
        d2.update({k:v for k,v in d1.items() if not k in d2})
        

    # add graphviz layout options (see https://stackoverflow.com/a/39662097)
    
    merge(G.graph['node'], {'color':'blue', 'fontcolor':'blue'})
    merge(G.graph['edge'], {'arrowsize': '0.6', 'splines': 'curved', 'fontcolor':'brown'})
    merge(G.graph['graph'], {'scale': '3'}) # 
   
    # adding attributes to edges in multigraphs is more complicated but see
    # https://stackoverflow.com/a/26694158                    
    #G[0][0]['color']='red'
        
    pdot = nx.drawing.nx_pydot.to_pydot(G)

    if G.name:
        pdot.set_label(G.name)
        pdot.set_labelloc('t')
        pdot.set_labeljust('l')

    def make_legend():
        
        if legend_edges:

            pydot_mod = get_pydot_mod(pdot)

            glegend = pydot_mod.Cluster(graph_name = 'Legend', label = 'Legend', labeljust='c')

            i = 0
            for line in legend_edges:

                n1 = pydot_mod.Node(name='legend%s' % i , label=line['label'], shape='none', fontcolor=line['color'])
                n2 = pydot_mod.Node(name='legend%s' % (i+len(legend_edges)), label='', shape='none')
                glegend.add_node(n1)
                glegend.add_node(n2)
                glegend.add_edge(pydot_mod.Edge(n1,n2, color=line['color'], penwidth=3))

                i += 1

            pdot.add_subgraph(glegend)

    make_legend()
    plt = Image(pdot.create_png())
    display(plt)    

""" TODO Review these - taken from  https://stackoverflow.com/a/42102761
         notice 
{
    'rankdir':'LR',       # horizontal layout
    'size':'7.75,10.25',
    
    'overlap':'false',
    'maxiter':99999999,
    'damping':9999999,
    'voro_margin':'001',
    'start':0.1,
    'K':1,
    'nodesep':999999999999,
    'labelloc':'c',
    'defaultdist':9999999,
    'size':'20,20',
    'sep':'+1',
    'normalize':99999999,
    'labeljust':'l',
    'outputorder':'nodesfirst',
    'concentrate':'true',
    'mindist':2,
    'fontsize':99999999,
    'center':'true',
    'scale':'.01',
    'inputscale':99999999,
    'levelsgap':9999999,
    'epsilon':0.0001,
}    
"""
    
def draw_mat(mat):    
    """ Draws a matrix as a DiGraph 
        
        For required libraries, see 
        https://datasciprolab.readthedocs.io/en/latest/exercises/matrix-networks/matrix-networks-solution.html#Required-libraries
        
    """

    import numpy as np
    import networkx as nx
    

    m = np.matrix(mat)

    G=nx.DiGraph(m)

    if not isinstance(mat[0][0], bool):
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i in G and j in G[i]:
                    G[i][j]['label'] = G[i][j]['weight']

    
    draw_nx(G)

def draw_adj(d):
    """
        Draws a a graph represented as a dictionary of adjancency lists. 
        Node identifiers can be any immutable data structure, like numbers, strings, tuples ...
    
            {
              'c': ['a','d'],  # node 'c' links to node 'a' and 'd'
              'f': ['c']       # node 'f' links to node 'c'
            }

        For required libraries, see 
        https://datasciprolab.readthedocs.io/en/latest/exercises/matrix-networks/matrix-networks-solution.html#Required-libraries


    """
    
    import networkx as nx
    
    G=nx.DiGraph(d)
    draw_nx(G)