from tree_sol import *
import unittest



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
    
    r = GenericTree(data)    
    for c in reversed(children):        
        c._sibling = r._child
        c._parent = r
        r._child = c        
    return r

def get_children(gt):
    """ Handy methods to get children. Try not to use this in exercise code !!!!
    """
    current = gt._child
    ret = []
    while current != None:
        ret.append(current)        
        current = current.sibling()
    return ret
        

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
        
        def rec_assert(c1, c2, row):                    
            
            if c2 == None:
                raise Exception("Found a None node in EXPECTED tree!\n\n" 
                                + str_trees(actual,expected,row))
            
            if c1 == None:
                raise Exception("Found a None node in ACTUAL tree! \n\n"
                                + str_trees(actual,expected,row))                     

            if not isinstance(c2, GenericTree):
                raise Exception("EXPECTED value is an instance of  %s , which is not a GenericTree !\n\n%s" % (type(c2).__name__ , str_trees(actual,expected,row)))
                                
            if not isinstance(c1, GenericTree):
                raise Exception("ACTUAL node is an instance of  %s  , which is not a  GenericTree  !\n\n%s"
                                % (type(c1).__name__, str_trees(actual, expected, row )))
                            
            if c1.data() != c2.data():
                raise Exception("Actual data is different from expected!\n\n" 
                                + str_trees(actual,expected,row))
            
            self.assertTrue(c1 == actual or c1.parent() != None, 
                            "Parent of ACTUAL node is None!"
                           + "\n\n" +  str_trees(actual,expected,row) )

            self.assertTrue(c2 == expected or c2.parent() != None, 
                            "Parent of EXPECTED node is  %s !\n\n%s" 
                             % ( c2.parent(),str_trees(actual,expected,row)) )            
            
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
                    self.assertEqual(c1.parent().data(), c2.parent().data(),
                                  "Different parents ! " 
                                 + "Actual parent.data() = " + str(c1.parent().data()) 
                                    + "   Expected parent.data() = " + str(c2.parent().data()
                                    + "\n\n" + str_trees(actual,expected,row) ))
            i = 0            
            
            cs1 = get_children(c1)
            cs2 = get_children(c2)
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
 
            
                            
class InsertChildTest(GenericTreeTest):

    def test_insert_child(self):        
        ta = GenericTree('a')
        self.assertEqual(ta.child(), None)
        tb = GenericTree('b')        
        ret = ta.insert_child(tb) 
        self.assertEqual(ret, None)
        self.assertEqual(ta.child(), tb)
        self.assertEqual(tb.parent(), ta)        
        self.assertEqual(tb.sibling(), None)
        self.assertEqual(tb.child(), None)
        
        tc = GenericTree('c')
        ta.insert_child(tc)
        self.assertEqual(ta.child(), tc)
        self.assertEqual(tc.sibling(), tb)
        self.assertEqual(tc.parent(), ta)
        self.assertEqual(tb.sibling(), None)


class FillLeftTest(GenericTreeTest):

    def test_01_a_empty(self):
        t1 = gt('a')
        t1.fill_left([])
        self.assertTreeEqual(t1, gt('a'))

    def test_02_a_wrong(self):
        t1 = gt('a')
        with self.assertRaises(ValueError):
            t1.fill_left(['x'])
        with self.assertRaises (ValueError):
            t1.fill_left(['x','y'])

    def test_03_ab(self):
        """ 
            a
            └b
        """    
        t1 = gt('a', gt('b'))
        t1.fill_left(['x'])
        self.assertTreeEqual(t1, gt('a',gt('x')))
        with self.assertRaises(ValueError):
            t1.fill_left(['x','y'])


    def test_04_a_bc(self):
        """ 
            a
            ├b
            └c
        """    

        t1 = gt('a', gt('b'),gt('c'))
        t1.fill_left(['x'])
        self.assertTreeEqual(t1, gt('a',gt('x'), gt('c')))
        with self.assertRaises(ValueError):
            t1.fill_left(['x','y'])

    def test_05_a_bcd(self):
        """ 
            a
            ├b
            ├c
            └d
        """    

        t1 = gt('a', gt('b'),gt('c'),gt('d'))
        t1.fill_left(['x'])
        self.assertTreeEqual(t1, gt('a',gt('x'), gt('c'),gt('d')))
        with self.assertRaises(ValueError):
            t1.fill_left(['x','y'])


    def test_06_a_bc_d_x(self):
        """ 
            a
            └b
             ├c
             └d
        """    

        t1 = gt('a', gt('b',gt('c'),gt('d')))
        t1.fill_left(['x'])
        self.assertTreeEqual(t1, gt('a', gt('x',gt('c'),gt('d'))))
        with self.assertRaises(ValueError):
            t1.fill_left(['x','y','z'])

    def test_07_a_bc_d_xy(self):
        """ 
            a
            └b
             ├c
             └d
        """    

        t1 = gt('a', gt('b',gt('c'),gt('d')))
        t1.fill_left(['x','y'])
        self.assertTreeEqual(t1, gt('a', gt('x',gt('y'),gt('d'))))

    def test_08_complex(self):
        """ 
            a
            ├b
            |└e
            | ├f
            | ├g
            | |└i
            | └h
            ├c
            |
            └d
        """    
        
        t1 = gt('a', 
                    gt('b', 
                            gt('e',
                                    gt('f'), 
                                    gt('g', 
                                            gt('i')),
                            gt('h')),
                    gt('c'),
                    gt('d')))

        t1.fill_left(['x','y','z'])
        self.assertTreeEqual(t1,  gt('a', 
                                        gt('x', 
                                                gt('y',
                                                        gt('z'), 
                                                        gt('g', 
                                                                gt('i')),
                                                gt('h')),
                                        gt('c'),
                                        gt('d'))))
     
        
