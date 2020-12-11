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
        if children[0] != None and not isinstance(children[0], BinaryTree):
            raise Exception('Wrong type %s for left child!' % type(children[0]))
        ret._left = children[0]
    if len(children) == 2:
        if children[1] != None and not isinstance(children[1], BinaryTree):
            raise Exception('Wrong type %s for right child!' % type(children[1]))
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
                raise Exception("ACTUAL data is different from expected!\n\n" 
                                + str_btrees(actual,expected,row))
            
            i = 0            
            
            cs1 = get_children(c1)
            cs2 = get_children(c2)
            if (len(cs1) != len(cs2)):
                raise Exception("Number of children is different !\n\n"
                                + str_btrees(actual, expected, row + min(len(cs1), len(cs2))) )
            while (i < len(cs1) ):
                rec_assert(cs1[i], cs2[i], row + 1)   
                i += 1 
                
        try:
            rec_assert(actual, expected, 0)
        except Exception as e:
            # not all exceptions have 'message' 
            raise AssertionError(getattr(e, 'message', e.args[0])) from None
        
        
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
    
    def test_bt(self):
        
        with self.assertRaises(Exception):
            bt(0,bt(1), bt(2), bt(3))
        
        with self.assertRaises(Exception):
            bt(2,666)
        
        with self.assertRaises(Exception):
            bt(2,None, 666)
            
        with self.assertRaises(Exception):
            bt(2,666, 666)
        
        with self.assertRaises(Exception):
            bt(1,bt(2), 666)

        with self.assertRaises(Exception):
            bt(1, 666, bt(2))

                            
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


class SumRecTest(BinaryTreeTest):

    """
        5
        ├
        └
    """
    def test_01_5_empty_empty(self):
        t = bt(5)
        self.assertEqual(t.sum_rec(), 5)

    """
        4
        ├7
        └
    """
    def test_02_4_7_empty(self):
        t = bt(4, bt(7))
        self.assertEqual(t.sum_rec(), 11)

    """
        6
        ├
        └3
    """
    def test_03_6_empty_3(self):
        t = bt(6, None, bt(3))
        self.assertEqual(t.sum_rec(), 9)

    """
        4
        ├8
        └3
    """
    def test_04_4_8_3(self):
        t = bt(4, bt(8), bt(3))
        self.assertEqual(t.sum_rec(), 15)

    """
        7
        ├2
        |├6
        |└
        └4
    """
    def test_05_7_26_4(self):
        t = bt(7, bt(2, bt(6)), bt(4))
        self.assertEqual(t.sum_rec(), 19)

    """
        9
        ├5            
        └3
         ├2
         └
    """
    def test_06_9_5_32(self):
        t = bt(9, bt(5), bt(3, bt(2)))
        self.assertEqual(t.sum_rec(), 19)

    """
        5
        ├2            
        |├3
        |└
        └ 
    """
    def test_07_523_left(self):
        t = bt(5, bt(2, bt(3)))
        self.assertEqual(t.sum_rec(), 10)

    """
        5
        ├
        └2            
         ├
         └3
    """
    def test_08_523_right(self):
        t = bt(5, None, bt(2, None, bt(3)))
        self.assertEqual(t.sum_rec(), 10)

    """
        3
        ├10
        │├1
        │└7
        │ ├5
        │ └
        └9
         ├6
         │├2
         ││├
         ││└4
         │└8
         └    """
    def test_09_complex(self):
        t = bt(3, 
                bt(10,
                        bt(1), 
                        bt(7, 
                            bt(5))),
                bt(9, 
                        bt(6, 
                            bt(2,
                                    None,
                                    bt(4)),
                            bt(8))))        

        self.assertEqual(t.sum_rec(), 55)
        
