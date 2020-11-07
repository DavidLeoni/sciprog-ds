import unittest
from cloning_sol import *

def to_py(linked_list):
    """ Returns linked_list as a regular Python list - very handy for testing.
    """
    python_list = []
    current = linked_list._head        
    
    while (current != None):
        python_list.append(current.get_data())
        current = current.get_next()                       
    return python_list        

def to_ll(python_list):
    """ Creates a LinkedList from a regular Python list - very handy for testing.
    """
    ret = LinkedList()
    
    for el in reversed(python_list):
        ret.add(el)
    return ret


class LinkedListTest(unittest.TestCase):

    def myAssert(self, linked_list, python_list):
        """ Checks provided linked_list can be represented as the given python_list.
        """
        self.assertEqual(to_py(linked_list), python_list)


class AddTest(LinkedListTest):
    
    def test_01_init(self):
        ul = LinkedList()
    
    def test_02_str(self):
        ul = LinkedList()
        self.assertTrue('LinkedList' in str(ul))
        ul.add('z')
        self.assertTrue('z' in str(ul))
        ul.add('w')
        self.assertTrue('z' in str(ul))
        self.assertTrue('w' in str(ul))
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = LinkedList()
        self.assertEqual(to_py(ul), [])
        ul.add('b')
        self.assertEqual(to_py(ul), ['b'])
        ul.add('a')
        self.assertEqual(to_py(ul), ['a', 'b'])

        
class RemoveTest(LinkedListTest):        
    
    def test_01_remove_empty_list(self):
        ul = LinkedList()
        with self.assertRaises(LookupError):
            ul.remove('a')

            
    def test_02_remove_one_element(self):
        ul = LinkedList()
        ul.add('a')
        with self.assertRaises(LookupError):
            ul.remove('b')
        ul.remove('a')
        self.assertEqual(to_py(ul), [])
        
    def test_03_remove_two_element(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        with self.assertRaises(LookupError):
            ul.remove('c')
        ul.remove('b')
        self.assertEqual(to_py(ul), ['a'])        
        ul.remove('a')
        self.assertEqual(to_py(ul), [])        

        
    def test_04_remove_first_occurrence(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('b')
        with self.assertRaises(LookupError):
            ul.remove('c')
        ul.remove('b')
        self.assertEqual(to_py(ul), ['b'])        
        ul.remove('b')
        self.assertEqual(to_py(ul), [])
  

class RevTest(unittest.TestCase):
    def test_rev_empty(self):
        ul = LinkedList()
        
        self.assertEqual([], to_py(ul))
        self.assertEqual([], to_py(ul.rev()))        

    def test_rev_one(self):
        ul = LinkedList()
        ul.add('a')
        self.assertEqual(['a'], to_py(ul))
        self.assertEqual(['a'], to_py(ul.rev()))
        

    def test_rev_three(self):
        ul = LinkedList()
        ul.add('c')
        ul.add('b')
        ul.add('a')
        self.assertEqual(['a','b','c'], to_py(ul))
        self.assertEqual(['c', 'b', 'a'], to_py(ul.rev()))        

class CloneTest(unittest.TestCase):

    def test_clone_empty(self):
        orig = LinkedList()
                
        cp = orig.clone()
        self.assertEqual([], to_py(cp))        
        
        orig.add('a')
        self.assertEqual(['a'], to_py(orig))
        self.assertEqual([], to_py(cp))        
        

    def test_clone_one(self):
        orig = LinkedList()
        orig.add('b')
        
        cp = orig.clone()
        self.assertEqual(['b'], to_py(cp))        
        
        orig.add('a')        
        self.assertEqual(['a', 'b'], to_py(orig))
        self.assertEqual(['b'], to_py(cp))        
        orig.remove('b')        
        self.assertEqual(['a'], to_py(orig))
        self.assertEqual(['b'], to_py(cp))        

        
    def test_clone_two(self):
        orig = LinkedList()
        orig.add('c')
        orig.add('b')        
        
        cp = orig.clone()
        self.assertEqual(['b', 'c'], to_py(cp))        
        
        orig.add('a')
        self.assertEqual(['a', 'b', 'c'], to_py(orig))
        self.assertEqual(['b','c'], to_py(cp))        

        orig.remove('c')
        self.assertEqual(['a', 'b'], to_py(orig))
        self.assertEqual(['b','c'], to_py(cp))     
        
        

class SliceTest(LinkedListTest):
    
    def test_01_neg_start(self):
        la = to_ll(['a','b','c'])

        with self.assertRaises(ValueError):
            la.slice(-3,1)

    def test_02_neg_end(self):
        la = to_ll(['a','b','c'])

        with self.assertRaises(ValueError):
            la.slice(1,-3)

    def test_03_start_greater_than_end(self):
        la = to_ll(['a','b','c','d','e','f','g'])
        lb = la.slice(3,2)
        self.assertEqual(to_py(la), ['a','b','c','d','e','f','g'])
        self.assertEqual(to_py(lb), [])

    def test_04_start_equal_end(self):
        la = to_ll(['a','b','c','d','e','f','g'])
        lb = la.slice(2,2)
        self.assertEqual(to_py(la), ['a','b','c','d','e','f','g'])
        self.assertEqual(to_py(lb), [])

    def test_05_empty_0_3(self):
        la = LinkedList()
        lb = la.slice(0,3)
        self.assertEqual(to_py(la), [])
        self.assertEqual(to_py(lb), [])

    def test_06_empty_2_5(self):
        la = LinkedList()
        lb = la.slice(2,5)
        self.assertEqual(to_py(la), [])
        self.assertEqual(to_py(lb), [])

    def test_07_a_0_1(self):
        la = to_ll(['a'])
        lb = la.slice(0,1)
        self.assertEqual(to_py(la), ['a'])
        self.assertEqual(to_py(lb), ['a'])


    def test_08_abc_3_5(self):
        #            0   1   2     3   4   5
        la = to_ll(['a','b','c'])
        lb = la.slice(3,5)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), [])

    def test_09_abc_0_1(self):
        #           0   1   2  
        la = to_ll(['a','b','c'])
        lb = la.slice(0,1)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), ['a'])

    def test_10_abc_0_2(self):
        #           0   1   2   3
        la = to_ll(['a','b','c'])
        lb = la.slice(0,2)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), ['a','b'])

    def test_11_abc_0_3(self):
        #           0   1   2   3
        la = to_ll(['a','b','c'])
        lb = la.slice(0,3)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), ['a','b','c'])

    def test_12_abc_0_4(self):
        #           0   1   2   3  4
        la = to_ll(['a','b','c'])
        lb = la.slice(0,4)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), ['a','b','c'])


    def test_13_abc_1_3(self):
        #           0   1   2   3
        la = to_ll(['a','b','c'])
        lb = la.slice(1,3)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), ['b','c'])

    def test_14_abc_2_3(self):
        #           0   1   2   3
        la = to_ll(['a','b','c'])
        lb = la.slice(2,3)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), ['c'])

    def test_15_abc_1_4(self):
        #           0   1   2   3   4
        la = to_ll(['a','b','c'])
        lb = la.slice(1,4)
        self.assertEqual(to_py(la), ['a','b','c'])
        self.assertEqual(to_py(lb), ['b','c'])

    def test_16_abcdefg_2_5(self):
        #           0   1   2   3   4   5   6
        la = to_ll(['a','b','c','d','e','f','g'])
        lb = la.slice(2,5)
        self.assertEqual(to_py(la), ['a','b','c','d','e','f','g'])
        self.assertEqual(to_py(lb), ['c','d','e'])

        