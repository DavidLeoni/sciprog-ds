from graph_solution import *
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
            raise Exception("Expected graph is None !")       
        
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
    
    def test_has_edge(self):
        self.assertTrue(dig({'a':['b']}).has_edge('a','b'))    
        self.assertFalse(dig({'a':['b']}).has_edge('a','a'))    
        self.assertTrue(dig({'a':['b'],
                            'a':['c']}).has_edge('a','c'))
                            
        with self.assertRaises(Exception):
            self.assertTrue(dig({'a':['b']}).has_edge('a','c'))

            
        
class FullGraphTest(DiGraphTest):
    
    def test_full_graph(self):
        self.assertDiGraphEqual(full_graph([]),
                                dig({}))
        self.assertDiGraphEqual(full_graph(['a']),
                                dig({'a': ['a']}))
        self.assertDiGraphEqual(full_graph(['a','b']), 
                                dig({'a':['a','b'],
                                    'b':['a','b']}))

class DagTest(DiGraphTest):        
    
    def test_dag(self):
        self.assertDiGraphEqual(dag([]), dig({}))
        self.assertDiGraphEqual(dag(['a']), dig({'a': []}))
        self.assertDiGraphEqual(dag(['a', 'b']), dig({'a': ['b']}))
        self.assertDiGraphEqual(dag(['a','b','c']),
                                dig({'a':['b','c'],
                                    'b':['c']}))

class ListGraphTest(DiGraphTest):        
    
    def test_list_graph(self):
        with self.assertRaises(Exception):
            list_graph(-4)
                    
        self.assertEquals(dig({}), list_graph(0))
        self.assertEquals(dig({1:[]}), list_graph(1))
        self.assertEquals(dig({1:[2],2:[3]}), list_graph(3))
        
class StarGraphTest(DiGraphTest):        

    def test_star_graph(self):
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
       
    def test_0(self):        
        self.assertDiGraphEqual(odd_line(0), dig({}))

    def test_1(self):        
        self.assertDiGraphEqual(odd_line(1), dig({1: []}))

    def test_2(self):        
        self.assertDiGraphEqual(odd_line(2), dig({1: [3]}))


    def test_3(self):        
        self.assertDiGraphEqual(odd_line(3), dig({1: [3],
                                                 3: [5]}))

    def test_4(self):        
        self.assertDiGraphEqual(odd_line(4), dig({1: [3],
                                                 3: [5],
                                                 5: [7]}))

class EvenLineTest(DiGraphTest):
        
    def test_0(self):        
        self.assertDiGraphEqual(even_line(0), dig({}))

    def test_1(self):        
        self.assertDiGraphEqual(even_line(1), dig({2: []}))

    def test_2(self):        
        self.assertDiGraphEqual(even_line(2), dig({4: [2]}))


    def test_3(self):        
        self.assertDiGraphEqual(even_line(3), dig({4: [2],
                                                  6: [4]}))

    def test_4(self):        
        self.assertDiGraphEqual(even_line(4), dig({4: [2],
                                                   6: [4],
                                                   8: [6]}))

class QuadsTest(DiGraphTest):
    
    
    def test_0(self):
        
        self.assertDiGraphEqual(quads(0), dig({}))

    def test_1(self):
        
        self.assertDiGraphEqual(quads(1), dig({1: [],
                                               2: [1]}))

    
    def test_2(self):
        
        self.assertDiGraphEqual(quads(2), dig({1: [3],
                                               2: [1],
                                               3: [4],
                                               4: [2]}))

    def test_3(self):
        
        self.assertDiGraphEqual(quads(3), dig({1: [3],
                                               2: [1],
                                               3: [4, 5],
                                               4: [2],
                                               5: [],
                                               6: [4, 5]}))


    def test_4(self):
        
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

    def test_1(self):        
        self.assertDiGraphEqual(pie(1), dig({0: [1],
                                             1: [1]}))

    def test_2(self):        
        self.assertDiGraphEqual(pie(2), dig({0: [1,2],
                                             1: [2],
                                             2: [1]}))

    def test_3(self):
        self.assertDiGraphEqual(pie(3), dig({0: [1,2,3],
                                             1: [2],
                                             2: [3],
                                             3: [1]}))

    def test_4(self):
        self.assertDiGraphEqual(pie(4), dig({0: [1,2,3,4],
                                             1: [2],
                                             2: [3],
                                             3: [4],
                                             4: [1]}))

class FluxTest(DiGraphTest):        

    def test_negative(self):
        with self.assertRaises(ValueError):
            flux(-1)
        with self.assertRaises(ValueError):
            flux(-2)
    
    def test_zero(self):
        self.assertDiGraphEqual(flux(0), dig({0: []}))

    def test_one(self):        
        self.assertDiGraphEqual(flux(1), dig({0: [1,2,3]}))
    
    def test_two(self):        
        self.assertDiGraphEqual(flux(2), dig({0: [1,2,3],
                                              1: [4],
                                              2: [5],
                                              3: [6]}))

    def test_three(self):        
        self.assertDiGraphEqual(flux(3), dig({0: [1,2,3],
                                              1: [4],
                                              2: [5],
                                              3: [6],
                                              4: [7],
                                              5: [8],
                                              6: [9]}))
        
        
class TestRemoveVertex(DiGraphTest):
    
    def test_empty(self):
        with self.assertRaises(Exception):
            dig({}).remove_vertex('a')
        
    def test_two(self):        
        g = dig({'a': ['b'],
                 'b': ['a']})
        
        g.remove_vertex('a')
        self.assertDiGraphEqual(g, dig({'b': []}))
        
        g.remove_vertex('b')
        self.assertDiGraphEqual(g, dig({}))

    def test_self(self):        
        g = dig({'a': ['a'],
                 'b': ['a', 'b']})
        
        g.remove_vertex('b')
        self.assertDiGraphEqual(g, dig({'a': ['a']}))
        
        g.remove_vertex('a')
        self.assertDiGraphEqual(g, dig({}))