class HeightRecTest(BinaryTreeTest):

    """
        a
        ├
        └
    """    
    def test_01(self):        
        self.assertEqual(bt('a').height_rec(), 0)

    """
        a
        ├b
        └
    """   
    def test_02(self):        
        self.assertEqual(bt('a', bt('b')).height_rec(), 1)

    """
        a
        ├
        └c
    """        
    def test_03(self):        
        self.assertEqual(bt('a', None, bt('c')).height_rec(), 1)

    """
        a
        ├b
        └c
    """           
    def test_04(self):        
        self.assertEqual(bt('a', bt('b'), bt('c')).height_rec(), 1)

    """
        a
        ├b
        |├c
        |└
        └d
    """        
    def test_05(self):        
        self.assertEqual(bt('a', bt('b', bt('c')), bt('d')).height_rec(), 2)
     
    """
        a
        ├d            
        └b
         ├c
         └
    """        
    def test_06(self):        
        self.assertEqual(bt('a', bt('d'), bt('b', bt('c'))).height_rec(), 2)

    """
        a
        ├b
        |├c
        ||├d
        |||├e
        |||└
        ||└
        |└
        └f
         ├g
         └         
    """        
    def test_07(self):        
        self.assertEqual(bt('a', 
                                bt('b', 
                                       bt('c', 
                                              bt('d', 
                                                     bt('e')))),
                                bt('f', 
                                       bt('g'))).height_rec(), 4)


class DepthRecTest(BinaryTreeTest):
        
    """
        a
        ├
        └
    """           
    def test_01(self):   
        t = bt('a')     
        t.depth_rec(0)
        self.assertTreeEqual(t, bt(0))

    """
        a
        ├b
        └
    """        
    def test_02(self):      
        t = bt('a', bt('b'))
        t.depth_rec(0)      
        self.assertTreeEqual(t, bt(0, bt(1)))

    """
        a
        ├
        └c
    """           
    def test_03(self):  
        t = bt('a', None, bt('c'))
        t.depth_rec(0)
        self.assertTreeEqual(t, bt(0, None, bt(1)))

    """
        a
        ├b
        └c
    """           
    def test_04(self):   
        t = bt('a', bt('b'), bt('c'))
        t.depth_rec(0)
        self.assertTreeEqual(t, bt(0, bt(1), bt(1)))

    """
        a
        ├b
        |├d
        |└
        └c
    """           
    def test_05(self):    
        t = bt('a', bt('b', bt('c')), bt('d'))    
        t.depth_rec(0)
        self.assertTreeEqual(t, bt(0, bt(1, bt(2)), bt(1)))

    """
        a
        ├d
        └b
         ├c
         └
    """                   
    def test_06(self):   
        t = bt('a', bt('d'), bt('b', bt('c')))     
        t.depth_rec(0)
        self.assertTreeEqual(t, bt(0, bt(1), bt(1, bt(2))))

    """
        a
        ├b
        |├c
        ||├d
        |||├e
        |||└
        ||└
        |└
        └f
         ├g
         └         
    """                
    def test_07(self):  
        t = bt('a', 
                   bt('b', 
                          bt('c', 
                                 bt('d', 
                                        bt('e')))), 
                   bt('f', 
                          bt('g')))
        t.depth_rec(0)
        self.assertTreeEqual(t, bt(0, bt(1, bt(2, bt(3, bt(4)))), bt(1, bt(2))))

