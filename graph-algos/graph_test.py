from graph_sol import *
import unittest

def str_compare_digraphs(actual, expected):
    """ Returns a string representing a comparison side by side 
        of the provided digraphs
    
    """


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

  
def dig(args):
    """ Shorthand to construct a DiGraph with provided arguments
    
        To use it, provide a dictionary with source vertex to  target verteces pairs like in the following examples:        
        
        >>> print dig({})
        
        DiGraph()
        
        >>> print dig({'a':['b','c']})
                
        a: [b,c]
        b: []
        c: []
        
        >>> print dig({'a': ['b','c'],
                       'b': ['b'],
                       'c': ['a']})
                
        a: [b,c]
        b: [b]
        c: [a]                
        
    """
        
    g = DiGraph()
             
    for vertex in args:
        
        g.add_vertex(vertex)            
            
        try:
            iter(args[vertex])
        except TypeError:
            raise Exception('Targets of %s are not iterable: %s' % (vertex, args[vertex]) )
        for target in args[vertex]:
            if not g.has_vertex(target):
                g.add_vertex(target)
            g.add_edge(vertex, target)
        
    return g
    
def udig(args):
    """ Shorthand to construct an *undirected* DiGraph with provided arguments
        If you include an edge a->b in arguments, it will automatically insert 
        an edge b->a in the output (if not yet present)
        For further usage info, see dig documentation.
    """

    ret = dig(args)
            
    for v in ret._edges:
        ret.add_vertex(v)
        
    for source in ret._edges:
        for target in ret._edges[source]:
            ret.add_edge(source, target)
            ret.add_edge(target, source)
            
    return ret    
    
def gen_graphs(n):    
    """ Returns a list with all the possible 2^(n^2) graphs of size n 
    
        Verteces will be identified with numbers from 1 to n 
    """    
    
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
        

        if expected == None:
            the_msg = "Expected graph is None !"
            raise AssertionError(the_msg)       
        
        if actual == None:
            the_msg = "Actual graph is None !"
            raise AssertionError(the_msg)

        if not isinstance(expected, DiGraph):
            the_msg = "Bad test code! Expected value is an instance of %s , which is not a DiGraph !\n\n EXPECTED value was:\n\n %s" % (type(expected).__name__ , expected)
            raise AssertionError(the_msg)
                        
        if not isinstance(actual, DiGraph):
            the_msg = "Actual value is an instance of %s , which is not a DiGraph!\n\n ACTUAL was:\n\n %s "  % (type(actual).__name__, actual)
            raise AssertionError(the_msg)
        
        if not expected == actual:            
            if msg == None:
                the_msg = "Graphs are different:"
            else:
                the_msg = msg
            the_msg = the_msg + " \n\n" + str_compare_digraphs(actual, expected) 
            raise AssertionError(the_msg)
    
    def assertSubset(self, set1, set2):
        """ Asserts set1 is a subset of set2 """
        
        if not set1.issubset(set2):
            the_msg = str(set1) + " is not a subset of " + str(set2)
            raise AssertionError(the_msg)


