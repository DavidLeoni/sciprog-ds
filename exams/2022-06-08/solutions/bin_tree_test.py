from bin_tree_sol import *
import unittest


def bt(*args):
    """ Shorthand function that returns a BinTree containing the provided 
        data and children. First parameter is the data, the following ones are the children.
        
        Usage examples:
        
        >>> print bt('a')
        a
        
        >>> print bt('a', bt('b'), bt('c'))            
            a
            ├b            
            └c
                            
    """
    if (len(args) == 0):
        raise ValueError("You need to provide at least one argument for the data!")
    if (len(args) > 3):
        raise ValueError("You must provide at most two nodes ! Found instead: %s " % (len(args) - 1))
        
    data = args[0]
    children = args[1:]
    
    ret = BinTree(data)    
    
    if len(children) > 0:
        if children[0] != None and not isinstance(children[0], BinTree):
            raise ValueError('Wrong type %s for left child!' % type(children[0]))
        ret._left = children[0]
    if len(children) == 2:
        if children[1] != None and not isinstance(children[1], BinTree):
            raise ValueError('Wrong type %s for right child!' % type(children[1]))
        ret._right = children[1]
    return ret



def str_btrees(bt1, bt2, error_row=-1):
    """ Returns a string version of the two trees side by side
    
        If error_row is given, the line in error is marked.
        If error_row == -1 it is ignored 
    """    
    
    s1 = str(bt1)
    s2 = str(bt2)

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


class BinTreeTest(unittest.TestCase):

    
    def assertTreeEqual(self, actual, expected):
        """ Asserts the trees actual and expected are equal """
        
        def get_children(t):
            ret = []
            if t._left:
                ret.append(t._left)
            if t._right:
                ret.append(t._right)
            return ret

        def rec_assert(c1, c2):
            
            nonlocal row
            
            if c2 is None:
                raise AssertionError("Found a None node in EXPECTED tree!\n\n" 
                                + str_btrees(actual,expected,row))
            
            if c1 is None:
                raise AssertionError("Found a None node in ACTUAL tree! \n\n"
                                + str_btrees(actual,expected,row))                     

            if not isinstance(c2, BinTree):
                raise AssertionError("EXPECTED value is an instance of  %s , which is not a BinTree !\n\n%s" % (type(c2).__name__ , str_btrees(actual,expected,row)))
                                
            if not isinstance(c1, BinTree):
                raise AssertionError("ACTUAL node is an instance of  %s  , which is not a  BinTree  !\n\n%s"
                                % (type(c1).__name__, str_btrees(actual, expected, row )))
                         
            if type(c1.data()) != type(c2.data()):
                errMsg = "ACTUAL data type:  %s  is different from EXPECTED data type:  %s\n\n" \
                         % (type(c1.data()).__name__, type(c2.data()).__name__)
                raise AssertionError(errMsg + str_btrees(actual,expected,row))
                
            if c1.data() != c2.data():
                raise AssertionError("ACTUAL data is different from expected!\n\n" 
                                + str_btrees(actual,expected,row))
            
            
            cs1 = get_children(c1)
            cs2 = get_children(c2)
            if (len(cs1) != len(cs2)):
                raise AssertionError("Number of children is different !\n\n"
                                + str_btrees(actual, expected, row) )
            
            
            if c1._left:
                row += 1
                rec_assert(c1._left, c2._left)            
            if c1._right:
                if c1._left:                        
                    row += 1
                else:
                    row += 2
                rec_assert(c1._right, c2._right)
                
        row = 0
        try:
            rec_assert(actual, expected)
        except Exception as e:
            # not all exceptions have 'message' 
            raise AssertionError(getattr(e, 'message', e.args[0])) from None
        
        
class BinTreeTestTest(BinTreeTest):    
    """ Tests the test itself ... """
    
    def test_str_btrees(self):
        self.assertTrue('a' in str_btrees(bt('a'), bt('b')))
        self.assertTrue('b' in str_btrees(bt('a'), bt('b')))
        
        self.assertTrue('a' in str_btrees(bt('a', bt('b')), bt('b', bt('c'))))
        self.assertTrue('c' in str_btrees(bt('a', bt('b')), bt('b', bt('c'))))
    
    def test_assert_tree_equal(self):
        self.assertTreeEqual(bt('a'), bt('a'))
        self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('b')))
        
        with self.assertRaises(AssertionError):
            self.assertTreeEqual(bt('a'), bt('b'))            
        with self.assertRaises(AssertionError):
            self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('c')))
        
        # different structure
        with self.assertRaises(AssertionError):
            self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('b',bt('c'))))

        with self.assertRaises(AssertionError):
            self.assertTreeEqual(bt('a', bt('b',bt('c'))), bt('a', bt('b')))        
    
    def test_print(self):
        # self.assertTreeEqual(bt('a', bt('b', bt('v')), bt('b', bt('v'))), bt('a', bt('b', bt('v'), bt('b', bt('v'))), bt('b')))
        return None 
    
    def test_bt(self):
        
        with self.assertRaises(ValueError):
            bt(0,bt(1), bt(2), bt(3))
        
        with self.assertRaises(ValueError):
            bt(2,666)
        
        with self.assertRaises(ValueError):
            bt(2,None, 666)
            
        with self.assertRaises(ValueError):
            bt(2,666, 666)
        
        with self.assertRaises(ValueError):
            bt(1,bt(2), 666)

        with self.assertRaises(ValueError):
            bt(1, 666, bt(2))

                            
