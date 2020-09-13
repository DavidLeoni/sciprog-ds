from tree_solution import *
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


class IsTriangleTest(GenericTreeTest):

   

    def test_01_a_empty(self):
        """ 
            a
        """         
        ta = gt('a')        
        self.assertFalse(ta.is_triangle(['a','b','c']))

    def test_02_a_list_ab(self):
        """ 
            a
            ├b
            └c
        """    

        ta = gt('a', gt('b'), gt('c'))        
        try:
            self.assertFalse(ta.is_triangle(['a','b']))
            self.fail("Should have failed !")
        except ValueError:
            pass

    def test_03_a_lista(self):
        """ 
            a
            ├b            
            └c
        """    

        ta = gt('a', gt('b'), gt('c'))        
        try:
            self.assertFalse(ta.is_triangle(['a']))
            self.fail("Should have failed !")
        except ValueError:
            pass


    def test_04_a_b(self):
        """ 
            a                       
            └b
        """    

        ta = gt('a', gt('b'))    
    
        self.assertFalse(ta.is_triangle(['a','b','c']))

    def test_05_a_b_c(self):
        """ 
            a
            ├b            
            └c
        """    

        ta = gt('a', gt('b'), gt('c'))    
    
        self.assertTrue(ta.is_triangle(['a','b','c']))

    def test_06_x_y_z(self):
        """ 
            x
            ├y            
            └z
        """    

        ta = gt('x', gt('y'), gt('z'))    
    
        self.assertTrue(ta.is_triangle(['x','y','z']))

    def test_07_a_b_c_different_order(self):
        """ 
            a
            ├b            
            └c
        """    

        ta = gt('a', gt('b'), gt('c'))        
        self.assertFalse(ta.is_triangle(['a','c','b']))

    def test_08_a_b_cd(self):
        """ 
            a
            ├b
            └c
             └d
        """    
        ta = gt('a', gt('b'), gt('c', gt('d')))    
    
        self.assertTrue(ta.is_triangle(['a','b','c']))

    def test_09_a_bd_c(self):
        """ 
            a
            ├b
            |└d
            └c             
        """    

        ta = gt('a', gt('b',gt('d')), gt('c'))    
    
        self.assertTrue(ta.is_triangle(['a','b','c']))

    def test_10_a_bde_c(self):
        """ 
            a
            ├b
            |├d
            |└e
            └c             
        """           
        ta = gt('a', gt('b',gt('d'),gt('e')), gt('c'))    
    
        self.assertTrue(ta.is_triangle(['a','b','c']))

    def test_11_a_b_c_d(self):
        """ 
            a
            ├b
            ├c            
            └d             
        """           
        ta = gt('a', gt('b'), gt('c'), gt('d'))    
    
        self.assertFalse(ta.is_triangle(['a','b','c']))

    def test_12_complex(self):
        """ 
            a
            ├b
            |├d
            |├e
            |└f
            └c
             └g
              ├h
              └i
               └l
        """    

        tb = gt('b', gt('d', gt('e'), gt('f')))
        tg = gt('g', gt('h'), gt('i', gt('l')))
        ta = gt('a', tb, gt('c', tg))

        self.assertTrue(ta.is_triangle(['a','b','c']))    
        self.assertFalse(ta.is_triangle(['b','c','a']))    
        self.assertFalse(tb.is_triangle(['b','d','e']))    
        self.assertTrue(tg.is_triangle(['g','h','i'])) 
        self.assertFalse(tg.is_triangle(['g','i','h'])) 
        



class HasTriangleTest(GenericTreeTest):

    def test_01_a_b_c(self):
        """ 
            a
            ├b            
            └c
        """    

        ta = gt('a', gt('b'), gt('c'))    
    
        self.assertTrue(ta.has_triangle(['a','b','c']))

    def test_05_a_b_c(self):
        """ 
            a
            └b
             ├c            
             └d
        """    

        ta = gt('a', gt('b', gt('c'), gt('d')))    
    
        self.assertFalse(ta.has_triangle(['a','b','c']))
        self.assertTrue(ta.has_triangle(['b','c','d']))
    def test_05_a_b_c(self):
        """ 
            a
            ├b
            └c
             ├d         
             └e
        """    

        ta = gt('a', gt('b'), gt('c', gt('d'), gt('e')))    
    
        self.assertTrue(ta.has_triangle(['a','b','c']))
        self.assertTrue(ta.has_triangle(['c','d','e']))

    def test_12_complex(self):
        """ 
            a
            ├b
            |├d
            |├e
            |└f
            └c
             └g
              ├h
              └i
               └l
        """    

        tb = gt('b', gt('d', gt('e'), gt('f')))
        tg = gt('g', gt('h'), gt('i', gt('l')))
        tc = gt('c', tg)
        ta = gt('a', tb, tc)

        
        self.assertTrue(ta.has_triangle(['a','b','c']))    
        self.assertFalse(ta.has_triangle(['a','c','b']))    
        self.assertFalse(ta.has_triangle(['b','c','a']))    
        self.assertFalse(tb.is_triangle(['b','d','e']))    
        self.assertTrue(tg.has_triangle(['g','h','i']))  
        self.assertTrue(tc.has_triangle(['g','h','i']))  # check recursion 
        self.assertTrue(ta.has_triangle(['g','h','i']))  # check recursion        

