#
#                  Library of utilities for 
#                   Scientific Programming
#                 Data Science Master @Unitn
#                    author:  David Leoni   
# 
#                   DO NOT MODIFY THIS FILE !
#
#                   
# 

import unittest
import sys

import random
# some attempt for avoiding random graphviz layout https://github.com/DavidLeoni/softpython-en/issues/2
random.seed(0)


def show_distances():
    import networkx as nx
    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(['a  0','b  1', 'c  1', 'd  2', 'e  3', 'f  -1', 'g  -1'])
    ret.add_edges_from([('a  0','b  1'),('a  0', 'c  1'), ('b  1', 'd  2'),  ('c  1', 'd  2'), ('d  2', 'e  3') 
                      , ('e  3', 'd  2'),
                     ('f  -1', 'g  -1')])
    return ret
    
def dig_to_nx(sciprog_digraph):
    """ Convert a Sciprog DiGraph into a NetworkX graph and return it. """
    import networkx as nx

    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(sciprog_digraph.verteces())
    for sv in sciprog_digraph.verteces():
        for tv in sciprog_digraph.adj(sv):            
            ret.add_edge(sv, tv)
    return ret

def draw_dig(sciprog_digraph,legend_edges=None, label='', save_to='', options={}):
    """ Draws a Sciprog DiGraph"""
    
    draw_nx(dig_to_nx(sciprog_digraph),legend_edges, label=label, save_to=save_to, options=options)


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


    
def draw_nx(G, legend_edges=None, label='', save_to='', options={}, clusters={}, clusters_common={}):
    """ Draws a NetworkX graph object. By default, assumes it is a DiGraph.
        
        - save_to: optional filepath where to save a .png image or .dot file        
        - to show clusters, set the cluster attribute in nodes
        - options: Dictionary of GraphViz options
        - clusters_common: options for all clusters
                           If 'dot_cluster':False is defined, creates a subgraph instead of a cluster.
        - clusters: map cluster ids to their options.                             
    
        For required libraries, see 
        https://en.softpython.org/graph-formats/graph-formats-sol.html#Required-libraries
    
        legend_edges example:
        
            legend_edges = [
                {'label':'ciao',
                 'color':'red'},
                {'label':'mondo',
                 'color':'blue'}

            ]    
    """
    
    if G == None:
        raise ValueError('Provided Graph is None !')        
                
    
    import networkx as nx
    import copy
       
    # fix graphviz path for anaconda in windows ...
    try:
        import os
        if os.name == 'nt':
            from os.path import expanduser
            home = expanduser("~")   # because in windows actual path can differ from user login !!!
            graphviz_path = '"C:\\Users\\' + home + '\\Anaconda3\\Library\\bin\\graphviz"'
            if os.path.exists(graphviz_path) and "PATH" in os.environ and (graphviz_path not in os.environ["PATH"]) :
                os.environ["PATH"] += ';' + graphviz_path
    except Exception as e:
        print(e)
        
    
    if not 'node' in G.graph:
        G.graph['node'] = {}
    if not 'edge' in G.graph:
        G.graph['edge'] = {}
    if not 'graph' in G.graph:
        G.graph['graph'] = {}

    def merge(d2, d1):
        d2.update({k:v for k,v in d1.items() if not k in d2})
        

    # add graphviz layout options (see https://stackoverflow.com/a/39662097)
    if 'node' in options:
        merge(G.graph['node'], options['node'])
    if 'edge' in options:
        merge(G.graph['edge'], options['edge'])
    if 'graph' in options:
        merge(G.graph['graph'], options['graph'])
    
        
    merge(G.graph['node'], {'color':'blue', 'fontcolor':'blue'})
    merge(G.graph['edge'], {'arrowsize': '0.6', 'splines': 'curved', 'fontcolor':'brown'})
        
    merge(G.graph['graph'], {'scale': '3', 'style':'dotted, rounded',}) 

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

    

    def make_clusters():

        allowed_types = (int,float,str,tuple)

        clus = {}
        nodes = G.nodes(data=True)
        if len(nodes) > 0:
            for node_id, data in nodes:                
                if 'cluster' in data:
                    
                    c = data['cluster']                   
                    
                    if c == None:  # for algos with forced cluster= in params
                        continue
                        
                    if not type(c) in allowed_types:
                        raise ValueError('Cluster type must be one of %s, found insted: %s' \
                                          % (type(c),allowed_types))
                    if c in clus:
                        clus[c].append(node_id)
                    else:
                        clus[c] = [node_id]
                    
            for c in clus:        
                if len(clus[c]) > 0:
                    pydot_mod = get_pydot_mod(pdot)
                    pydot_nodes = []                
                    
                    copts = {}                    
                    
                    copts = copy.deepcopy(clusters_common)                        
                    if c in clusters:                        
                        merge(copts, clusters[c])                    
                    
                    # we assume user wants physically close grouping
                    # NOTE: we invented dot_cluster property!
                    if not 'dot_cluster' in copts or copts['dot_cluster']: 
                        pydot_cluster = pydot_mod.Cluster(graph_name=str(c)) 
                    else:
                        pydot_cluster = pydot_mod.Subgraph(graph_name=str(c))  
                                             
                    for attr in copts:
                        if 'dot_cluster' != attr:
                            pydot_cluster.obj_dict['attributes'][attr] = copts[attr]
                        
                    for node_id in clus[c]:
                        pydot_node = pydot_mod.Node(name=node_id)
                        pydot_cluster.add_node(pydot_node)
                    pdot.add_subgraph(pydot_cluster)

    make_clusters()
    make_legend()
    fix_save_to = save_to.strip().lower()

    if fix_save_to:
        try:
            # note for saving dot we don't require graph_viz installed
            if fix_save_to.endswith('.dot'):
                pdot.write_raw(save_to.strip())
                print("Dot saved to file: ", save_to)
            else:               
                if not fix_save_to.endswith('.png'):
                    raise ValueError("Provided filename should end with .png  found instead save_to=%s" % save_to) 
                pdot.write_png(save_to)
                print("Image saved to file: ", save_to)

        except Exception as e:
            print("ERROR: Could not save file to ", save_to)
            print(e)

    # if we are in jupyter ...
    if not fix_save_to.endswith('.dot'):
        # if we save the dot file it's probably because 
        # we don't have graphviz on our system
        import importlib
        ipython_spec = importlib.util.find_spec("IPython")
        if ipython_spec:
            import matplotlib
            import matplotlib.pyplot as plt
            import matplotlib.image as mpimg
            from IPython.display import Image, display
            plt = Image(pdot.create_png())
            display(plt)    
    
