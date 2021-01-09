from gen_tree_sol import *
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
    
    i = len(children) - 1
    for c in reversed(children):
        if not isinstance(children[0], GenericTree):
            raise Exception('Wrong type %s for child at index %i!' % (type(children[0]), i))
        c._sibling = r._child
        c._parent = r
        r._child = c     
        
        i = i - 1
    return r

def get_children(gt):
    """ Handy methods to get children. Try not to use this in exercise code !!!!
    """
    current = gt._child
    ret = []
    i = 0
    while current != None:
        if not isinstance(current, GenericTree):
            raise Exception('Found a child of wrong type %s at index %s' % (type(current), i))
        ret.append(current)        
        current = current.sibling()
        i += 1
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
                          
        self.assertTrue(t.is_root(), "Detached node %s is not a root, does it have still the _parent or _sibling set to something ?" % t.data())

    
    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEqual(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! You are returning instead %s" % ret)
    
    
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
                raise Exception("ACTUAL data is different from expected!\n\n"
                                + str_trees(actual,expected,row))
            
            if not (c1 == actual or c1.parent() != None):
                raise Exception("Parent of ACTUAL node is None!"
                           + "\n\n" +  str_trees(actual,expected,row) )

            if not (c2 == expected or c2.parent() != None): 
                raise Exception("Parent of EXPECTED node is  %s !\n\n%s" % (c2.parent(),str_trees(actual,expected,row)) ) 
            
            if not (c1.parent() == None or isinstance(c1.parent(), GenericTree)): 
                raise Exception(("ACTUAL parent is an instance of %s , which is not a GenericTree!" % type(c1.parent()))
                                + "\n\n" +  str_trees(actual,expected,row) )

            if not (c2.parent() == None or isinstance(c2.parent(), GenericTree)): 
                raise Exception(("EXPECTED parent is an instance of %s , which is not a GenericTree!" % type(c2.parent()))
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
            
            current1 = c1.child()
            current2 = c2.child()
                        
            while ( current1 != None and current2 != None):                
                rec_assert(current1, current2, row + 1)   
                current1 = current1.sibling()
                current2 = current2.sibling()
                i += 1 

            if (current1 == None and current2 != None) or (current1 != None and current2 == None):                                            
                raise Exception("Children sizes are different !\n\n"
                                + str_trees(actual, expected, row + i))                
        
        try:
            rec_assert(actual, expected, 0)
        except Exception as e:
            # not all exceptions have 'message' 
            raise AssertionError(getattr(e, 'message', e.args[0])) from None                
        
        
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
            

    def test_gt(self):
        
        with self.assertRaises(Exception):
            gt()
        
        with self.assertRaises(Exception):
            gt(2,666)
        
        with self.assertRaises(Exception):
            gt(2,None, 666)
            
        with self.assertRaises(Exception):
            gt(2,666, 666)
        
        with self.assertRaises(Exception):
            gt(1,gt(2), 666)

        with self.assertRaises(Exception):
            gt(1, 666, gt(2))
                            
class InsertChildTest(GenericTreeTest):

    def test_01(self):        
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

class InsertChildrenTest(GenericTreeTest):
        
    def test_01(self):
        
        t = gt('a')
        t.insert_children([gt('d'), gt('e')])        
        self.assertTreeEqual(t, gt('a', gt('d'), gt('e')))
        t.insert_children([gt('b'), gt('c')])
        self.assertTreeEqual(t, gt('a', gt('b'), gt('c'), gt('d'), gt('e')))        

class InsertSiblingTest(GenericTreeTest):
        
    def test_01_right_sibling(self):
        ta = gt('a')                        
        tb = gt('b')        
        ta.insert_child(tb)        

        tb.insert_sibling(gt('c'))        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('c')))

    def test_02_middle_sibling(self):
        
        tb = gt('b')
        ta = gt('a', tb, gt('d'))        

        tb.insert_sibling(gt('c'))        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('c') , gt('d')))
                
    def test_03_to_root(self):
        ta = gt('a')
        
        with self.assertRaises(Exception):
            ta.insert_sibling(gt('b'))
    
class InsertSiblingsTest(GenericTreeTest):
    
    def test_01(self):
        tb = gt('b')
        ta = gt('a', tb, gt('e'))        

        tb.insert_siblings([gt('c'), gt('d')])        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('c') , gt('d'), gt('e')))

    def test_02_to_root(self):
        ta = gt('a')
        
        with self.assertRaises(Exception):
            ta.insert_siblings([gt('b'), gt('c')])          

        
        