class ContainsRecTest(BinaryTreeTest):

    """
        a
        ├
        └
    """
    def test_01_a_empty_empty(self):
        t = bt('a')
        self.assertTrue(t.contains_rec('a'))
        self.assertFalse(t.contains_rec('b'))

    """
        a
        ├b
        └
    """
    def test_02_a_b_empty(self):
        t = bt('a', bt('b'))
        self.assertTrue(t.contains_rec('a'))
        self.assertTrue(t.contains_rec('b'))
        self.assertFalse(t.contains_rec('c'))

    """
        a
        ├
        └c
    """
    def test_03_a_empty_b(self):
        t = bt('a', None, bt('c'))
        self.assertTrue(t.contains_rec('a'))
        self.assertFalse(t.contains_rec('b'))
        self.assertTrue(t.contains_rec('c'))


    """
        a
        ├b
        └c
    """
    def test_04_a_b_c(self):
        t = bt('a', bt('b'), bt('c'))
        self.assertTrue(t.contains_rec('a'))
        self.assertTrue(t.contains_rec('b'))
        self.assertTrue(t.contains_rec('c'))
        self.assertFalse(t.contains_rec('d'))

    """
        a
        ├b
        |├c
        |└
        └d
    """
    def test_05_a_bc_d(self):
        t = bt('a', bt('b', bt('c')), bt('d'))
        self.assertTrue(t.contains_rec('a'))
        self.assertTrue(t.contains_rec('b'))
        self.assertTrue(t.contains_rec('c'))
        self.assertTrue(t.contains_rec('d'))
        self.assertFalse(t.contains_rec('e'))

    """
        a
        ├b            
        └c
         ├d
         └
    """
    def test_06_a_b_cd(self):
        t = bt('a', bt('b'), bt('c', bt('d')))
        self.assertTrue(t.contains_rec('a'))
        self.assertTrue(t.contains_rec('b'))
        self.assertTrue(t.contains_rec('c'))
        self.assertTrue(t.contains_rec('d'))
        self.assertFalse(t.contains_rec('e'))

    """
        a
        ├b            
        |├c
        |└
        └ 
    """
    def test_07_abc_left(self):
        t = bt('a', bt('b', bt('c')))
        self.assertTrue(t.contains_rec('a'))
        self.assertTrue(t.contains_rec('b'))
        self.assertTrue(t.contains_rec('c'))
        self.assertFalse(t.contains_rec('d'))

    """
        a
        ├
        └b            
         ├
         └c
    """
    def test_08_abc_right(self):
        t = bt('a', None, bt('b', None, bt('c')))
        self.assertTrue(t.contains_rec('a'))
        self.assertTrue(t.contains_rec('a'))
        self.assertTrue(t.contains_rec('a'))
        self.assertFalse(t.contains_rec('d'))

    """
        a
        ├b
        │├c
        │└d
        │ ├
        │ └e
        └f
         ├g
         │├h
         │└
         └i
    """
    def test_09_complex(self):
        t = bt('a', 
                    bt('b',
                            bt('c'), 
                            bt('d', 
                                    None,
                                    bt('e'))),
                    bt('f', 
                            bt('g', 
                                    bt('h')), 
                            bt('i')))
        self.assertTrue(t.contains_rec('g'))
        self.assertTrue(t.contains_rec('d'))
        self.assertFalse(t.contains_rec('z'))

class JoinRecTest(BinaryTreeTest):

    """
        a
        ├
        └
    """
    def test_01_a_empty_empty(self):
        t = bt('a')
        self.assertEqual(t.join_rec(), 'a')

    """
        a
        ├b
        └
    """
    def test_02_a_b_empty(self):
        t = bt('a', bt('b'))
        self.assertEqual(t.join_rec(), 'ba')

    """
        a
        ├
        └c
    """
    def test_03_a_empty_b(self):
        t = bt('a', None, bt('b'))
        self.assertEqual(t.join_rec(),'ab')


    """
        a
        ├b
        └c
    """
    def test_04_a_b_c(self):
        t = bt('a', bt('b'), bt('c'))
        self.assertEqual(t.join_rec(),'bac')

    """
        a
        ├b
        |├c
        |└
        └d
    """
    def test_05_a_bc_d(self):
        t = bt('a', bt('b', bt('c')), bt('d'))
        self.assertEqual(t.join_rec(),'cbad')

    """
        a
        ├b            
        └c
         ├d
         └
    """
    def test_06_a_b_cd(self):
        t = bt('a', bt('b'), bt('c', bt('d')))
        self.assertEqual(t.join_rec(),'badc')

    """
        a
        ├b            
        |├c
        |└
        └ 
    """
    def test_07_abc_left(self):
        t = bt('a', bt('b', bt('c')))
        self.assertEqual(t.join_rec(),'cba')
    """
        a
        ├
        └b            
         ├
         └c
    """
    def test_08_abc_right(self):
        t = bt('a', None, bt('b', None, bt('c')))
        self.assertEqual(t.join_rec(),'abc')

    """
        e
        ├b
        │├a
        │└c
        │ ├
        │ └d
        └h
        ├g
        │├f
        │└
        └i
    """
    def test_09_complex(self):
        t = bt('e', 
                    bt('b',
                            bt('a'), 
                            bt('c', 
                                    None,
                                    bt('d'))),
                    bt('h', 
                            bt('g', 
                                    bt('f')), 
                            bt('i')))
        self.assertEqual(t.join_rec(),'abcdefghi')

