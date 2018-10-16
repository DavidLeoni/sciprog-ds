#
#      Library of utilities for Scientific Programming Algolab 
# 
#                   DO NOT MODIFY THIS FILE !
#
#  IMPORTANT: algolab.py files in exercises/ subdirs during sphinx conf 
#             get overwrittten by root algolab.py  !
#

import unittest
import sys



def _get_generic_tree_def():
    """ Hack to get the damned GenericTree definition without explicitly importing the module. 
    """

    if 'tree' in sys.modules: 
        return getattr(sys.modules['tree'], 'GenericTree')
    elif 'tree_solution' in sys.modules: 
        return getattr(sys.modules['tree_solution'], 'GenericTree')
    else:
        raise Exception("Cannot find a module containg GenericTree definition !")        


def gt(*args):
    """ Shorthand function that returns a GenericTree containing the provided 
        data and children. First parameter is the data, the following ones are the children.
        
        Usage examples:
        
        >>> print gt('a')
        a
        
        >>> print gt('a', gt('b'), gt('c'))            
            a
            ├b            
            └c
                            
    """
    if (len(args) == 0):
        raise Exception("You need to provide at least one argument for the data!")
        
    data = args[0]
    children = args[1:]
        
    GenericTree = _get_generic_tree_def()
    
    r = GenericTree(data)    
    for c in reversed(children):        
        c._sibling = r._child
        c._parent = r
        r._child = c        
    return r

def str_trees(t1, t2, error_row=-1):
    """ Returns a string version of the two trees side by side
    
        If error_row is given, the line in error is marked.
        If error_row == -1 it is ignored 
    """    
    
    s1 = str(t1)
    s2 = str(t2)

    lines1 = s1.split("\n")
    lines2 = s2.split("\n")                

    max_len1 = 0                
    for line in lines1:                                    
        max_len1 = max(len(line.rstrip()), max_len1)        
    max_len1 = max(max_len1, len("ACTUAL"))        
        
    max_len2 = len("EXPECTED")
    for line in lines2:                                    
        max_len2 = max(len(line.rstrip()), max_len2)
    
    strings = []

    dist = 2 
    
    strings.append(("ACTUAL").ljust(max_len1 + dist))
    strings.append("  EXPECTED\n")
    
    i = 0

    while i < len(lines1) or i < len(lines2):

        if i < len(lines1): 
            strings.append(lines1[i].rstrip())
            len1 = len(lines1[i].rstrip())
        else:
            len1 = 0
                       
        if (i < len(lines2)):
            len2 = len(lines2[i].rstrip())
            
            pad_len1 = 4 + max_len1 - len1
            strings.append((" " * pad_len1) + lines2[i].rstrip()) 
        else:
            len2 = 0
            
        if (error_row == i):
            pad_len2 = 2 + max_len1 + max_len2 - len1 - len2
            strings.append((" " * pad_len2) + "<--- DIFFERENT ! ")  # TODO this shoots 'DIFFERENT' too far !
            
        strings.append("\n")

        i += 1
    
    return "".join(strings)