def draw_mat(mat, legend_edges=None, label='', save_to='', options={}):    
    """ Draws a matrix as a DiGraph 
        
        - save_to: optional filepath where to save a .png image or .dot file        
        - options: Dictionary of GraphViz options
    
        For required libraries, see 
        https://en.softpython.org/graph-formats/graph-formats-sol.html#Required-libraries        
        
        For other options, see draw_nx
        
    """
    if mat == None:
        raise ValueError('Provided matrix is None !')    
        
    import numpy as np
    import networkx as nx
    

    m = np.matrix(mat)

    G=nx.DiGraph(m)

    if not isinstance(mat[0][0], bool):
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i in G and j in G[i]:
                    G[i][j]['label'] = G[i][j]['weight']
    

    
    draw_nx(G,legend_edges, label=label, save_to=save_to, options=options)

def draw_adj(d,legend_edges=None, label='', save_to='', options={}):
    """
        Draws a a graph represented as a dictionary of adjancency lists. 
        Node identifiers can be any immutable data structure, like numbers, strings, tuples ...
    
            {
              'c': ['a','d'],  # node 'c' links to node 'a' and 'd'
              'f': ['c']       # node 'f' links to node 'c'
            }

        - save_to: optional filepath where to save a .png image or .dot file        
        - options: Dictionary of GraphViz options
    
        For required libraries, see 
        https://en.softpython.org/graph-formats/graph-formats-sol.html#Required-libraries
            
        
        For other options, see draw_nx


    """
    
    if d == None:
        raise ValueError('Provided dictionary is None !')  
    
    import networkx as nx
    
    G=nx.DiGraph(d)
    draw_nx(G,legend_edges, label=label, save_to=save_to, options=options)
    