class DetachChildTest(GenericTreeTest):
            
    def test_01(self):
        
        tb = gt('b')
        tc = gt('c')
        
        t = gt('a', tb, tc)
        
        ret = t.detach_child()                
        self.assertReturnNone(ret, "detach_child") 
        
        self.assertTreeEqual(t, gt('a', gt('c')))
        self.assertTreeEqual(tb, gt('b'))  

        ret = t.detach_child()         
        self.assertTreeEqual(t, gt('a'))
        self.assertTreeEqual(tb, gt('b'))  
        self.assertTreeEqual(tc, gt('c'))
        
        
        with self.assertRaises(Exception):
            ret = t.detach_child()

        
class DetachSiblingTest(GenericTreeTest):
        
    def test_01_root(self):
        ta = gt('a')

        with self.assertRaises(Exception):        
            ta.detach_sibling()                        

    def test_02_child(self):
        
        tb = gt('b')
        ta = gt('a', tb)

        with self.assertRaises(Exception):        
            tb.detach_sibling()
            
    def test_03_three(self):
        tb = gt('b')
        tc = gt('c')
        ta = gt('a', tb, tc)
        
        tb.detach_sibling()                        
        self.assertTreeEqual(ta, gt('a', gt('b')))
        self.assertTreeEqual(tc, gt('c'))

    def test_04_four(self):
        tb = gt('b')
        tc = gt('c')
        td = gt('d')
        ta = gt('a', tb, tc, td)
        
        tb.detach_sibling()                        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('d')))
        self.assertTreeEqual(tc, gt('c'))
        
        tb.detach_sibling() 
        self.assertTreeEqual(ta, gt('a', gt('b')))
        self.assertTreeEqual(tc, gt('c'))
        self.assertTreeEqual(td, gt('d'))        
                    
            
class DetachTest(GenericTreeTest):        
    
    def test_01_one_node(self):
        t = gt('a')    
        
        with self.assertRaises(Exception):
            t.detach('a')
            
        self.assertTreeEqual(t, gt('a'))

    def test_02_two_nodes(self):
        tb = gt('b')
        ta = gt('a', tb)
        ta.detach('b')
        self.assertTreeEqual(tb, gt('b')) 
        self.assertTreeEqual(ta, gt('a'))

    def test_03_three_nodes_child(self):
        tb = gt('b')
        tc = gt('c')
        ta = gt('a', tb, tc)
        ta.detach('b')
        self.assertTreeEqual(tb, gt('b'))         
        self.assertTreeEqual(ta, gt('a', gt('c')))


    def test_04_three_nodes_second(self):
        tb = gt('b')
        tc = gt('c')
        ta = gt('a', tb, tc)
        ta.detach('c')
        self.assertTreeEqual(tc, gt('c'))         
        self.assertTreeEqual(ta, gt('a', gt('b')))
        
    def test_05_three_nodes_duplicates(self):
        tb1 = gt('b')
        tb2 = gt('b')
        ta = gt('a', tb1, tb2)
        ta.detach('b')
        self.assertTreeEqual(tb1, gt('b'))
        self.assertTreeEqual(ta, gt('a', tb2))     
        

class AncestorsTest(GenericTreeTest):

    def test_01_root(self):        
        ta = gt('a')
        self.assertEqual(ta.ancestors(), [])

    """
        a
        └b  <-
    """                
    def test_02_two(self):        

        tb = gt('b')        
        ta = gt('a', tb)
        self.assertEqual(tb.ancestors(), [ta])

    """
        a
        ├b
        └c  <-
    """        
    def test_03_brothers(self):        

        tb = gt('b')       
        tc = gt('c')
        ta = gt('a', tb, tc)
        self.assertEqual(tb.ancestors(), [ta])

    """
        a
        ├b
        │├d
        │└e
        └c
         └f
    """   
    def test_04_level2(self):        

        te = gt('e')
        td = gt('d')
        tf = gt('f')
        tb = gt('b', td, te)        
        tc = gt('c', tf)
        ta = gt('a', tb, tc)            

        self.assertEqual(tc.ancestors(), [ta])
        self.assertEqual(tf.ancestors(), [tc, ta])
        self.assertEqual(te.ancestors(), [tb, ta])