class DiGraphTestTest(DiGraphTest):
    """
        Tests DiGraph basic methods
    """
    def test_adj(self):
        self.assertEqual(dig({'a': []}).adj('a'), 
                         [])
        self.assertEqual(dig({'a': ['b']}).adj('a'),
                         ['b'])
        self.assertEqual(dig({'a': ['b', 'c']}).adj('a'),
                         ['b', 'c'])
        g = dig({'a': ['b']})
        lst = g.adj('a')
        lst[0] = 'c'
        self.assertEqual(['b'], g.adj('a'))
        
    def test_eq(self):
        
        self.assertEqual(dig({'a': ['b','c']}),
                         dig({'a': ['c', 'b']}))        
                                         
        self.assertTrue(dig({'a': ['b','c']}) == dig({'a': ['c', 'b']}))
        self.assertFalse(dig({'a': ['b']}) == dig({'a': ['c', 'b']}))                         
    
    def test_str(self):
        self.assertTrue("DiGraph()" in str(dig({})))
        self.assertTrue("x" in str(dig({'x':['y']})))
        self.assertTrue("y" in str(dig({'x':['y']})))
        self.assertEqual(set(['x','y']), dig({'x':['y']}).verteces())
        self.assertEqual(set(['x','y','z','w', 'z']),
                          dig({'x':['y'], 'z': ['w','x']}).verteces())
       
                
    def test_gen_graphs(self):
        
        gs0 = gen_graphs(0)
        self.assertEqual(len(gs0), 1)
        self.assertTrue(dig({}) in gs0)
        
        gs1 = gen_graphs(1)        
        
        self.assertEqual(len(gs1), 2)    
        self.assertTrue(dig({1: []}) in gs1)
        
    def test_assert_dig(self):
        
        self.assertDiGraphEqual(dig({}), dig({}))
        
        with self.assertRaises(Exception):
            self.assertDiGraphEqual(dig({}), dig({'a':[]}))        

    def test_dfs(self):

        # just running as it does nothing ..
        with self.assertRaises(Exception):
            dig({}).dfs('a')
                        
        dig({'a':[]}).dfs('a')
                        
        for g in gen_graphs(3):
            g.dfs(1)    
                
    def test_bfs_empty(self):
        with self.assertRaises(Exception):
            dig({}).bfs('a')
        
    def test_bfs_not_found(self):
        with self.assertRaises(Exception):
            dig({'a':[]}).bfs('b')

    def test_bfs_root_parent(self):
        dig({'a': ['a']}).bfs('a')        

    def test_bfs_parent(self):
        dig({'a': ['a', 'b']}).bfs('a')        

    def test_bfs(self):

        # just running bfs as it does nothing ...                                                

        dig({'a':[]}).bfs('a')
                
        for g in gen_graphs(3):
            g.bfs(1)

class HasEdgeTest(DiGraphTest):
    
    def test_01_has_edge(self):
        self.assertTrue(dig({'a':['b']}).has_edge('a','b'))    
        self.assertFalse(dig({'a':['b']}).has_edge('a','a'))    
        self.assertTrue(dig({'a':['b'],
                            'a':['c']}).has_edge('a','c'))
                            
        with self.assertRaises(Exception):
            self.assertTrue(dig({'a':['b']}).has_edge('a','c'))

            
        
class FullGraphTest(DiGraphTest):
    
    def test_01_full_graph(self):
        self.assertDiGraphEqual(full_graph([]),
                                dig({}))
        self.assertDiGraphEqual(full_graph(['a']),
                                dig({'a': ['a']}))
        self.assertDiGraphEqual(full_graph(['a','b']), 
                                dig({'a':['a','b'],
                                    'b':['a','b']}))

class DagTest(DiGraphTest):        
    
    def test_01_dag(self):
        self.assertDiGraphEqual(dag([]), dig({}))
        self.assertDiGraphEqual(dag(['a']), dig({'a': []}))
        self.assertDiGraphEqual(dag(['a', 'b']), dig({'a': ['b']}))
        self.assertDiGraphEqual(dag(['a','b','c']),
                                dig({'a':['b','c'],
                                    'b':['c']}))

class ListGraphTest(DiGraphTest):        
    
    def test_01_list_graph(self):
        with self.assertRaises(Exception):
            list_graph(-4)
                    
        self.assertEqual(dig({}), list_graph(0))
        self.assertEqual(dig({1:[]}), list_graph(1))
        self.assertEqual(dig({1:[2],2:[3]}), list_graph(3))
        
class StarGraphTest(DiGraphTest):        

    def test_01_star_graph(self):
        with self.assertRaises(Exception):
            star_graph(-4)
        self.assertDiGraphEqual(star_graph(0),
                                dig({}))
        self.assertDiGraphEqual(star_graph(1),
                                dig({1:[]}))      
        
        self.assertDiGraphEqual(star_graph(2),
                                dig({1: [2]}))
        self.assertDiGraphEqual(star_graph(3),
                                dig({1: [2,3]}))
        self.assertDiGraphEqual(star_graph(4),
                                dig({1: [2,3,4]}))
        
class OddLineTest(DiGraphTest):
       
    def test_00(self):        
        self.assertDiGraphEqual(odd_line(0), dig({}))

    def test_01(self):        
        self.assertDiGraphEqual(odd_line(1), dig({1: []}))

    def test_02(self):        
        self.assertDiGraphEqual(odd_line(2), dig({1: [3]}))


    def test_03(self):        
        self.assertDiGraphEqual(odd_line(3), dig({1: [3],
                                                 3: [5]}))

    def test_04(self):        
        self.assertDiGraphEqual(odd_line(4), dig({1: [3],
                                                 3: [5],
                                                 5: [7]}))

