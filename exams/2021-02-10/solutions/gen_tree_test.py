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
        
        
        
        def rec_assert(c1, c2):                    
        
            nonlocal row
        
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
                       
            if type(c1.data()) != type(c2.data()):
                errMsg = "ACTUAL data type:  %s  is different from EXPECTED data type:  %s  !\n\n" \
                         % (type(c1.data()).__name__, type(c2.data()).__name__)
                raise Exception(errMsg + str_trees(actual,expected,row))
                
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
                row += 1
                rec_assert(current1, current2)
                current1 = current1.sibling()
                current2 = current2.sibling()
                i += 1 

            if (current1 == None and current2 != None) or (current1 != None and current2 == None):                                            
                raise Exception("Children sizes are different !\n\n"
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




class MarvelousTest(GenericTreeTest):
        
    def test_01_a(self):
        t = gt('a')
        res = t.marvelous()        
        self.assertTreeEqual(t, gt('a'))
        self.assertEqual(res, None)  # must return nothing 
    
    def test_02_b(self):
        tb = gt('b')
        ta = gt('a', 
                    tb)
        
        res = ta.marvelous()        
        self.assertTreeEqual(ta, gt('b', 
                                        gt('b')))
        self.assertEqual(res, None)              # must return nothing 
        self.assertEqual(id(tb), id(ta._child))  # no new nodes 
        
    def test_03_bc(self):
        tb = gt('b')
        tc = gt('c')
        
        ta = gt('a', 
                    tb,
                    tc)
        
        res = ta.marvelous()        
        self.assertTreeEqual(ta, gt('bc', 
                                         gt('b'),
                                         gt('c')))

        self.assertEqual(res, None)                       # must return nothing 
        self.assertEqual(id(tb), id(ta._child))           # no new nodes 
        self.assertEqual(id(tc), id(ta._child._sibling))  # no new nodes 
 
 
    def test_04_cb(self):
        t = gt('a',                   
                   gt('c'),
                   gt('b'),)
        
        t.marvelous()        
        self.assertTreeEqual(t, gt('cb', 
                                         gt('c'),
                                         gt('b')))
        

    def test_05_cbd(self):
        t = gt('a',                   
                   gt('c'),
                   gt('b'),
                   gt('d'))

        t.marvelous()        
        self.assertTreeEqual(t, gt('cbd', 
                                          gt('c'),
                                          gt('b'),
                                          gt('d')))


    def test_06_cd(self):
        t = gt('a',                   
                   gt('b',
                            gt('d')),
                   gt('c'))

        t.marvelous()        
        self.assertTreeEqual(t, gt('dc', 
                                        gt('d',
                                               gt('d')),
                                        gt('c')))



    def test_07_bd(self):
        t = gt('a',                   
                   gt('b'),
                            
                   gt('c',
                           gt('d'),))
        
        ret = t.marvelous()        
        self.assertTreeEqual(t, gt('bd', 
                                         gt('b'),                                           
                                         gt('d',
                                                gt('d'))))
 
 
    def test_08_cdfg(self):
        t = gt('a',                   
                   gt('b',
                            gt('c'),
                            gt('d')),
                            
                   gt('e',
                           gt('f'),
                           gt('g')))
        
        t.marvelous()        
        self.assertTreeEqual(t, gt('cdfg',                   
                                           gt('cd',
                                                   gt('c'),
                                                   gt('d')),
                                                        
                                           gt('fg',
                                                   gt('f'),
                                                   gt('g'))))

    def test_09_complex(self):
        t = gt('a',
                    gt('b',
                            gt('M'),
                            
                            gt('A'),
                            gt('R')),
                    gt('c',
                            gt('e',
                                gt('V'),),
                            gt('E')),
                    gt('d', 
                            gt('L'),
                            gt('f', 
                                gt('O'),
                                gt('U'),),
                            gt('S')))
        t.marvelous()
        self.assertTreeEqual(t, gt('MARVELOUS',
                                        gt('MAR',
                                                gt('M'),
                                                
                                                gt('A'),
                                                gt('R')),
                                        gt('VE',
                                                gt('V',
                                                    gt('V'),),
                                                gt('E')),
                                        gt('LOUS', 
                                                gt('L'),
                                                gt('OU', 
                                                    gt('O'),
                                                    gt('U'),),
                                                gt('S'))))