class BinSearchTest(BinaryTreeTest):
    def test_complex(self):
        t = bt(7, 
             bt(3, 
                    bt(2), 
                    bt(6)),
             bt(12, 
                    bt(8, 
                           None,
                           bt(11,
                                 bt(9))),
                    bt(14, 
                           bt(13))))


        self.assertTrue(t.bin_search_rec(8))
        self.assertTrue(t.bin_search_rec(13))
        self.assertTrue(t.bin_search_rec(7))
        self.assertFalse(t.bin_search_rec(1))
        self.assertFalse(t.bin_search_rec(5))
        self.assertFalse(t.bin_search_rec(10))


    
class UnivaluedRecTest(BinaryTreeTest):

    def test_complex_1(self):
        t = bt(3, 
                bt(3, 
                    bt(7), 
                    bt(3)),
                bt(3, 
                    bt(2, 
                           None,
                           bt(3,
                                 bt(3))),
                    bt(4, 
                           bt(3))))

        self.assertFalse(t.univalued_rec())

    def test_complex_2(self):
        t = bt(3, 
             bt(3, 
                    bt(3), 
                    bt(3)),
             bt(3, 
                    bt(3, 
                           None,
                           bt(3,
                                 bt(3))),
                    bt(3, 
                           bt(3))))

        self.assertTrue(t.univalued_rec())


class SameRecTest(BinaryTreeTest):

    def test_complex_1(self):
        t1 = bt(3, 
                bt(3, 
                    bt(7), 
                    bt(3)),
                bt(3, 
                    bt(2, 
                           None,
                           bt(3,
                                 bt(3))),
                    bt(4, 
                           bt(3))))
        t2 = bt(4, 
                bt(3, 
                    bt(8), 
                    bt(3)),
                bt(3,                     
                    bt(4, 
                           bt(3))))

        self.assertFalse(t1.same_rec(t2))

    def test_complex_2(self):
        t1 = bt(3, 
                bt(3, 
                    bt(7), 
                    bt(3)),
                bt(3, 
                    bt(2, 
                           None,
                           bt(3,
                                 bt(3))),
                    bt(4, 
                           bt(3))))
        t2 = bt(3, 
                bt(3, 
                    bt(7), 
                    bt(3)),
                bt(3, 
                    bt(2, 
                           None,
                           bt(3,
                                 bt(3))),
                    bt(4, 
                           bt(3))))

        self.assertTrue(t1.same_rec(t2))