class EvenLineTest(DiGraphTest):
        
    def test_00(self):        
        self.assertDiGraphEqual(even_line(0), dig({}))

    def test_01(self):        
        self.assertDiGraphEqual(even_line(1), dig({2: []}))

    def test_02(self):        
        self.assertDiGraphEqual(even_line(2), dig({4: [2]}))


    def test_03(self):        
        self.assertDiGraphEqual(even_line(3), dig({4: [2],
                                                  6: [4]}))

    def test_04(self):        
        self.assertDiGraphEqual(even_line(4), dig({4: [2],
                                                   6: [4],
                                                   8: [6]}))

class QuadsTest(DiGraphTest):
    
    
    def test_00(self):
        
        self.assertDiGraphEqual(quads(0), dig({}))

    def test_01(self):
        
        self.assertDiGraphEqual(quads(1), dig({1: [],
                                               2: [1]}))

    
    def test_02(self):
        
        self.assertDiGraphEqual(quads(2), dig({1: [3],
                                               2: [1],
                                               3: [4],
                                               4: [2]}))

    def test_03(self):
        
        self.assertDiGraphEqual(quads(3), dig({1: [3],
                                               2: [1],
                                               3: [4, 5],
                                               4: [2],
                                               5: [],
                                               6: [4, 5]}))


    def test_04(self):
        
        self.assertDiGraphEqual(quads(4), dig({1: [3],
                                               2: [1],
                                               3: [4, 5],
                                               4: [2],
                                               5: [7],
                                               6: [4, 5],
                                               7: [8],
                                               8: [6]}))        

class PieTest(DiGraphTest):        
    
    def test_0(self):        
        self.assertDiGraphEqual(pie(0), dig({}))

    def test_01(self):        
        self.assertDiGraphEqual(pie(1), dig({0: [1],
                                             1: [1]}))

    def test_02(self):        
        self.assertDiGraphEqual(pie(2), dig({0: [1,2],
                                             1: [2],
                                             2: [1]}))

    def test_03(self):
        self.assertDiGraphEqual(pie(3), dig({0: [1,2,3],
                                             1: [2],
                                             2: [3],
                                             3: [1]}))

    def test_04(self):
        self.assertDiGraphEqual(pie(4), dig({0: [1,2,3,4],
                                             1: [2],
                                             2: [3],
                                             3: [4],
                                             4: [1]}))

class FluxTest(DiGraphTest):        

    def test_01_negative(self):
        with self.assertRaises(ValueError):
            flux(-1)
        with self.assertRaises(ValueError):
            flux(-2)
    
    def test_02_zero(self):
        self.assertDiGraphEqual(flux(0), dig({0: []}))

    def test_03_one(self):        
        self.assertDiGraphEqual(flux(1), dig({0: [1,2,3]}))
    
    def test_04_two(self):        
        self.assertDiGraphEqual(flux(2), dig({0: [1,2,3],
                                              1: [4],
                                              2: [5],
                                              3: [6]}))

    def test_05_three(self):        
        self.assertDiGraphEqual(flux(3), dig({0: [1,2,3],
                                              1: [4],
                                              2: [5],
                                              3: [6],
                                              4: [7],
                                              5: [8],
                                              6: [9]}))
        
        
class TestRemoveVertex(DiGraphTest):
    
    def test_01_empty(self):
        with self.assertRaises(Exception):
            dig({}).remove_vertex('a')
        
    def test_02_two(self):        
        g = dig({'a': ['b'],
                 'b': ['a']})
        
        g.remove_vertex('a')
        self.assertDiGraphEqual(g, dig({'b': []}))
        
        g.remove_vertex('b')
        self.assertDiGraphEqual(g, dig({}))

    def test_03_self(self):        
        g = dig({'a': ['a'],
                 'b': ['a', 'b']})
        
        g.remove_vertex('b')
        self.assertDiGraphEqual(g, dig({'a': ['a']}))
        
        g.remove_vertex('a')
        self.assertDiGraphEqual(g, dig({}))