class GrandChildrenTest(GenericTreeTest):
            
    def test_01_root(self):
        self.assertEqual(gt('a').grandchildren(), [])

    """
        a
        └b
    """            
    def test_02_one_child_no_children(self):
        self.assertEqual(gt('a',  gt('b')).grandchildren(), [])        

    """
        a
        └b
         └c
    """            
    def test_03_one_child_one_grandchildren(self):
        self.assertEqual(gt('a',  gt('b', gt('c'))).grandchildren(), ['c'])        

    """
        a
        └b
         ├c
         └d
    """            
    def test_04_one_child_two_grandchildren(self):
        self.assertEqual(gt('a',  gt('b', gt('c'), gt('d'))).grandchildren(), ['c', 'd'])        

    """
        a
        ├b
        │└c
        └d
          └e
    """            
    def test_05_two_children_two_grandchildren(self):
        self.assertEqual(gt('a',  gt('b', gt('c')), gt('d', gt('e'))).grandchildren(), ['c', 'e'])        

    """
            a
            ├b
            │├c
            │└d
            │ └g
            ├e
            │└h  
            └f    
    """
    def test_05_complex_grandgrandchildren(self):
        self.assertEqual(gt('a',  gt('b', gt('c'), gt('d', gt('g'))), 
                                   gt('e', gt('h')),
                                   gt('f')).grandchildren(), ['c', 'd', 'h'])
        
        
class ZigTest(GenericTreeTest):
    
    def test_01_last_root(self):        
        self.assertEqual(gt('a').zig(), ['a'])

    
    def test_02_last__one_child(self):
        """ 
            a
            └b <-
        """
        self.assertEqual(gt('a', gt('b')).zig(), ['a', 'b'])

    def test_03_last_two_children(self):
        """ 
            a
            ├b 
            └c 
        """    
        self.assertEqual(gt('a', gt('b'), gt('c')).zig(), ['a', 'b'])
        
    def test_04_depth_three(self):
        """ 
            a
            ├b
            │├c
            │└d
            └e 
        """    
        self.assertEqual(gt('a', gt('b', gt('c'), gt('d')), gt('e')).zig(), ['a','b', 'c'])        

class ZagTest(GenericTreeTest):        
    
    def test_01_root(self):        
        self.assertEqual(gt('a').zag(), ['a'])


    def test_02_one_child(self):
        """ 
            a    
            └b 
        """
        self.assertEqual(gt('a', gt('b')).zag(), ['a'])
        self.assertEqual(gt('a', gt('b')).child().zag(), ['b'])

    def test_03_two_children(self):
        """ 
            a
            ├b 
            └c 
        """    
        self.assertEqual(gt('a', gt('b'), gt('c')).child().zag(),
                         ['b', 'c'])
        
    def test_04_depth_three(self):
        """ 
            a
            ├b   <-- start from
            │├c
            │└d
            └e   
        """    
        t = gt('a', gt('b', gt('c'), gt('d')), gt('e'))
            
        self.assertEqual(t.child().zag(),
                         ['b','e'])        

class ZigZagTest(GenericTreeTest):
    
    def test_01_root(self):        
        self.assertEqual(gt('a').zigzag(),
                         ['a'])

    
    def test_02_one_child(self):
        """ 
            a
            └b 
            
        """
        self.assertEqual(gt('a', gt('b')).zigzag(),
                         ['a','b'])

    def test_03_two_children(self):
        """ 
            a
            ├b 
            └c 
        """    
        self.assertEqual(gt('a', gt('b'), gt('c')).zigzag(),
                         ['a', 'b', 'c'])

    def test_04_middle_child(self):
        """ 
            a
            ├b  
            ├c
            │└e
            └d 
            
            Notice the siblings chain must arrive to the end up to 'd' !
        """    
        self.assertEqual(gt('a', gt('b', gt('d')), gt('c')).zigzag(),
                         ['a', 'b', 'd'])

        
    def test_05_complex(self):
        """ 
            a
            ├b
            ├c
            │└e
            └d
             ├f
             └g
            
        """    
        self.assertEqual( gt('a', gt('b'), gt('c', gt('e')), gt('d', gt('f'), gt('g'))).zigzag(),
                         ['a','b','c', 'd','f', 'g'])


      
        