def draw_bt(bin_tree,legend_edges=None, label='', save_to='', options={}):
    """
        Draws a binary tree        

        - save_to: optional filepath where to save a .png image or .dot file        
        - options: Dictionary of GraphViz options
    
        For required libraries, see 
        https://en.softpython.org/graph-formats/graph-formats-sol.html#Required-libraries            
        
        For other options, see draw_nx

    """
    from bin_tree_test import bt
    from queue import deque
        
    
    def di(node):        
        if node is None:
            return id(None)
        return getattr(node, 'sciprog_fake_id', id(node))        
            
    def new_fake_node():
        nonlocal i
        ret = bt(i)
        ret.sciprog_fake_id = i
        i+=1
        return ret
    
    if bin_tree == None:
        raise ValueError('Provided bin_tree is None !')  
    
    import networkx as nx
    
    invstyle = 'invis' #'dashed'
        
    G=nx.DiGraph()
        
    q = deque()    
    q.append((None, bin_tree, True,None, 'n', 0))
    
    i = 0
    
    while len(q) > 0:
        
        parent, t, color, prev_sibling, headport, level = q.popleft()
        
        if color:
            G.add_node(di(t), label = t._data, cluster=di(parent))
        else:
            G.add_node(di(t), label = t._data, width='0.1', cluster=di(parent), style=invstyle)
                
        
        if prev_sibling:
            G.add_edge(di(prev_sibling),di(t), style=invstyle)
        
        if parent != None:            
            if headport == 'ne':
                tailport = 'sw'
            elif headport == 'n':
                tailport = 's'
            elif headport == 'nw':
                tailport = 'se'
            headport = 'n'
            if color:
                G.add_edge(di(parent),di(t), headport=headport, tailport=tailport)
            else:
                G.add_edge(di(parent),di(t), headport=headport, tailport=tailport, style=invstyle)

                
        if color and (t.left() or t.right()):
            if t.left():
                ln = t.left()
                new_color = True
            else:
                ln = new_fake_node()
                new_color = False

            q.append((t, ln, new_color, None, 'ne', level+1))

            mn = new_fake_node()
            q.append((t, mn, False, ln, 'n', level+1))  
            

            if t.right():
                rn = t.right()
                new_color = True
            else:
                rn = new_fake_node()
                new_color = False
            
            q.append((t, rn, new_color, mn, 'nw', level+1))
            
    options = {'graph':{'splines':'false', 'nodesep':'0.4', 'ranksep':'0.4'}}
    
    draw_nx(G,legend_edges, label=label, save_to=save_to, options=options, 
            clusters_common={'dot_cluster':False,'rank':'same'})
    
def draw_experimental_gt(gen_tree,legend_edges=None, label='', save_to='', options={}):
    """
        Draws a generic tree        

        - save_to: optional filepath where to save a .png image or .dot file        
        - to show clusters, set the cluster attribute in nodes
        - options: Dictionary of GraphViz options
    
        For required libraries, see 
        https://en.softpython.org/graph-formats/graph-formats-sol.html#Required-libraries            
        
        For other options, see draw_nx

    """
    
    def di(node):
        return str(id(node))
    
    if gen_tree == None:
        raise ValueError('Provided gen_tree is None !')  
    
    import networkx as nx
    
        
    G=nx.DiGraph()
    
    stack = [(gen_tree, 0)]
    visited = set()
    while len(stack) > 0:
        t, level = stack.pop()
        
        visited.add(di(t))
        
        G.add_node(di(t), label = t._data, color='black', fontcolor='black', cluster=level)
        
        if t.parent() != None:
            G.add_node(di(t.parent()), label = t.parent().data(), cluster=level-1)
            G.add_edge(di(t), di(t.parent()), color='blue', weight=1.0)
            if not di(t.parent()) in visited:
                
                stack.append((t.parent(), level - 1))
        
        if t.sibling() != None:
            G.add_node(di(t.sibling()), label = t.sibling().data(),  cluster=level)
            G.add_edge(di(t), di(t.sibling()), color='black', weight=0.2)
            if not di(t.sibling()) in visited:
                stack.append((t.sibling(), level))

        if t.child() != None:
            G.add_node(di(t.child()), label = t.child().data(), cluster=level+1)
            G.add_edge(di(t),di(t.child()), color='red', weight=1.0)
            if not di(t.child()) in visited:
                stack.append((t.child(), level+1))
    
    draw_nx(G,legend_edges, label=label, save_to=save_to, options=options)
    
        