class TransposeTest(DiGraphTest):
    
    def test_01_empty(self):
        g = dig({})
        g.transpose()
        self.assertDiGraphEqual(dig({}), g)
        
    def test_02_return_none(self):
        self.assertReturnNone(dig({}).transpose(), 'transpose')
        self.assertReturnNone(dig({'a': ['b']}).transpose(), 'transpose')                

    def test_03_self(self):
        g = dig({'a': ['a']})
        g.transpose()
        self.assertDiGraphEqual(g, g)
        
    def test_04_bipartite(self):
        g = dig({'a': ['c'],
                'b' : ['d']})
        g.transpose()
        self.assertDiGraphEqual(g, dig({'c': ['a'],
                                        'd': ['b']}))

    def test_05_star(self):
        g = dig({'a': ['b','c','d']})
        g.transpose()
        self.assertDiGraphEqual(g, dig({'b': ['a'],
                                        'c': ['a'],
                                        'd': ['a']}))
        g.transpose()
        self.assertEqual(g, dig({'a': ['b','c','d']}))

        
class HasSelfLoopsTest(DiGraphTest):       
        
    def test_01_empty(self):        
        self.assertFalse(dig({}).has_self_loops())

    def test_02_one(self):        
        self.assertFalse(dig({'a':[]}).has_self_loops())
        self.assertTrue(dig({'a':['a']}).has_self_loops())

    def test_03_two(self):        
        self.assertFalse(dig({'a':[]}).has_self_loops())
        self.assertTrue(dig({'a':['b', 'a']}).has_self_loops())
        self.assertFalse(dig({'a':['b'],
                              'b':['a']}).has_self_loops())


class RemoveSelfLoopTest(DiGraphTest):
        
    def test_01_empty(self):
        g = dig({})
        g.remove_self_loops()
        self.assertDiGraphEqual(g, dig({}))

    def test_02_no_loops(self):
        g = dig({'a':[]})
        g.remove_self_loops()
        self.assertDiGraphEqual(g, dig({'a':[]}))

    def test_03_complex(self):
        g = dig({'a':['a','b'],
                 'b':['c', 'b']})
        g.remove_self_loops()
        self.assertDiGraphEqual(g,
                                dig({'a': ['b'],
                                     'b': ['c']}))

        
class UndirTest(DiGraphTest):
    
    def test_01_empty(self):
        g = dig({})        
        self.assertDiGraphEqual(g.undir(), dig({}))
        
    def test_02_self(self):
        g = dig({'a': ['a']})        
        self.assertDiGraphEqual(g.undir(), g)
        
    def test_03_bipartite(self):
        g = dig({'a': ['c'],
                'b': ['d']})        
        self.assertDiGraphEqual(g.undir(), dig({'a': ['c'],
                                                'b': ['d'],
                                                'c': ['a'],
                                                'd': ['b']}))

    def test_04_star(self):
        g = dig({'a':['b','c','d']})
        self.assertDiGraphEqual(g.undir(), dig({'a': ['b','c','d'],
                                                'b': ['a'],
                                                'c': ['a'],
                                                'd': ['a']}))
        # tests double undirected invariant
        self.assertDiGraphEqual(g.undir(), dig({'a': ['b','c','d'],
                                                'b': ['a'],
                                                'c': ['a'],
                                                'd': ['a']}))        

class DistancesTest(DiGraphTest):
    
    def test_01_empty(self):
        with self.assertRaises(Exception):
            dig({}).distances('a')

    def test_02_not_found(self):
        with self.assertRaises(Exception):
            dig({'a'}).distances('b')


    def test_03_root(self):        
        self.assertEqual(dig({'a': []}).distances('a'),
                             {'a': 0})
        self.assertEqual(dig({'a': ['a']}).distances('a'),
                        {'a': 0})

    def test_04_one(self):        
        self.assertEqual(dig({'a': ['b']}).distances('a'),
                          {'a': 0, 
                           'b': 1})


    def test_05_unreachable(self):        
        self.assertEqual(dig({'a': [],
                              'b': []}).distances('a'),
                          {'a': 0, 
                          'b': -1})

    def test_06_triangle(self):        
        self.assertEqual(dig({'a': ['b'],
                              'b': ['c'],
                              'c': ['a']}).distances('a'),
                          {'a': 0, 
                           'b': 1,
                           'c': 2})
        
    def test_07_square(self):        
        self.assertEqual(dig({'a': ['b','c'],
                              'b': ['d'],
                              'c': ['d']}).distances('a'),
                          {'a': 0, 
                           'b': 1,
                           'c': 1,
                           'd': 2})