class UnclesTest(GenericTreeTest):

    """
        a
        └b    <- 
         └c          
    """            
    def test_01_unique_single_child(self):
        
        tb = gt('b')
        ta = gt('a',  tb, gt('c') )
        
        self.assertEqual(tb.uncles(), [])        


    """
        a
        └b
         └c <-         
    """            
    def test_02_unique_single_grandchild(self):
        
        tc = gt('c')
        ta = gt('a',  gt('b'), tc)
        
        self.assertEqual(tc.uncles(), [])        

    """
        a
        ├b
        │└c <-         
        └d  
    """            
    def test_03_one_uncle_after(self):
        
        tc = gt('c')
        ta = gt('a',  gt('b', tc), gt('d'))
        
        self.assertEqual(tc.uncles(), ['d'])        



    """
        a
        ├b
        └c
         └d <-         
          
    """            
    def test_04_one_uncle_before(self):
        
        td = gt('d')
        ta = gt('a',  gt('b'), gt('c', td))
        
        self.assertEqual(td.uncles(), ['b'])


    """
        a
        ├b
        ├c
        │└d <-
        └e
          
    """            
    def test_05_middle(self):
        
        td = gt('d')
        ta = gt('a',  gt('b'), gt('c', td), gt('e'))
        
        self.assertEqual(td.uncles(), ['b', 'e'])
        
    """
            a
            ├b
            │├c
            │└d
            │ └g
            ├e
            │└h  <- 
            └f    
    """
    def test_06_complex_1(self):
        
        th = gt('h')
        ta = gt('a',  gt('b', gt('c'), gt('d', gt('g'))), 
                      gt('e', th),
                      gt('f'))
        self.assertEqual(th.uncles(), ['b', 'f'])

    """
            a
            ├b
            │├c
            │└d
            │ └g <-            
            ├e
            │└h   
            └f    
    """
    def test_07_complex_2(self):
        
        tg = gt('g')
        ta = gt('a',  gt('b', gt('c'), gt('d', tg)), 
                      gt('e', gt('h')),
                      gt('f'))
        self.assertEqual(tg.uncles(), ['c'])

        
class CommonAncestorTest(GenericTreeTest):
    
    def test_01_itself(self):
        tb = gt('b')
        ta = gt('a', tb)
        self.assertEqual(tb.common_ancestor(tb), ta)       
        
    def test_02_forest(self):
        tb = gt('b')
        ta = gt('a')
        with self.assertRaises(LookupError):
            ta.common_ancestor(tb)               
        
    def test_03_immediate(self):
        tb = gt('b')
        tc = gt('b')        
        ta = gt('a', tb, tc)
        self.assertTreeEqual(tb.common_ancestor(tc), ta)       
        
    def test_04_brothers(self):
        tb = gt('b')
        tc = gt('c')     
        ta = gt('a', tb, tc)
        self.assertTreeEqual(tb.common_ancestor(tc), ta)       
        
    """
        a
        ├b
        │├d
        │└e
        └c
         └f
    """   
    def test_05_level_2(self):
        
        te = gt('e')
        td = gt('d')
        tf = gt('f')
        tb = gt('b', td, te)        
        tc = gt('c', tf)
        ta = gt('a', tb, tc)
        self.assertTreeEqual(td.common_ancestor(te), tb)
        self.assertTreeEqual(tf.common_ancestor(tf), tc)
        self.assertTreeEqual(td.common_ancestor(tf), ta)
        self.assertTreeEqual(te.common_ancestor(tb), ta)
        

    """
        a
        └b
         ├c
         │├d
         │└e
         └f
        
    """   
    def test_06_level_3(self):
        
        te = gt('e')
        td = gt('d')
        tf = gt('f')
        tc = gt('c', td, te)
        tb = gt('b', tc, tf)
        ta = gt('a', tb)
        self.assertTreeEqual(tf.common_ancestor(tc), tb)
        self.assertTreeEqual(tf.common_ancestor(td), tb)
        self.assertTreeEqual(td.common_ancestor(te), tc)
            
class MirrorTest(GenericTreeTest):
    """
    a  <-   Becomes:   a
    """
    def test_01_root(self):
        t = gt('a')
        t.mirror()
        self.assertTreeEqual(t, gt('a'))

    """
    a   <-   Becomes  a
    └b                └b
    """       
    def test_02_ab(self):
        t = gt('a',gt('b'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('b')))
    

    """
    a   <-   Becomes: a
    ├b                ├c
    └c                └b
    
    """    
    def test_03_abc(self):
        t = gt('a',gt('b'),gt('c'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('c'), gt('b')))


    """
    a   <-     Becomes:   a
    ├b                    ├f
    │├c                   └b
    │├d                    ├e
    │└e                    ├d
    └f                     └c 
                          
    """    
    def test_04_abcdef(self):
        t = gt('a',gt('b', gt('c'), gt('d'), gt('e')),gt('f'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('f'), gt('b', gt('e'), gt('d'), gt('c'))))
    
    
    """
    a                       a 
    ├b   <-     Becomes:    ├b
    │├c                     │├d
    │└d                     │└c
    └e                      └e
    """
    def test_05_non_root(self):
        tb = gt('b', gt('c'), gt('d'))        
        ta = gt('a',tb,gt('e'))
        tb.mirror()
        self.assertTreeEqual(ta, gt('a', gt('b', gt('d'), gt('c')),  gt('e')))
    
