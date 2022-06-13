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
        raise ValueError("You need to provide at least one argument for the data!")
        
    data = args[0]
    children = args[1:]
    
    r = GenericTree(data)    
    
    i = len(children) - 1
    for c in reversed(children):
        if not isinstance(c, GenericTree):
            raise ValueError('Wrong type %s for child at index %i!' % (type(children[0]), i))
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
            raise ValueError('Found a child of wrong type %s at index %s' % (type(current), i))
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
        """ Checks provided node t is a root, if not raises AssertionError """
                          
        self.assertTrue(t.is_root(), "Detached node %s is not a root, does it have still the _parent or _sibling set to something ?" % t.data())

    
    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEqual(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! You are returning instead %s" % ret)
    
    
    def assertTreeEqual(self, actual, expected):
        """ Asserts the trees actual and expected are equal """
        
        
        
        def rec_assert(c1, c2):                    
        
            nonlocal row
        
            if c2 is None:
                raise AssertionError("Found a None node in EXPECTED tree!\n\n" 
                                + str_trees(actual,expected,row))
            
            if c1 is None:
                raise AssertionError("Found a None node in ACTUAL tree! \n\n"
                                + str_trees(actual,expected,row))                     

            if not isinstance(c2, GenericTree):
                raise AssertionError("EXPECTED value is an instance of  %s , which is not a GenericTree !\n\n%s" % (type(c2).__name__ , str_trees(actual,expected,row)))
                                
            if not isinstance(c1, GenericTree):
                raise AssertionError("ACTUAL node is an instance of  %s  , which is not a  GenericTree  !\n\n%s"
                                % (type(c1).__name__, str_trees(actual, expected, row )))
                       
            if type(c1.data()) != type(c2.data()):
                errMsg = "ACTUAL data type:  %s  is different from EXPECTED data type:  %s  !\n\n" \
                         % (type(c1.data()).__name__, type(c2.data()).__name__)
                raise AssertionError(errMsg + str_trees(actual,expected,row))
                
            # note != instead of 'is not'
            if c1.data() != c2.data():
                raise AssertionError("ACTUAL data is different from expected!\n\n"
                                + str_trees(actual,expected,row))
            
            if c1 is not actual and c1.parent() is None:
                raise AssertionError("Parent of ACTUAL node is None!"
                           + "\n\n" +  str_trees(actual,expected,row) )

            if c2 is not expected and c2.parent() is None: 
                raise AssertionError("Parent of EXPECTED node is  %s !\n\n%s" % (c2.parent(),str_trees(actual,expected,row)) ) 
            
            if c1.parent() is not None and not isinstance(c1.parent(), GenericTree): 
                raise AssertionError(("ACTUAL parent is an instance of %s , which is not a GenericTree!" % type(c1.parent()))
                                + "\n\n" +  str_trees(actual,expected,row) )

            if c2.parent() is not None and not isinstance(c2.parent(), GenericTree): 
                raise AssertionError(("EXPECTED parent is an instance of %s , which is not a GenericTree!" % type(c2.parent()))
                                + "\n\n" +  str_trees(actual,expected,row) )
            
            if (c1.parent() is None):
                if (c2.parent() is not None):
                    raise AssertionError("Different parents! "
                                    + "Actual parent = None   Expected parent.data() = " + str(c2.parent().data()) 
                                    + "\n\n" + str_trees(actual,expected,row) )
                                    
            else:    
                if (c2.parent() is None):                    
                    raise AssertionError("Different parents! "
                                    + "Actual parent.data() = " + str(c1.parent().data()) 
                                    + "   Expected parent = None"
                                    + "\n\n" + str_trees(actual,expected,row)) 
                else: # let's just check data for now
                    self.assertEqual(c1.parent().data(), c2.parent().data(),
                                  "Different parents ! " 
                                 + "Actual parent.data() = " + str(c1.parent().data()) 
                                    + "   Expected parent.data() = " + str(c2.parent().data()
                                    + "\n\n" + str_trees(actual,expected,row) ))
            
            if c1 is actual and c2 is expected:
                if (c1.sibling() is None):
                    if (c2.sibling() is not None):
                        raise AssertionError("Different siblings! "
                                        + "Actual sibling = None   Expected sibling.data() = " + str(c2.sibling().data()) 
                                        + "\n\n" + str_trees(actual,expected,row) )
                                        
                else:    
                    if (c2.sibling() is None):                    
                        raise AssertionError("Different siblings! "
                                        + "Actual sibling.data() = " + str(c1.sibling().data()) 
                                        + "   Expected sibling = None"
                                        + "\n\n" + str_trees(actual,expected,row)) 
                    else: # let's just check data for now
                        self.assertEqual(c1.sibling().data(), c2.sibling().data(),
                                    "Different siblings ! " 
                                    + "Actual sibling.data() = " + str(c1.sibling().data()) 
                                        + "   Expected sibling.data() = " + str(c2.sibling().data()
                                        + "\n\n" + str_trees(actual,expected,row) ))


            i = 0                                    
            
            current1 = c1.child()
            current2 = c2.child()
                            
            while ( current1 is not None and current2 is not None):
                row += 1
                # the only direct sibling check we need to do is only in the root,
                # others are implied by the fact we are scanning
                rec_assert(current1, current2)
                current1 = current1.sibling()
                current2 = current2.sibling()
                i += 1 

            if (current1 is None and current2 is not None) or (current1 is not None and current2 is None):                                            
                raise AssertionError("Children sizes are different !\n\n"
                                + str_trees(actual, expected, row))                
        
        row = 0    
        try:
            rec_assert(actual, expected)
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
        
        with self.assertRaises(AssertionError):
            self.assertTreeEqual(gt('a'), gt('b'))            
        with self.assertRaises(AssertionError):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('c')))
        
        # different structure
        with self.assertRaises(AssertionError):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b',gt('c'))))

        with self.assertRaises(AssertionError):
            self.assertTreeEqual(gt('a', gt('b',gt('c'))), gt('a', gt('b')))        
    
    def test_print(self):
        # self.assertTreeEqual(gt('a', gt('b', gt('v')), gt('b', gt('v'))), gt('a', gt('b', gt('v'), gt('b', gt('v'))), gt('b')))
        return None 
            

    def test_gt(self):
        
        with self.assertRaises(ValueError):
            gt()
        
        with self.assertRaises(ValueError):
            gt(2,666)
        
        with self.assertRaises(ValueError):
            gt(2,None, 666)
            
        with self.assertRaises(ValueError):
            gt(2,666, 666)
        
        with self.assertRaises(ValueError):
            gt(1,gt(2), 666)

        with self.assertRaises(ValueError):
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
        