class EquiDistancesTest(DiGraphTest):
    
    def test_01_empty(self):
        with self.assertRaises(LookupError):
            dig({}).equidistances('a','a')

        with self.assertRaises(LookupError):
            dig({}).equidistances('a','b')


    def test_02_not_found(self):
        with self.assertRaises(Exception):
            dig({'a'}).equidistances('a','b')


    def test_03_root(self):        
        self.assertEqual(dig({'a': []}).equidistances('a','a'),
                             {'a':0})

    def test_03_root_self(self):        
        self.assertEqual(dig({'a': ['a']}).equidistances('a','a'),
                             {'a': 0})


    def test_04_ab_no_selfloops(self):        
        self.assertEqual(dig({'a': ['b'],
                              'b': ['a']}).equidistances('a','b'),
                          {})

    def test_05_ab_unreachable(self):        
        self.assertEqual(dig({'a': [],
                              'b': []}).equidistances('a', 'b'),
                          {})


    def test_06_a_b_c(self):        
        self.assertEqual(dig({'a': ['b'],
                              'b': [],
                              'c': ['b']}).equidistances('a','c'),
                          {'b': 1})

    def test_06_a_b_c_d_e(self):
        self.assertEqual(dig({'a': ['b'],
                              'b': ['c'],
                              'c': [],
                              'd':['c'],
                              'e': ['d'],
                              }).equidistances('a','e'),
                          {'c': 2})


    def test_06_diamond(self):        
        self.assertEqual(dig({'a': ['b','c'],
                              'd': ['b','c']}).equidistances('a','d'),
                          {'b': 1,
                           'c': 1})


    def test_07_complex(self):        
        self.assertEqual(dig({  'a': ['b','e'],
                                'b': ['d'],
                                'c': ['d'],
                                'd': ['f'],
                                'e': ['d','b'],
                                'f': ['g','h'],
                                'g': ['e']}).equidistances('a','g'),
                             {'d': 2,
                              'e': 1,
                              'f': 3,
                              'h': 4})

class CpTest(DiGraphTest):

    def test_01_wrong_source(self):
        with self.assertRaises(Exception):
             dig({}).cp('n666')

    def test_02_one(self):
        """   e1
        """        
        self.assertEqual(dig({'e1':[]}).cp('e1'), {'e1':None})

    def test_03_e1_selfloop(self):
        # if a node points to itself, we don't want to consider it a parent of itself"""
        self.assertEqual(dig({'e1':['e1']}).cp('e1'), 
                         {'e1':None}) 


    def test_04_n1_e1(self):
        """   n1 <- e1
        """        
        self.assertEqual(dig({'n1':['e1']}).cp('n1'), 
                              {
                               'n1':None, 
                               'e1':'n1'
                              })    

    def test_05_n1_n2_e1(self):
        """   n1 <- n2 <- e2
        """        
        self.assertEqual(dig({'n1':['n2'],
                              'n2':['e1']}).cp('n1'), 
                              {
                               'n1':None, 
                               'n2':'n1',
                               'e1':'n2'
                              })    

    def test_06_n1_e1_e2(self):
        """ n1 <- e2
            ^
            |
            e1
        """        
        self.assertEqual(dig({'n1':['e1','e2']}).cp('n1'), 
                              {
                               'n1':None, 
                               'e1':'n1',
                               'e2':'n1'
                              })    

    def test_07_n1_n2_e1_triangle(self):
        self.assertEqual(dig({'n1':['n2'],
                              'n2':['e1'],
                              'e1':['n1']}).cp('n1'), 
                              {
                               'n1':None, 
                               'n2':'n1',
                               'e1':'n2'
                              })   

    def test_08_n1_n2_n3_e1_diamond(self):
        """
              n1
             /   \ 
            .     .
           n2     n3
             \   /
              . .
              e1
        """
        self.assertEqual(dig({'n1':['n2','n3'],
                              'n2':['e1'],
                              'n3':['e1']}).cp('n1'), 
                              {
                               'n1':None, 
                               'n2':'n1',
                               'n3':'n1',
                               'e1':'n2'   # n2 is the leftmost in the queue
                              })   

    def test_09_complex(self):        
        """            
            See schema in exam text
        """

        self.assertEqual(dig({'n1':['n2','e2'],
                              'n2':['e1'],
                              'e1':['n1'],
                              'e2':['n2','n3', 'n4'],
                              'n3':['e3'],
                              'n4':['n1']}).cp('n1'),
                         {
                            'n1':None,
                            'n2':'n1',
                            'e1':'n2',
                            'e2':'n1',
                            'n3':'e2',
                            'n4':'e2',
                            'e3':'n3'
                          })

                     