class InsertLeftTest(BinTreeTest):

    def test_insert_left(self):        
        ta = BinTree('a')        
        self.assertEqual(ta.left(), None)
        self.assertEqual(ta.right(), None)
        ret = ta.insert_left('c')
        self.assertEqual(ret, None)
        tc = ta.left() 
        self.assertEqual(tc.data(), 'c')
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)
        self.assertEqual(ta.right(), None)
                
        ta.insert_left('b')
        tb = ta.left()
        self.assertEqual(ta.right(), None)
        self.assertEqual(tb.data(), 'b')
        self.assertEqual(tb.left(), tc)
        self.assertEqual(tb.right(), None)
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)

class InsertRightTest(BinTreeTest):

    def test_insert_right(self):        
        ta = BinTree('a')        
        self.assertEqual(ta.left(), None)
        self.assertEqual(ta.right(), None)
        ret = ta.insert_right('c')
        self.assertEqual(ret, None)
        tc = ta.right() 
        self.assertEqual(tc.data(), 'c')
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)
        self.assertEqual(ta.left(), None)
                
        ta.insert_right('b')
        tb = ta.right()
        self.assertEqual(ta.left(), None)
        self.assertEqual(tb.data(), 'b')
        self.assertEqual(tb.left(), None)
        self.assertEqual(tb.right(), tc)
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)


class IsHeapStackTest(BinTreeTest):
    
    def test_01_5(self):
        t = bt(5)
        self.assertEqual(t.is_heap_stack(), True)

    def test_02_5_8(self):
        t = bt(5,
                 bt(8))
        self.assertEqual(t.is_heap_stack(), True)


    def test_03_3_9(self):
        t = bt(3,
                 bt(9))
        self.assertEqual(t.is_heap_stack(), True)


    def test_04_7_7(self):
        t = bt(7,
                 bt(7))
        self.assertEqual(t.is_heap_stack(), True)

    def test_05_4_2(self):
        t = bt(4,
                bt(2))
        self.assertEqual(t.is_heap_stack(), False)


    def test_06_5_n_2(self):
        t = bt(5,
                None,
                bt(2))
        self.assertEqual(t.is_heap_stack(), False)

    def test_07_7_n_8(self):
        t = bt(7,
                None,
                bt(8))
        self.assertEqual(t.is_heap_stack(), True)


    def test_08_9_n_9(self):
        t = bt(9,
                None,
                bt(9))
        self.assertEqual(t.is_heap_stack(), True)



    def test_09_9_9_9(self):
        t = bt(9,
                bt(9),
                bt(9))
        self.assertEqual(t.is_heap_stack(), True)


    def test_10_9_15_20(self):
        t = bt(9,
                bt(15),
                bt(20))
        self.assertEqual(t.is_heap_stack(), True)


    def test_11_7_3_20(self):
        t = bt(7,
                bt(3),
                bt(20))
        self.assertEqual(t.is_heap_stack(), False)


    def test_12_7_9_3(self):
        t = bt(7,
                bt(9),
                bt(3))
        self.assertEqual(t.is_heap_stack(), False)


    def test_12b_(self):
        t = bt(4,
                  bt(6,
                         bt(5)))
        self.assertEqual(t.is_heap_stack(), False)
                  

    def test_12c_(self):
        t = bt(7,
                  bt(15,
                         None,
                         bt(9)))
        self.assertEqual(t.is_heap_stack(), False)

    def test_12d_(self):
        t = bt(16,
                  None,
                  bt(20,
                         None,
                         bt(19)))
        self.assertEqual(t.is_heap_stack(), False)

        
    def test_13_complex_pos(self):
        t = bt(7,
                bt(9, 
                        bt(10,
                                bt(40)),
                        bt(14)),
                bt(20, 
                        None,
                        bt(30,
                                bt(50),
                                bt(90))))
                            
        self.assertEqual(t.is_heap_stack(), True)


    def test_14_complex_neg1(self):
        t = bt(7,
                bt(9, 
                        bt(10,
                                bt(9)),
                        bt(14)),
                bt(20, 
                        None,
                        bt(3,
                                bt(11),
                                bt(90))))
                            
        self.assertEqual(t.is_heap_stack(), False)


    def test_15_complex_neg2(self):
        t = bt(7,
                bt(9, 
                        bt(10,
                                bt(40)),
                        bt(14)),
                bt(20, 
                        None,
                        bt(30,
                                bt(5),
                                bt(90))))
                            
        self.assertEqual(t.is_heap_stack(), False)