class FunRecTest(BinaryTreeTest):

    """
        f
        ├
        └
    """
    def test_01_x(self):
        t = bt('x')
        self.assertEqual(t.fun_rec(), 'x')

    """
        f
        ├x
        └
    """
    def test_02_fx(self):
        t = bt('f', bt('x'))
        self.assertEqual(t.fun_rec(), 'f(x)')


    """
        g
        ├y
        └z
    """
    def test_03_gyz(self):
        t = bt('g', bt('y'), bt('z'))
        self.assertEqual(t.fun_rec(),'g(y,z)')

    """
        g
        ├f
        |├x
        |└
        └y
    """
    def test_04_a_gfxy(self):
        t = bt('g', bt('f', bt('x')), bt('y'))
        self.assertEqual(t.fun_rec(),'g(f(x),y)')

    """
        g
        ├y           
        └f
         ├x
         └
    """
    def test_05_gyfx(self):
        t = bt('g', bt('y'), bt('f', bt('x')))
        self.assertEqual(t.fun_rec(),'g(y,f(x))')

    """
        h
        ├g            
        |├x
        |└
        └ 
    """
    def test_06_hgx(self):
        t = bt('h', bt('g', bt('x')))
        self.assertEqual(t.fun_rec(),'h(g(x))')

    """
        f
        ├g
        │├x
        │└y
        └f
         ├h
         │├z
         │└
         └w
    """
    def test_07_complex(self):
        t = bt('f', 
                    bt('g',
                            bt('x'), 
                            bt('y')),
                    bt('f', 
                            bt('h', 
                                    bt('z')), 
                            bt('w')))
        self.assertEqual(t.fun_rec(),'f(g(x,y),f(h(z),w))')

class SumLeavesRecTest(BinaryTreeTest):

    """
        5
        ├
        └
    """
    def test_01_5_empty_empty(self):
        t = bt(5)
        self.assertEqual(t.sum_leaves_rec(), 5)

    """
        4
        ├7
        └
    """
    def test_02_4_7_empty(self):
        t = bt(4, 
                    bt(7))
        self.assertEqual(t.sum_leaves_rec(), 7)

    """
        6
        ├
        └3
    """
    def test_03_6_empty_3(self):
        t = bt(6, 
                    None, 
                    bt(3))
        self.assertEqual(t.sum_leaves_rec(), 3)

    """
        4
        ├8
        └3
    """
    def test_04_4_8_3(self):
        t = bt(4, 
                    bt(8), 
                    bt(3))
        self.assertEqual(t.sum_leaves_rec(), 8+3)

    """
        7
        ├2
        |├6
        |└
        └4
    """
    def test_05_7_26_4(self):
        t = bt(7, 
                    bt(2, 
                            bt(6)), 
                    bt(4))
        self.assertEqual(t.sum_leaves_rec(), 6+4)

    """
        9
        ├5            
        └3
         ├2
         └
    """
    def test_06_9_5_32(self):
        t = bt(9, 
                    bt(5), 
                    bt(3, 
                            bt(2)))
        self.assertEqual(t.sum_leaves_rec(), 5+2)

    """
        5
        ├2            
        |├3
        |└
        └ 
    """
    def test_07_523_left(self):
        t = bt(5, 
                    bt(2, 
                            bt(3)))
        self.assertEqual(t.sum_leaves_rec(), 3)

    """
        5
        ├
        └2            
         ├
         └3
    """
    def test_08_523_right(self):
        t = bt(5, 
                    None, 
                    bt(2, 
                            None, 
                            bt(3)))
        self.assertEqual(t.sum_leaves_rec(), 3)

    """
        3
        ├10
        │├1
        │└7
        │ ├5
        │ └
        └9
         ├6
         │├2
         ││├
         ││└4
         │└8
         └
    """
    def test_09_complex(self):
        t = bt(3, 
                bt(10,
                        bt(1), 
                        bt(7, 
                            bt(5))),
                bt(9, 
                        bt(6, 
                            bt(2,
                                    None,
                                    bt(4)),
                            bt(8))))
        self.assertEqual(t.sum_leaves_rec(), 18)  # 1+5+4+8)




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