def draw_proof(proof, db, step_id=None, only_ids=False):
    """ Draw all statements reachable from given row_id
    
        THIS FUNCTION IS ALREADY COMPLETE, *DO NOT* CHANGE IT !
    """    
    import networkx as nx
    
    stmt_type_to_color = {
        '$a' : 'blue',
        '$f' : 'purple'
    }
  
    G=nx.DiGraph()

    if step_id == None:
        step_id = len(proof)
    
    stack = [step_id]
    while len(stack) > 0:
        dep_id = stack.pop()
                
        attrs = proof[dep_id-1]        
        
        if only_ids:
            label = str(dep_id)
        else:            
            label = '%s\n%s\n%s: %s' % (dep_id, 
                                        attrs['sequence'], 
                                        attrs['label'],
                                        db[attrs['label']]['sequence'])

        color = stmt_type_to_color[attrs['keyword']]
        G.add_node( dep_id,
                    label=label, 
                    color=color)
        stack.extend(reversed(attrs['step_ids'])) # NOTE: IT IS REVERSED !
        
    for key in G.nodes():

        for target in proof[key-1]['step_ids']:
            G.add_edge(key, target)
    draw_nx(G)


def viz_server(default_module='example.py'):
    """
      Creates a Flask server to serve GraphViz by connecting to Gravizo online service
            
      default_module: a module name to execute, 
              (can be either with or without the '.py')

      WARNING: this is a prototype to use only when GraphViz is not installable, like in repl.it
      See also https://github.com/DavidLeoni/softpython-en/issues/3              
    """
    from flask import Flask, render_template_string, request, redirect

    web_site = Flask(__name__, static_url_path='/')

    index_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <title>softpython viz tool</title>    
        </head>
        <body>
        
            <form style="display:block; margin-bottom:15px;" 
                  action="/" 
                  method="post">
                <input type="text" 
                       name="module" 
                       value="{{module}}"/>
                <input type="submit" 
                       value="Reload"/>
            </form>                                    
            <img src='https://g.gravizo.com/svg?{{dot}}'/>
            <pre> {{error}} </pre>            
        </body>
        </html>    
    """

    def load_index(module):
        default_data = "digraph G {}"
        data = default_data
        err = ''
        try:
            print("The module is '" + module + "'")
            import importlib
            smod = module.strip()
            if smod.endswith('.py'):
                smod = smod[:-3]
            mod = importlib.import_module(smod)
            importlib.reload(mod)                                            
            with open('output.dot', 'r') as file:
                data = file.read()	
                i = data.index('{')
                
                if i != -1:
                    # gravizo really wants a named graph
                    # [ strict ] (graph | digraph) [ ID ] '{' stmt_list '}'
                    j = data.index('graph')
                    sp = data[j:i].strip().split()    
                    if len(sp) == 1:
                        data = data[:j] + 'graph G ' + data[i:]
                    # gravizo really does not want "" quotes
                    data = data[:i].replace('"','') + data[i:]
                
        except Exception as e:
            print('****** ERROR')
            import traceback 
            traceback.print_exc() 
            data = default_data
            err = e.__class__.__name__ + ': '+ str(e)
        import urllib
        from urllib.parse import quote
        data=quote(data)
        return render_template_string(index_html, 
                                module=module,
                                dot=data,
                                error=err)

    @web_site.route('/')
    def index():
        return load_index(default_module)

    @web_site.route('/', methods = ['POST'])
    def reload():                
        module = request.form['module']            
        return load_index(module)

    web_site.run(host='0.0.0.0', port=8080)