class ExitsTest(DiGraphTest):


    def test_01_e1(self):
        """   e1
        """
        self.assertEqual(exits({'e1':None}),
                         {'e1':['e1']})  # the path to reach exit 1 starts with exit 1 itself

    def test_02_n1_e1(self):
        """   n1 <- e1
        """
        self.assertEqual(exits({'n1':None,
                                'e1':'n1'}),
                         {'e1':['n1','e1']})  # the path to reach exit 1 starts with n1

    def test_03_n1_n2_e1(self):
        """   n1 <- n2 <- e2
        """
        self.assertEqual(exits({'n1':None,
                                'n2':'n1',
                                'e1':'n2'}),
                         {
                           'e1':['n1','n2','e1']
                         }) 


    def test_04_n1_e1_e2_V(self):
        """ n1 <- e2
            ^
            |
            e1
        """
        self.assertEqual(exits({'n1':None,
                                'e1':'n1',
                                'e2':'n1'}),
                         {
                           'e1':['n1','e1'],
                           'e2':['n1','e2']
                         }) 
    def test_05_n1_e1_e2_seq(self):
        """   n1 <- e1 <- e2
        """
        self.assertEqual(exits({'n1':None,
                                'e1':'n1',
                                'e2':'e1'}),   
                        # to avoid congestion, half crowd may be told to exit e1, 
                        # while other half can go to e2 even if it is farther.
                         {
                           'e1':['n1','e1'],
                           'e2':['n1','e1','e2']
                         }) 


    def test_06_complex(self):        
        """

              n1
             /   \
           n2     e2
            \    /  \
            e1   n3  n4
                 |
                 e3
        """

        self.assertEqual(exits({'n1':None,
                                'n2':'n1',
                                'e1':'n2',
                                'e2':'n1',
                                'n3':'e2',
                                'n4':'e2',
                                'e3':'n3'}),   
                         {
                            'e1': ['n1','n2','e1'],
                            'e2': ['n1','e2'],
                            'e3': ['n1','e2','n3','e3']
                        })   
                     

        
        
class CCTest(DiGraphTest):
       
    def assertCCEqual(self, actual, expected):
        """ We need this to be sure the connected components indeces between actual and expected are the same, so we normalize the dicts
            
            Example:
                { 
                  'a':1,
                  'b':2,
                  'c':1
                }
                Should be consided the same as 
                {
                  'a':2,
                  'b':1,
                  'a':2                
                }
                
                But normalizing the second dict will look like the first one.
        """
        def normalize(d):
            ret = {}
            m = {} # old cc id -> new cc id
            counter = 1
            for k in sorted(d.keys()):
                if not d[k] in m:                    
                    m[d[k]] = counter                    
                    counter += 1
                ret[k] = m[d[k]]
            return ret
        
        self.assertEqual(normalize(actual), normalize(expected))

    #NOTE: uses udig
    def test_01_empty(self):        
        self.assertCCEqual(udig({}).cc(), {})

    #NOTE: uses udig
    def test_02_root(self):        
        self.assertCCEqual(udig({'a': ['a']}).cc(),
                           {'a': 1})

    #NOTE: uses udig
    def test_03_two_connected(self):        
        self.assertCCEqual(udig({'a': ['b']}).cc(),
                           {'a': 1, 
                            'b': 1})        
        
    #NOTE: uses udig
    def test_04_two_disconnected(self):        
        self.assertCCEqual(udig({'a': [], 
                                 'b': []}).cc(),
                           {'a': 1, 
                            'b': 2})            

    #NOTE: uses udig
    def test_05_triangle(self):        
        self.assertCCEqual(udig({'a': ['b'],
                                 'b': ['c'],
                                 'c': ['a']}).cc(),
                              {'a': 1, 
                               'b': 1,
                               'c': 1})

    #NOTE: uses udig
    def test_06_three_disconnected(self):        
        self.assertCCEqual(udig({'a': [],
                                 'b': [],
                                 'c': []}).cc(),
                                {'a': 1, 
                                 'b': 2,
                                 'c': 3})

    #NOTE: uses udig
    def test_07_three_two_comp(self):        
        self.assertCCEqual(udig({'a': ['b'],
                                 'c': []}).cc(),
                                {'a': 1, 
                                 'b': 1,
                                 'c': 2})        
    #NOTE: uses udig
    def test_08_four(self):        
        self.assertCCEqual(udig({'a': ['b'],
                                 'c': ['d']}).cc(),
                              {'a': 1, 
                               'b': 1,
                               'c': 2,
                               'd': 2})
        