class PathsSlowRecTest(BinaryTreeTest):

    def test_01_empty(self):
        t = bt(5)
        self.assertEqual(t.paths_slow_rec(), [[5]])

    def test_02_4_7_N(self):
        t = bt(4, 
                    bt(7))
        self.assertEqual(t.paths_slow_rec(), [[4,7]])
    
    def test_03_3_8(self):
        t = bt(3,   
                   None,
                   bt(8))
        self.assertEqual(t.paths_slow_rec(), [[3,8]])

    def test_04_2_5__2_9(self):
        t = bt(2,   
                   bt(5),
                   bt(9))
        self.assertEqual(t.paths_slow_rec(), [[2,5],[2,9]])

    def test_05_2_5_3__2_9(self):
        t = bt(2,   
                   bt(5, 
                         bt(3)),
                   bt(9))
        self.assertEqual(t.paths_slow_rec(), [[2,5,3],[2,9]])
        
    def test_05_2_5__2_10_6(self):
        t = bt(2,   
                   bt(5),
                   bt(10,
                          bt(6)))
        self.assertEqual(t.paths_slow_rec(), [[2,5],[2,10,6]])
        
    def test_complex(self):        
        t = bt('a',
                bt('b', 
                        bt('d',
                                bt('h')),
                        bt('e')),
                bt('c',
                        bt('f',
                                None,
                                bt('i', 
                                         bt('l'),
                                         bt('m'))),
                        bt('g')))
        self.assertEqual(t.paths_slow_rec(), [['a', 'b', 'd', 'h'],
                                              ['a', 'b', 'e'],
                                              ['a', 'c', 'f', 'i', 'l'],
                                              ['a', 'c', 'f', 'i', 'm'],
                                              ['a', 'c', 'g']])
        
class PathsFastRecTest(BinaryTreeTest):

    def test_01_empty(self):
        t = bt(5)
        self.assertEqual(t.paths_fast_rec(), [[5]])

    def test_02_4_7_N(self):
        t = bt(4, 
                    bt(7))
        self.assertEqual(t.paths_fast_rec(), [[4,7]])
    
    def test_03_3_8(self):
        t = bt(3,   
                   None,
                   bt(8))
        self.assertEqual(t.paths_fast_rec(), [[3,8]])

    def test_04_2_5__2_9(self):
        t = bt(2,   
                   bt(5),
                   bt(9))
        self.assertEqual(t.paths_fast_rec(), [[2,5],[2,9]])

    def test_05_2_5_3__2_9(self):
        t = bt(2,   
                   bt(5, 
                         bt(3)),
                   bt(9))
        self.assertEqual(t.paths_fast_rec(), [[2,5,3],[2,9]])
        
    def test_05_2_5__2_10_6(self):
        t = bt(2,   
                   bt(5),
                   bt(10,
                          bt(6)))
        self.assertEqual(t.paths_fast_rec(), [[2,5],[2,10,6]])
        
    def test_complex(self):        
        t = bt('a',
                bt('b', 
                        bt('d',
                                bt('h')),
                        bt('e')),
                bt('c',
                        bt('f',
                                None,
                                bt('i', 
                                         bt('l'),
                                         bt('m'))),
                        bt('g')))
        self.assertEqual(t.paths_fast_rec(), [['a', 'b', 'd', 'h'],
                                              ['a', 'b', 'e'],
                                              ['a', 'c', 'f', 'i', 'l'],
                                              ['a', 'c', 'f', 'i', 'm'],
                                              ['a', 'c', 'g']])        
        
class SumStackTest(BinaryTreeTest):

    """
        5
        ├
        └
    """
    def test_01_5_empty_empty(self):
        t = bt(5)
        self.assertEqual(t.sum_stack(), 5)

    """
        4
        ├7
        └
    """
    def test_02_4_7_empty(self):
        t = bt(4, bt(7))
        self.assertEqual(t.sum_stack(), 11)

    """
        6
        ├
        └3
    """
    def test_03_6_empty_3(self):
        t = bt(6, None, bt(3))
        self.assertEqual(t.sum_stack(), 9)

    """
        4
        ├8
        └3
    """
    def test_04_4_8_3(self):
        t = bt(4, bt(8), bt(3))
        self.assertEqual(t.sum_stack(), 15)

    """
        7
        ├2
        |├6
        |└
        └4
    """
    def test_05_7_26_4(self):
        t = bt(7, bt(2, bt(6)), bt(4))
        self.assertEqual(t.sum_stack(), 19)

    """
        9
        ├5            
        └3
         ├2
         └
    """
    def test_06_9_5_32(self):
        t = bt(9, bt(5), bt(3, bt(2)))
        self.assertEqual(t.sum_stack(), 19)

    """
        5
        ├2            
        |├3
        |└
        └ 
    """
    def test_07_523_left(self):
        t = bt(5, bt(2, bt(3)))
        self.assertEqual(t.sum_stack(), 10)

    """
        5
        ├
        └2            
         ├
         └3
    """
    def test_08_523_right(self):
        t = bt(5, None, bt(2, None, bt(3)))
        self.assertEqual(t.sum_stack(), 10)

    """
        3
        ├10
        │├1
        │└7
        │ ├5
        │ └
        └9
         ├6
         │├2
         ││├
         ││└4
         │└8
         └
    """
    def test_09_complex(self):
        t = bt(3, 
                bt(10,
                        bt(1), 
                        bt(7, 
                            bt(5))),
                bt(9, 
                        bt(6, 
                            bt(2,
                                    None,
                                    bt(4)),
                            bt(8))))
        self.assertEqual(t.sum_stack(), 55)