class FollowTest(GenericTreeTest):

    def test_01_a_empty(self):
        t1 = gt('a')
        self.assertEqual(t1.follow([]), ['a'])

    def test_02_a_wrong(self):
        t1 = gt('a')
        with self.assertRaises(ValueError):
            t1.follow([0])
        with self.assertRaises(ValueError):
            t1.follow([1])
        with self.assertRaises (ValueError):
            t1.follow([0,0])
        with self.assertRaises(ValueError):
            t1.follow([0,1])
        with self.assertRaises(ValueError):
            t1.follow([1,0])
        with self.assertRaises(ValueError):
            t1.follow([1,1])


    def test_03_ab(self):
        """ 
            a
            └b
        """    
        t1 = gt('a', gt('b'))
        self.assertEqual(t1.follow([]), ['a'])
        self.assertEqual(t1.follow([0]), ['a','b'])
        with self.assertRaises(ValueError):
            t1.follow([1])
        with self.assertRaises(ValueError):
            t1.follow([2])
        with self.assertRaises(ValueError):
            t1.follow([0,0])


    def test_04_a_bc(self):
        """ 
            a
            ├b
            └c
        """    

        t1 = gt('a', gt('b'),gt('c'))
        self.assertEqual(t1.follow([]), ['a'])
        self.assertEqual(t1.follow([0]), ['a','b'])
        self.assertEqual(t1.follow([1]), ['a','c'])        
        with self.assertRaises(ValueError):
            t1.follow([0,0])

    def test_05_a_bcd(self):
        """ 
            a
            ├b
            ├c
            └d
        """    

        t1 = gt('a', gt('b'),gt('c'), gt('d'))
        self.assertEqual(t1.follow([]), ['a'])
        self.assertEqual(t1.follow([0]), ['a','b'])
        self.assertEqual(t1.follow([1]), ['a','c'])        
        self.assertEqual(t1.follow([2]), ['a','d'])
        with self.assertRaises(ValueError):
            t1.follow([0,0])


    def test_06_a_bc_d(self):
        """ 
            a
            └b
             ├c
             └d
        """    

        t1 = gt('a', gt('b',gt('c'),gt('d')))
        self.assertEqual(t1.follow([]), ['a'])
        self.assertEqual(t1.follow([0]), ['a','b'])
        self.assertEqual(t1.follow([0,0]), ['a','b','c'])
        self.assertEqual(t1.follow([0,1]), ['a','b','d'])
        with self.assertRaises(ValueError):
            t1.follow([0,2])
        with self.assertRaises(ValueError):
            t1.follow([0,0,0])
        with self.assertRaises(ValueError):
            t1.follow([0,2,0])


    def test_07_complex(self):
        """ 
            a
            ├b
            ├c
            |└e
            | ├f
            | ├g
            | |└i
            | └h
            └d
        """    
        
        t1 = gt('a', 
                    gt('b'),
                    gt('c', gt('e',
                                    gt('f'), 
                                    gt('g', 
                                            gt('i')),
                            gt('h'))),
                gt('d'))

        self.assertEqual(t1.follow([]),  ['a'])
        self.assertEqual(t1.follow([0]), ['a','b'])
        self.assertEqual(t1.follow([1]), ['a','c'])
        self.assertEqual(t1.follow([2]), ['a','d'])
        self.assertEqual(t1.follow([1,0,2]), ['a','c','e','h'])
        self.assertEqual(t1.follow([1,0,1,0]), ['a','c','e','g','i'])