class HasCycleTest(DiGraphTest):
    def test_01_empty(self):
        self.assertEqual(dig({}).has_cycle(), False)
    
    def test_02_one_no_cycle(self):
        self.assertEqual(dig({'a':[]}).has_cycle(), False)

    def test_03_one_with_cycle(self):
        self.assertEqual(dig({'a':['a']}).has_cycle(), True)

    def test_04_two_without_cycle(self):
        self.assertEqual(dig({'a':['b']}).has_cycle(), False)

    def test_05_two_with_cycle(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['a'] }).has_cycle(), True) 

    def test_06_two_with_self_loop_1(self):
        self.assertEqual(dig({'a':['a'],
                              'b':['a'] }).has_cycle(), True)                               

    def test_07_two_with_self_loop_2(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['b'] }).has_cycle(), True)                                                             

    def test_08_triangle(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['c'],
                              'c':['a'] }).has_cycle(), True)                                                                           
    def test_09_line(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['c'],
                              'c':[] }).has_cycle(), False)

   
    def test_10_complex_with_cycle_1(self):
        self.assertEqual(dig({'a':['b','c'],
                              'b':['d','e'],
                              'c':['b'] }).has_cycle(), False)

   
    def test_11_complex_with_cycle_2(self):
        self.assertEqual(dig({'a':['b','c'],
                              'b':['d','e','c'],
                              'c':['b'] }).has_cycle(), True)


class TopSortTest(DiGraphTest):                                                   

    def test_01_empty(self):
        self.assertEqual(dig({}).top_sort(), [])

    def test_02_one(self):
        self.assertEqual(dig({'a':[]}).top_sort(), ['a'])


    def test_03_ab(self):
        self.assertEqual(dig({'a':['b']}).top_sort(), ['a','b'])


    def test_04_abc_v(self):
        ts = dig({'a':['c'],'b':['c']}).top_sort()
        self.assertIn(ts, [
                            ['a','b','c'],
                            ['b','a','c']
                          ])

    def test_05_ab_cd(self):
        ts = dig({'a':['b'], 'c':['d']}).top_sort()
        # Observe that given this graph has two components each of size 2,
        # once two positions are fixed the other two are univocally determined
        # So first we write all possible sequences with a and b at distance 0
        # Then all possible sequences with a and b at distance 1
        # Then all possible sequences with a and b at distance 2
        self.assertIn(ts, [                    # 0123    
                            ['a','b','c','d'], # ab
                            ['c','a','b','d'],  #  ab
                            ['c','d','a','b'], #   ab
                            ['a','c','b','d'], # a b
                            ['c','a','d','b'], #  a b
                            ['a','c','d','b'], # a  b
                          ] )

    def test_06_simple_diamond(self):
        ts = dig({'a':['b','c'], 'b':['d'], 'c':['d']}).top_sort()
        self.assertIn(ts, [
                            ['a','b','c','d'],
                            ['a','c','b','d']
                          ] )


    def test_07_complex_diamond(self):
        ts = dig({'a':['b','c','d'], 'b':['e'], 'c':['e'], 'd':['e']}).top_sort()
        # Observe a and e will always stay at beginning and the end, respectively
        # Then progressively move b to the right, observing that for each b position
        # you can only have two other configurations for c and d
        self.assertIn(ts, [
                            ['a','b','c','d','e'],
                            ['a','b','d','c','e'],
                            ['a','d','b','c','e'],
                            ['a','c','b','d','e'],
                            ['a','c','d','b','e'],
                            ['a','d','c','b','e'],
                          ] )


    def test_08_dag(self):
        ts = dig({'a':['b','c','d'], 'b':['c','d'], 'c':['d'], 'd':[]}).top_sort()
        self.assertEqual(ts, ['a','b','c','d'] )