class HeightStackTest(BinaryTreeTest):

    def test_01(self):        
        self.assertEqual(bt('a').height_stack(), 0)

    def test_02(self):        
        self.assertEqual(bt('a', bt('b')).height_stack(), 1)

    def test_03(self):        
        self.assertEqual(bt('a', None, bt('b')).height_stack(), 1)

    def test_04(self):        
        self.assertEqual(bt('a', bt('b'), bt('c')).height_stack(), 1)

    def test_05(self):        
        self.assertEqual(bt('a', bt('b', bt('c')), bt('d')).height_stack(), 2)

    def test_06(self):        
        self.assertEqual(bt('a', bt('d'), bt('b', bt('c'))).height_stack(), 2)

    def test_07(self):        
        self.assertEqual(bt('a', bt('b', bt('c', bt('d', bt('e')))), bt('f', bt('g'))).height_stack(), 4)
        

class BinInsertRecTest(BinaryTreeTest):
    def test_complex(self):
        
        t1 = bt(7)
        t1.bin_insert_rec(3)
        t1.bin_insert_rec(6)
        t1.bin_insert_rec(2)
        t1.bin_insert_rec(12)
        t1.bin_insert_rec(14)
        t1.bin_insert_rec(13)
        t1.bin_insert_rec(8)
        t1.bin_insert_rec(11)
        t1.bin_insert_rec(9)

        t2 = bt(7, 
                    bt(3, 
                            bt(2), 
                            bt(6)),
                    bt(12, 
                            bt(8, 
                                None,
                                bt(11,
                                        bt(9))),
                            bt(14, 
                                bt(13))))


        self.assertTreeEqual(t1, t2)        
        
        
