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


    
def draw_nx(G):
    """ Draws a NetworkX graph object. By default, assumes it is a DiGraph.
    
        For required libraries, see 
        https://datasciprolab.readthedocs.io/en/latest/exercises/matrix-networks/matrix-networks-solution.html#Required-libraries
    
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
    
    
    # add graphviz layout options (see https://stackoverflow.com/a/39662097)
    G.graph['node'] = {'color': 'blue', 'fontcolor':'blue'}
    G.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved', 'fontcolor':'brown'}
    G.graph['graph'] = {'scale': '3'}

    # adding attributes to edges in multigraphs is more complicated but see
    # https://stackoverflow.com/a/26694158                    
    #G[0][0]['color']='red'
        
    pdot = nx.drawing.nx_pydot.to_pydot(G)
    plt = Image(pdot.create_png())
    display(plt)    
    
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