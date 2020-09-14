                            
from bin_tree_sol import *
import unittest


def bt(*args):
    """ Shorthand function that returns a BinaryTree containing the provided 
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
        raise Exception("You need to provide at least one argument for the data!")
    if (len(args) > 3):
        raise Exception("You must provide at most two nodes ! Found instead: %s " % (len(args) - 1))
        
    data = args[0]
    children = args[1:]
    
    ret = BinaryTree(data)    
    
    if len(children) > 0:
        ret._left = children[0]
    if len(children) == 2:
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


class BinaryTreeTest(unittest.TestCase):

    
    def assertTreeEqual(self, actual, expected):
        """ Asserts the trees actual and expected are equal """
        
        def get_children(bt):
            ret = []
            if bt._left:
                ret.append(bt._left)
            if bt._right:
                ret.append(bt._right)
            return ret

        def rec_assert(c1, c2, row):                    
            
            if c2 == None:
                raise Exception("Found a None node in EXPECTED tree!\n\n" 
                                + str_btrees(actual,expected,row))
            
            if c1 == None:
                raise Exception("Found a None node in ACTUAL tree! \n\n"
                                + str_btrees(actual,expected,row))                     

            if not isinstance(c2, BinaryTree):
                raise Exception("EXPECTED value is an instance of  %s , which is not a BinaryTree !\n\n%s" % (type(c2).__name__ , str_btrees(actual,expected,row)))
                                
            if not isinstance(c1, BinaryTree):
                raise Exception("ACTUAL node is an instance of  %s  , which is not a  BinaryTree  !\n\n%s"
                                % (type(c1).__name__, str_btrees(actual, expected, row )))
                            
            if c1.data() != c2.data():
                raise Exception("Actual data is different from expected!\n\n" 
                                + str_btrees(actual,expected,row))
            
            i = 0            
            
            cs1 = get_children(c1)
            cs2 = get_children(c2)
            if (len(cs1) != len(cs2)):
                raise Exception("Children sizes are different !\n\n"
                                + str_btrees(actual, expected, row + min(len(cs1), len(cs2))) )
            while (i < len(cs1) ):
                rec_assert(cs1[i], cs2[i], row + 1)   
                i += 1 
        
        rec_assert(actual, expected, 0)

        
        
        
class BinaryTreeTestTest(BinaryTreeTest):    
    """ Tests the test itself ... """
    
    def test_str_btrees(self):
        self.assertTrue('a' in str_btrees(bt('a'), bt('b')))
        self.assertTrue('b' in str_btrees(bt('a'), bt('b')))
        
        self.assertTrue('a' in str_btrees(bt('a', bt('b')), bt('b', bt('c'))))
        self.assertTrue('c' in str_btrees(bt('a', bt('b')), bt('b', bt('c'))))
    
    def test_assert_tree_equal(self):
        self.assertTreeEqual(bt('a'), bt('a'))
        self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('b')))
        
        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a'), bt('b'))            
        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('c')))
        
        # different structure
        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('b',bt('c'))))

        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a', bt('b',bt('c'))), bt('a', bt('b')))        
    
    def test_print(self):
        # self.assertTreeEqual(bt('a', bt('b', bt('v')), bt('b', bt('v'))), bt('a', bt('b', bt('v'), bt('b', bt('v'))), bt('b')))
        return None 
            
                            
class InsertLeftTest(BinaryTreeTest):

    def test_insert_left(self):        
        ta = BinaryTree('a')        
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

class InsertRightTest(BinaryTreeTest):

    def test_insert_right(self):        
        ta = BinaryTree('a')        
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



class ScheduleRecTest(BinaryTreeTest):

    def test_01_a(self):
        t = bt('a')
        self.assertEqual(t.schedule_rec(), ['a'])

    def test_02_ab(self):
        t = bt('b',
                    bt('a'))
        self.assertEqual(t.schedule_rec(), ['a','b'])

    def test_03_ba_left(self):
        t = bt('a',
                    bt('b'))
        self.assertEqual(t.schedule_rec(), ['b','a'])

    def test_04_ba_right(self):
        t = bt('a',
                    None,
                    bt('b'))
        self.assertEqual(t.schedule_rec(), ['b','a'])


    def test_05_bca(self):
        t = bt('a',
                    bt('b'),
                    bt('c'))
        self.assertEqual(t.schedule_rec(), ['b','c','a'])

    def test_06_cbda(self):
        t = bt('a',
                    bt('b', 
                            bt('c')),
                    bt('d'))

        self.assertEqual(t.schedule_rec(), ['c','b','d','a'])

    def test_07_complex(self):
        t = bt('i',
                    bt('d', 
                            bt('b',
                                    bt('a')),
                            bt('c')),
                    bt('h',
                            bt('f',
                                    None,
                                    bt('e')),
                            bt('g')))


        self.assertEqual(t.schedule_rec(), ['a','b','c','d','e','f','g','h','i'])