class GenericTreeTest(unittest.TestCase):

    def assertRoot(self, t):
        """ Checks provided node t is a root, if not raises Exception """
                          
        self.assertTrue(t.is_root(), "Detached node " + t.data() + " is not a root, does it have still the _parent or _sibling set to something ?")

    
    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEqual(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! Instead you are returning " + str(ret))
    
    
    def assertTreeEqual(self, actual, expected):
        """ Asserts the trees actual and expected are equal """
        
        GenericTree = _get_generic_tree_def()
        
        def rec_assert(c1, c2, row):                    
            
            if c2 == None:
                raise Exception("Bad test code! Found a None node in EXPECTED tree!\n\n" 
                                + str_trees(actual,expected,row))
            
            if c1 == None:
                raise Exception("Found a None node in actual tree! \n\n"
                                + str_trees(actual,expected,row))                     

            if not isinstance(c2, GenericTree):
                raise Exception("Bad test code! EXPECTED value is an instance of  %s , which is not a GenericTree !\n\n%s" % (type(c2).__name__ , str_trees(actual,expected,row)))
                                
            if not isinstance(c1, GenericTree):
                raise Exception("ACTUAL node is an instance of  %s  , which is not a  GenericTree  !\n\n%s"
                                % (type(c1).__name__, str_trees(actual, expected, row )))
                            
            if c1.data() != c2.data():
                raise Exception("Actual data is different from expected!\n\n" 
                                + str_trees(actual,expected,row))
            
            self.assertTrue(c1 == actual or c1.parent() != None, 
                            "Actual parent is None!"
                           + "\n\n" +  str_trees(actual,expected,row) )

            self.assertTrue(c2 == expected or c2.parent() != None, 
                            "Expected parent is None!" 
                             + "\n\n" +  str_trees(actual,expected,row) )            
            
            self.assertTrue(c1.parent() == None or isinstance(c1.parent(), GenericTree), 
                           "Actual parent is not a GenericTree instance!"
                            + "\n\n" +  str_trees(actual,expected,row) )
            self.assertTrue(c2.parent() == None or isinstance(c2.parent(), GenericTree), 
                           "Expected parent is not a GenericTree instance!"
                            + "\n\n" +  str_trees(actual,expected,row) )
            
            if (c1.parent() == None):
                if (c2.parent() != None):
                    raise Exception("Different parents! "
                                    + "Actual parent = None   Expected parent.data() = " + str(c2.parent().data()) 
                                    + "\n\n" + str_trees(actual,expected,row) )
                                    
            else:    
                if (c2.parent() == None):                    
                    raise Exception("Different parents! "
                                    + "Actual parent.data() = " + str(c1.parent().data()) 
                                    + "   Expected parent = None"
                                    + "\n\n" + str_trees(actual,expected,row)) 
                else: # let's just check data for now
                    self.assertEquals(c1.parent().data(), c2.parent().data(),
                                  "Different parents ! " 
                                 + "Actual parent.data() = " + str(c1.parent().data()) 
                                    + "   Expected parent.data() = " + str(c2.parent().data()
                                    + "\n\n" + str_trees(actual,expected,row) ))
            i = 0            
            
            cs1 = c1.children()
            cs2 = c2.children()
            if (len(cs1) != len(cs2)):
                raise Exception("Children sizes are different !\n\n"
                                + str_trees(actual, expected, row + min(len(cs1), len(cs2))) )
            while (i < len(cs1) ):
                rec_assert(cs1[i], cs2[i], row + 1)   
                i += 1 
        
        rec_assert(actual, expected, 0)

        
        
        
class GenericTreeTestTest(GenericTreeTest):    
    """ Tests the test itself ... """

    
    def test_str_trees(self):
        self.assertTrue('a' in str_trees(gt('a'), gt('b')))
        self.assertTrue('b' in str_trees(gt('a'), gt('b')))
        
        self.assertTrue('a' in str_trees(gt('a', gt('b')), gt('b', gt('c'))))
        self.assertTrue('c' in str_trees(gt('a', gt('b')), gt('b', gt('c'))))
    
    def test_assert_tree_equal(self):
        self.assertTreeEqual(gt('a'), gt('a'))
        self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b')))
        
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a'), gt('b'))            
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('c')))
        
        # different structure
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b',gt('c'))))

        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b',gt('c'))), gt('a', gt('b')))        
    
    def test_print(self):
        # self.assertTreeEqual(gt('a', gt('b', gt('v')), gt('b', gt('v'))), gt('a', gt('b', gt('v'), gt('b', gt('v'))), gt('b')))
        return None 
        
def _get_digraph_def():
    """ Hack to get the damned DiGraph definition without excplicitly importing the module. 
    """

    if 'graph' in sys.modules: 
        return getattr(sys.modules['graph'], 'DiGraph')
    elif 'graph_solution' in sys.modules: 
        return getattr(sys.modules['graph_solution'], 'DiGraph')
    else:
        raise Exception("Cannot find a module containing DiGraph definition !")        

def _get_visit_def():
    """ Hack to get the damned Visit definition without excplicitly importing the module. 
    """

    if 'graph' in sys.modules: 
        return getattr(sys.modules['graph'], 'Visit')
    elif 'graph_solution' in sys.modules: 
        return getattr(sys.modules['graph_solution'], 'Visit')
    else:
        raise Exception("Cannot find a module containing Visit definition !")        
        
def _get_vertex_log_def():
    """ Hack to get the damned VertexLog definition without excplicitly importing the module. 
    """

    if 'graph' in sys.modules: 
        return getattr(sys.modules['graph'], 'VertexLog')
    elif 'graph_solution' in sys.modules: 
        return getattr(sys.modules['graph_solution'], 'VertexLog')
    else:
        raise Exception("Cannot find a module containing VertexLog definition !")        

        