class TransposeTest(DiGraphTest):
    
    def test_empty(self):
        g = dig({})
        g.transpose()
        self.assertDiGraphEqual(dig({}), g)
        
    def test_return_none(self):
        self.assertReturnNone(dig({}).transpose(), 'transpose')
        self.assertReturnNone(dig({'a': ['b']}).transpose(), 'transpose')                

    def test_self(self):
        g = dig({'a': ['a']})
        g.transpose()
        self.assertDiGraphEqual(g, g)
        
    def test_bipartite(self):
        g = dig({'a': ['c'],
                'b' : ['d']})
        g.transpose()
        self.assertDiGraphEqual(g, dig({'c': ['a'],
                                        'd': ['b']}))

    def test_star(self):
        g = dig({'a': ['b','c','d']})
        g.transpose()
        self.assertDiGraphEqual(g, dig({'b': ['a'],
                                        'c': ['a'],
                                        'd': ['a']}))
        g.transpose()
        self.assertEqual(g, dig({'a': ['b','c','d']}))

        
class HasSelfLoopsTest(DiGraphTest):       
        
    def test_empty(self):        
        self.assertFalse(dig({}).has_self_loops())

    def test_one(self):        
        self.assertFalse(dig({'a':[]}).has_self_loops())
        self.assertTrue(dig({'a':['a']}).has_self_loops())

    def test_two(self):        
        self.assertFalse(dig({'a':[]}).has_self_loops())
        self.assertTrue(dig({'a':['b', 'a']}).has_self_loops())
        self.assertFalse(dig({'a':['b'],
                              'b':['a']}).has_self_loops())


class RemoveSelfLoopTest(DiGraphTest):
        
    def test_empty(self):
        g = dig({})
        g.remove_self_loops()
        self.assertDiGraphEqual(g, dig({}))

    def test_no_loops(self):
        g = dig({'a':[]})
        g.remove_self_loops()
        self.assertDiGraphEqual(g, dig({'a':[]}))

    def test_complex(self):
        g = dig({'a':['a','b'],
                 'b':['c', 'b']})
        g.remove_self_loops()
        self.assertDiGraphEqual(g,
                                dig({'a': ['b'],
                                     'b': ['c']}))

        
class UndirTest(DiGraphTest):
    
    def test_empty(self):
        g = dig({})        
        self.assertDiGraphEqual(g.undir(), dig({}))
        
    def test_self(self):
        g = dig({'a': ['a']})        
        self.assertDiGraphEqual(g.undir(), g)
        
    def test_bipartite(self):
        g = dig({'a': ['c'],
                'b': ['d']})        
        self.assertDiGraphEqual(g.undir(), dig({'a': ['c'],
                                                'b': ['d'],
                                                'c': ['a'],
                                                'd': ['b']}))

    def test_star(self):
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
    
    def test_empty(self):
        with self.assertRaises(Exception):
            dig({}).distances('a')

    def test_not_found(self):
        with self.assertRaises(Exception):
            dig({'a'}).distances('b')


    def test_root(self):        
        self.assertEqual(dig({'a': []}).distances('a'),
                             {'a': 0})
        self.assertEqual(dig({'a': ['a']}).distances('a'),
                        {'a': 0})

    def test_one(self):        
        self.assertEqual(dig({'a': ['b']}).distances('a'),
                          {'a': 0, 
                           'b': 1})


    def test_unreachable(self):        
        self.assertEqual(dig({'a': [],
                              'b': []}).distances('a'),
                          {'a': 0, 
                          'b': -1})

    def test_triangle(self):        
        self.assertEqual(dig({'a': ['b'],
                              'b': ['c'],
                              'c': ['a']}).distances('a'),
                          {'a': 0, 
                           'b': 1,
                           'c': 2})
        
    def test_square(self):        
        self.assertEqual(dig({'a': ['b','c'],
                              'b': ['d'],
                              'c': ['d']}).distances('a'),
                          {'a': 0, 
                           'b': 1,
                           'c': 1,
                           'd': 2})

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
    def test_empty(self):
        self.assertEqual(dig({}).has_cycle(), False)
    
    def test_one_no_cycle(self):
        self.assertEqual(dig({'a':[]}).has_cycle(), False)

    def test_one_with_cycle(self):
        self.assertEqual(dig({'a':['a']}).has_cycle(), True)

    def test_two_without_cycle(self):
        self.assertEqual(dig({'a':['b']}).has_cycle(), False)

    def test_two_with_cycle(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['a'] }).has_cycle(), True) 

    def test_two_with_self_loop_1(self):
        self.assertEqual(dig({'a':['a'],
                              'b':['a'] }).has_cycle(), True)                               

    def test_two_with_self_loop_2(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['b'] }).has_cycle(), True)                                                             

    def test_triangle(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['c'],
                              'c':['a'] }).has_cycle(), True)                                                                           
    def test_triangle(self):
        self.assertEqual(dig({'a':['b'],
                              'b':['c'],
                              'c':[] }).has_cycle(), False)

   
    def test_complex_with_cycle(self):
        self.assertEqual(dig({'a':['b','c'],
                              'b':['d','e'],
                              'c':['b'] }).has_cycle(), False)

   
    def test_complex_with_cycle(self):
        self.assertEqual(dig({'a':['b','c'],
                              'b':['d','e','c'],
                              'c':['b'] }).has_cycle(), True)

                                                         