class AddRowTest(BinaryTreeTest):


    def test_01_a_empty(self):
        t = bt('a')
        t.add_row([])
        self.assertTreeEqual(t,bt('a'))

    def test_02_a_x(self):
        t = bt('a')
        t.add_row(['x'])
        self.assertTreeEqual(t,bt('a',
                                       bt('x')))

    def test_03_a__x_y(self):
        t = bt('a')
        t.add_row(['x','y'])
        self.assertTreeEqual(t,bt('a',
                                       bt('x'),
                                       bt('y')))

    def test_04_a__x_y_z(self):
        t = bt('a')
        
        with self.assertRaises(ValueError):
            t.add_row(['x','y','z'])

        
    def test_05_a_b_c__x(self):
        t = bt('a',
                    bt('b'),
                    bt('c'),)
        t.add_row(['x'])
        self.assertTreeEqual(t,bt('a',
                                       bt('b',
                                            bt('x')),
                                       bt('c')))

    def test_06_a_b_c__x_y(self):
        t = bt('a',
                    bt('b'),
                    bt('c'),)
        t.add_row(['x','y'])
        self.assertTreeEqual(t,bt('a',
                                       bt('b',
                                            bt('x'),
                                            bt('y')),
                                       bt('c')))

    def test_07_a_b_c__x_y_z(self):
        t = bt('a',
                    bt('b'),
                    bt('c'),)
        t.add_row(['x','y','z'])
        self.assertTreeEqual(t,bt('a',
                                       bt('b',
                                            bt('x'),
                                            bt('y')),
                                       bt('c',
                                            bt('z'))))

    def test_08_a_b_c__x_y_z_w(self):
        t = bt('a',
                    bt('b'),
                    bt('c'),)
        t.add_row(['x','y','z','w'])
        self.assertTreeEqual(t,bt('a',
                                       bt('b',
                                            bt('x'),
                                            bt('y')),
                                       bt('c',
                                            bt('z'),
                                            bt('w'))))

    def test_09_a_b_c__x_y_z_w_t(self):
        t = bt('a',
                    bt('b'),
                    bt('c'))
        with self.assertRaises(ValueError):
            t.add_row(['x','y','z','w','t'])
        

    """
        a
        ├b
        │├c
        │└d
        └f
         ├g
         └i
    """
    def test_10_complex(self):
        t = bt('a', 
                    bt('b',
                            bt('c'), 
                            bt('d')),
                    bt('f', 
                            bt('g'),                                    
                            bt('i')))
        t.add_row(['x','y','z','w','t'])
        self.assertTreeEqual(t, bt('a', 
                                        bt('b',
                                                bt('c',
                                                        bt('x'),
                                                        bt('y'),), 
                                                bt('d', 
                                                        bt('z'),
                                                        bt('w'))),
                                        bt('f', 
                                                bt('g', 
                                                        bt('t')), 
                                                bt('i'))))
                                                
                                                

                            
class PruneRecTest(BinaryTreeTest):

    def test_a_pa(self):
        """ root is not pruned """
        ta = bt('a')
        with self.assertRaises(ValueError):
            ta.prune_rec('a')        

    def test_a_a_pa(self):
        ta = bt('a', bt('a'))
        with self.assertRaises(ValueError):
            ta.prune_rec('a')    


    def test_root_pb(self):
        ta = bt('a')
        ta.prune_rec('b')
        self.assertTreeEqual(ta, bt('a'))

    def test_a_a_pb(self):
        ta = bt('a', bt('a'))
        ta.prune_rec('b')        
        self.assertTreeEqual(ta, bt('a',bt('a')))

    def test_a_b_pa(self):
        ta = bt('a', bt('b'))
        with self.assertRaises(ValueError):
            ta.prune_rec('a')        

    def test_a_b_pb(self):
        ta = bt('a', bt('b'))
        ta.prune_rec('b')
        self.assertTreeEqual(ta, bt('a'))

    def test_a_b_b_pb(self):
        ta = bt('a', bt('b'),bt('b'))
        ta.prune_rec('b')
        self.assertTreeEqual(ta, bt('a'))

    def test_a_a_b_pb(self):
        ta = bt('a', bt('a'),bt('b'))
        ta.prune_rec('b')
        self.assertTreeEqual(ta, bt('a', bt('a')))

    def test_a_b_a_pb(self):
        ta = bt('a', bt('b'),bt('a'))
        ta.prune_rec('b')
        self.assertTreeEqual(ta, bt('a',None, bt('a')))

    def test_a_n_b_c_pc(self):
        ta = bt('a', 
                    None, 
                    bt('b', 
                            bt('c')))
        ta.prune_rec('c')
        self.assertTreeEqual(ta, bt('a', 
                                        None, 
                                        bt('b')))

    def test_complex(self):
        ta = bt('a',
                bt('b',
                        bt('z'),
                        bt('c',
                            bt('d'),
                            bt('z',
                                    None,
                                    bt('e')))),
                bt('z', 
                        bt('f'),
                        bt('z', 
                            None,
                            bt('g'))))
        
        tb = bt('a',
                    bt('b',
                           None,
                           bt('c',
                                  bt('d'))))
                    
        ta.prune_rec('z')
        self.assertTreeEqual(ta, tb)