def str_compare_digraphs(actual, expected):
    """ Returns a string representing a comparison side by side 
        of the provided digraphs
    
    """
    
    DiGraph = _get_digraph_def()

    if actual == None and expected == None:
        return "Both graphs are None."

    if (actual == None) ^ (expected == None):
        if actual == None:
            what = ""
        else:
            what = "NOT"
        return "ACTUAL GRAPH IS " + what + " None ! " +"\n\nACTUAL: \n" + str(actual)  +"\n\nEXPECTED: \n" + str(expected) 

    if (isinstance(actual, DiGraph) ^ isinstance(expected, DiGraph)):
        if isinstance(actual, DiGraph):
            what = ""
        else:
            what = "NOT"
        return "ACTUAL GRAPH IS " + what + " an instance of DiGraph ! " +"\n\nACTUAL: \n" + str(actual)  +"\n\nEXPECTED: \n" + str(expected) 
    

    if actual.is_empty() ^ expected.is_empty():
        if actual.is_empty():
            what = ""
        else:
            what = "NOT"
            
        return " ACTUAL GRAPH IS " + what + " EMPTY ! " +"\n\nACTUAL: \n" + str(actual)  +"\n\nEXPECTED: \n" + str(expected) 

    dist = 2

    max_len1_keys = 0    
    max_len1_values = max(len("ACTUAL"), dist)
    for source in actual.verteces():
        max_len1_keys = max(max_len1_keys, len(str(source)+": " ))
        max_len1_values = max(max_len1_values, len(str(actual.adj(source))))
    
    max_len1 = len("ACTUAL")    
    for line in str(actual).split("\n"):        
        max_len1 = max(max_len1, len(line))
    
    max_len2_keys = 0    
    max_len2_values = len("EXPECTED")    
    for source in expected.verteces():
        max_len2_keys = max(max_len2_keys, len(str(source)+": " ))
        max_len2_values = max(max_len2_values, len(str(expected.adj(source))))
   
    max_len_keys = max(max_len1_keys, max_len2_keys)
            
    max_len2 = len("EXPECTED")
    for line in str(expected).split("\n"):
        max_len2 = max(max_len2, len(line))
    
    strings = []
    

    vs = sorted(set(actual.verteces()).union( expected.verteces()),key=str)

    strings = []

    
    strings.append(" " * (max_len_keys + dist))
    strings.append("ACTUAL".ljust(max_len1_values))
    strings.append(" " * dist)
    strings.append("EXPECTED\n")
    
    for vertex in vs:
                
        strings.append(str(vertex).ljust(max_len_keys))
        strings.append(': ')
                
        if vertex in actual.verteces():
            strings.append(str(actual.adj(vertex)).ljust(max_len1_values + dist))
        else:
            strings.append("--" + " " * (max_len1_values))
            
        if vertex in expected.verteces():            
            strings.append(str(expected.adj(vertex)).ljust(max_len2_values + dist))
        else:
            strings.append("--".ljust(max_len2_values + dist))
        
        if (not vertex in actual.verteces()
            or not vertex in expected.verteces()
            or set(actual.adj(vertex)) != set(expected.adj(vertex))):
            strings.append("  <---- DIFFERENT ! ")
        
        strings.append("\n")
            
    return ''.join(strings)

  
   
def dig(*args):
    """ Shorthand to construct a DiGraph with provided arguments
    
        To use it, provide source vertex / target vertex pairs like in the following examples:        
        
        >>> print dig()        
        
        DiGraph()
        
        >>> print dig('a',['b','c'])
                
        a: [b,c]
        b: []
        c: []
        
        >>> print dig('a',['b','c'],
                     'b', ['b'],
                     'c', ['a'])
                
        a: [b,c]
        b: [b]
        c: [a]                
        
    """
    
    DiGraph = _get_digraph_def()
    
    g = DiGraph()
        
    if len(args) % 2 == 1:
        raise Exception("Number of arguments must be even! You need to provide"
                    + " vertex/list pairs like 'a',['b', 'c'], b, ['d'], ... !")

    i = 1        
    for a in args:
        
        if i % 2 == 1:
            vertex = a
            g.add_vertex(vertex)            
            
        else:
            try:
                iter(a)
            except TypeError:
                raise Exception('Targets of ' + str(vertex) + ' are not iterable: ' + str(a) )
            for target in a:
                if not g.has_vertex(target):
                    g.add_vertex(target)
                g.add_edge(vertex, target)
        i += 1
    
    return g
    
    
    