class CloneTest(GenericTreeTest):
    """
    a
    """
    def test_01_root(self):
        ta = gt('a')
        t2 = ta.clone()        

        self.assertTreeEqual(ta,t2)
        ta._data = 'b'  # if we change the original data, clone should be unaffected
        self.assertTreeEqual(t2, gt('a'))        
        ta.insert_child(gt('c')) # same if we insert an extra child 
        self.assertTreeEqual(t2, gt('a'))        
        

    """
    a
    └b
    """
    def test_02_ab(self):
        tb= gt('b')
        ta = gt('a', tb)
        
        t2 = ta.clone()        

        self.assertTreeEqual(ta,t2)
        ta._data = 'x'  # if we change the original, clone should be unaffected
        tb._data = 'y'        
        self.assertTreeEqual(t2, gt('a',gt('b')))

    """
    a
    ├b
    └c
     └d
    """
    def test_03_abcd(self):
        td = gt('d')
        tc= gt('c', td)
        tb= gt('b')
        ta = gt('a', tb, tc)
        t2 = ta.clone()  
        
        self.assertTreeEqual(ta,t2)
        ta._data = 'x'  # if we change the original, clone should be unaffected
        tb._data = 'y' 
        tc._data = 'y'
        td._data = 'w'
        self.assertTreeEqual(t2, gt('a',gt('b'), gt('c', gt('d'))))

class RightmostTest(GenericTreeTest):

    def test_01_a(self):
        t1 = gt('a')
        self.assertEqual(t1.rightmost(), ['a'])

    def test_02_ab(self):
        """ 
            a
            └b
        """    

        t1 = gt('a', gt('b'))
        self.assertEqual(t1.rightmost(), ['a','b'])

    def test_03_a_bc(self):
        """ 
            a
            ├b
            └c
        """    

        t1 = gt('a', gt('b'),gt('c'))
        self.assertEqual(t1.rightmost(), ['a','c'])

    def test_04_a_bcd(self):
        """ 
            a
            ├b
            ├c
            └d
        """    

        t1 = gt('a', gt('b'),gt('c'),gt('d'))
        self.assertEqual(t1.rightmost(), ['a','d'])


    def test_05_a_bc_d(self):
        """ 
            a
            └b
             ├c
             └d
        """    

        t1 = gt('a', gt('b',gt('c'),gt('d')))
        self.assertEqual(t1.rightmost(), ['a','b','d'])


    def test_06_complex(self):
        """ 
            a
            ├b
            ├c
            │└e
            └d
             ├f
             └g
              ├h
              └i
        """    
        
        t1 = gt('a', gt('b'),gt('c', gt('e')),gt('d', gt('f'), gt('g', gt('h'), gt('i'))))
        self.assertEqual(t1.rightmost(), ['a','d','g','i'])
        
        
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
            │└e
            │ ├f
            │ ├g
            │ │└i
            │ └h
            ├c
            │
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
            │└e
            │ ├f
            │ ├g
            │ │└i
            │ └h
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
            │└d
            └c             
        """    

        ta = gt('a', gt('b',gt('d')), gt('c'))    
    
        self.assertTrue(ta.is_triangle(['a','b','c']))

    def test_10_a_bde_c(self):
        """ 
            a
            ├b
            │├d
            │└e
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
            │├d
            │├e
            │└f
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

    def test_02_a_b_c(self):
        """ 
            a
            └b
             ├c            
             └d
        """    

        ta = gt('a', gt('b', gt('c'), gt('d')))    
    
        self.assertFalse(ta.has_triangle(['a','b','c']))
        self.assertTrue(ta.has_triangle(['b','c','d']))

    def test_03_a_b_c(self):
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
            │├d
            │├e
            │└f
            └c
             └g
              ├h
              └i
               └l
        """    

        tb = gt('b', gt('d'), gt('e'), gt('f'))
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