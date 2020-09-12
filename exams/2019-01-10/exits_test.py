from exits_sol import *
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
    
    def test_01_has_edge(self):
        self.assertTrue(dig({'a':['b']}).has_edge('a','b'))    
        self.assertFalse(dig({'a':['b']}).has_edge('a','a'))    
        self.assertTrue(dig({'a':['b'],
                            'a':['c']}).has_edge('a','c'))
                            
        with self.assertRaises(Exception):
            self.assertTrue(dig({'a':['b']}).has_edge('a','c'))

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
                     