def gen_graphs(n):    
    """ Returns a list with all the possible 2^(n^2) graphs of size n 
    
        Verteces will be identified with numbers from 1 to n 
    """    

    DiGraph = _get_digraph_def()    
    
    def gen_bits(n):
        """  Generates a sequence of 2^(n^2) lists, each of n^2 0 / 1 ints  """
                        
        bits = n*n;    
        nedges = 2**bits    
        
        ret = []
        for i in range(0, nedges):
                    
            right = [int(x) for x in bin(i)[2:]]
            lst = ([0] * (bits - len(right)))
            lst.extend(right)
    
            ret.append(lst)
        return ret

    if n == 0:
        return [DiGraph()]
        
    i = 0
    
    ret = []

    for lst in gen_bits(n):
        
        g = DiGraph()
        for j in range(1, n+1):
            g.add_vertex(j)
        
        source = 0
        for b in lst:            
            if i % n == 0:
                source += 1
            if b:
                g.add_edge(source, (i % n) + 1)
            i += 1
        ret.append(g)
    return ret


class DiGraphTest(unittest.TestCase):    
    
    def assertReturnNone(self, ret, function_name):
        
        """ Asserts method result ret equals None """
        self.assertEqual(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! Instead you are returning " + str(ret))

    
    def assertDiGraphEqual(self, actual, expected,  msg=None):
        
        DiGraph = _get_digraph_def()

        if expected == None:
            raise Exception("Bad test code! Expected graph is None !")       
        
        if actual == None:
            raise Exception("Actual graph is None !")                            

        if not isinstance(expected, DiGraph):
            raise Exception(("Bad test code! Expected value is an instance of %s , which is not a DiGraph !\n\n EXPECTED value was:\n\n %s" % (type(expected).__name__ , expected)))
                        
        if not isinstance(actual, DiGraph):
            raise Exception(("Actual value is an instance of %s , which is not a DiGraph!\n\n ACTUAL was:\n\n %s "  % (type(actual).__name__, actual)))
        
        if not expected == actual:            
            if msg == None:
                the_msg = "Graphs are different:"
            else:
                the_msg = msg
            raise AssertionError(the_msg + " \n\n" + str_compare_digraphs(actual, expected) )
    
    def assertSubset(self, set1, set2):
        """ Asserts set1 is a subset of set2 """
        
        if not set1.issubset(set2):
            raise AssertionError(str(set1) + " is not a subset of " + str(set2))
    
    def raise_graph(self, exception, graph, visit):
        """ Emulates reraising an exception for a given graph visit """
                        
        raise Exception(traceback.format_exc(exception)
             +"\n Failed graph was: \n" + str(graph)
             +"\n Failed graph visit was: \n" + str(visit))


class DiGraphTestTest(DiGraphTest):
    """
        Tests DiGraph basic methods
    """
    def test_adj(self):
        self.assertEqual(dig('a', []).adj('a'), 
                         [])
        self.assertEqual(dig('a', ['b']).adj('a'),
                         ['b'])
        self.assertEqual(dig('a', ['b', 'c']).adj('a'),
                         ['b', 'c'])
        g = dig('a', ['b'])
        lst = g.adj('a')
        lst[0] = 'c'
        self.assertEqual(['b'], g.adj('a'))
        
    def test_eq(self):
        
        self.assertEqual(dig('a', ['b','c']),
                         dig('a', ['c', 'b']))        
                                         
        self.assertTrue(dig('a', ['b','c']) == dig('a', ['c', 'b']))                         
        self.assertFalse(dig('a', ['b']) == dig('a', ['c', 'b']))                         
    
    def test_str(self):
        self.assertTrue("DiGraph()" in str(dig()))
        self.assertTrue("x" in str(dig('x',['y'])))
        self.assertTrue("y" in str(dig('x',['y'])))
        self.assertEquals(set(['x','y']), dig('x',['y']).verteces())
        self.assertEquals(set(['x','y','z','w', 'z']),
                          dig('x',['y'], 'z', ['w','x']).verteces())
       
                
    def test_gen_graphs(self):
        
        gs0 = gen_graphs(0)
        self.assertEqual(len(gs0), 1)
        self.assertTrue(dig() in gs0)
        
        gs1 = gen_graphs(1)        
        
        self.assertEqual(len(gs1), 2)    
        self.assertTrue(dig(1, []) in gs1)
        
    def test_assert_dig(self):
        
        self.assertDiGraphEqual(dig(), dig())
        
        with self.assertRaises(Exception):
            self.assertDiGraphEqual(dig(), dig('a',[]))        

    def test_dfs(self):

        with self.assertRaises(Exception):
            self.assertEquals(dig().dfs('a'), [])
                        
        self.assertEquals(dig('a',[]).dfs('a').verteces(), ['a'])
                        
        for g in gen_graphs(3):
            try:
                visit = g.dfs(1)
                self.assertLessEqual(visit.last_time(), 3*2)
                self.assertEqual(visit.log(1).finish_time, 
                                  visit.last_time())
            except Exception as e:
                self.raise_graph(e, g, visit)
          
    def test_bfs_empty(self):
        with self.assertRaises(Exception):
            dig().bfs('a')
        
    def test_bfs_not_found(self):
        with self.assertRaises(Exception):
            dig('a').bfs('b')

    def test_bfs_root_parent(self):
        
        visit = dig('a', ['a']).bfs('a')        
        self.assertEqual(visit.log('a').parent, None )

    def test_bfs_parent(self):
        
        visit = dig('a', ['a', 'b']).bfs('a')        
        self.assertEqual(visit.log('b').parent, 'a' )
              
             
    def test_bfs(self):

                                                        
        self.assertEquals(dig('a',[]).bfs('a').verteces(), ['a'])
                
        for g in gen_graphs(3):
            try:
                visit = g.bfs(1)
                self.assertSubset(set(visit.verteces()), g.verteces() )                
                self.assertLessEqual(visit.last_time(), 3)
            except Exception as e:                                                
                self.raise_graph(e, g, visit)                
                        
        
class VisitTest(unittest.TestCase):
    
    def test_log(self):        
        """ Checks it doesn't explode with non-existing verteces """
        
        Visit = _get_visit_def()
        
        self.assertEqual(-1, Visit().log('a').discovery_time)
        self.assertEqual(-1, Visit().log('a').finish_time)

    def test_verteces(self):        
        Visit = _get_visit_def()

        self.assertEqual([], Visit().verteces())
        
        visit = Visit()
        visit.log('a')
        self.assertEqual([], visit.verteces())
        self.assertEqual(['a'], visit.verteces(get_all=True))
        visit.log('a').discovery_time = 1
        self.assertEqual(['a'], visit.verteces())
        visit.log('b').discovery_time = 2
        self.assertEqual(['a', 'b'], visit.verteces())
        #  descendant=False, get_all=False):
        self.assertEqual(['b', 'a'], visit.verteces(descendant=True))
        self.assertEqual(['b', 'a'], visit.verteces(descendant=True))
        
        visit.log('a').finish_time = 4
        visit.log('b').finish_time = 3
        self.assertEqual(['b', 'a'], visit.verteces(sort_by=lambda log:log.finish_time))
        
    def test_str(self):
        Visit = _get_visit_def()

        visit = Visit()
        visit.log('z').discovery_time = 1        
        self.assertTrue('z' in str(visit))                

        

def show_distances():
    import networkx as nx
    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(['a  0','b  1', 'c  1', 'd  2', 'e  3', 'f  -1', 'g  -1'])
    ret.add_edges_from([('a  0','b  1'),('a  0', 'c  1'), ('b  1', 'd  2'),  ('c  1', 'd  2'), ('d  2', 'e  3') 
                      , ('e  3', 'd  2'),
                     ('f  -1', 'g  -1')])
    return ret
    
def to_nx(algolab_digraph):
    """ Convert an Algolab DiGraph into a NetworkX graph and return it. """
    import networkx as nx

    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(algolab_digraph.verteces())
    for sv in algolab_digraph.verteces():
        for tv in algolab_digraph.adj(sv):            
            ret.add_edge(sv, tv)
    return ret
    
def draw_mat(mat):    
    """ Draws a matrix as a DiGraph 
        In order to work, requires GraphViz (which is not a python package !)
        
        other libraries: networkx , pydot
    """

    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from IPython.display import Image, display
    import networkx as nx
    

    m = np.matrix(mat)

    G=nx.OrderedDiGraph(m)
    
    # add graphviz layout options (see https://stackoverflow.com/a/39662097)
    G.graph['node'] = {'color': 'blue', 'fontcolor':'blue'}
    G.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved', 'fontcolor':'brown'}
    G.graph['graph'] = {'scale': '3'}

    # adding attributes to edges in multigraphs is more complicated but see
    # https://stackoverflow.com/a/26694158                    
    #G[0][0]['color']='red'
    
    if not isinstance(mat[0][0], bool):
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i in G and j in G[i]:
                    G[i][j]['label'] = G[i][j]['weight']

    
    pdot = nx.drawing.nx_pydot.to_pydot(G)
    plt = Image(pdot.create_png())
    display(plt)
