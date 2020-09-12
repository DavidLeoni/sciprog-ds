from linked_list_sol import *
import unittest

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
    """ Test cases for LinkedList v3
    
        Test cases are improved by adding a new method myAssert(self, linked_list, python_list)         
    """    
    
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
            
    def test_03_is_empty(self):
        ul = LinkedList()
        self.assertTrue(ul.is_empty())        
        ul.add('a')
        self.assertFalse(ul.is_empty())        
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = LinkedList()
        self.myAssert(ul, [])
        ul.add('b')
        self.myAssert(ul, ['b'])
        ul.add('a')
        self.myAssert(ul, ['a', 'b'])


class CoupleSortTest(LinkedListTest):

    def test_01_empty(self):
        ll = LinkedList()        
        ll.couple_sort()
        self.assertEqual(to_py(ll), [])


    def test_02_4(self):
        ll = to_ll([4])
        res = ll.couple_sort()
        self.assertEqual(to_py(ll), [4])
        self.assertEqual(res, None)  # must not return anything


    def test_03_35(self):
        ll = to_ll([3,5])
        ll.couple_sort()
        self.assertEqual(to_py(ll), [3,5])

    def test_04_62(self):
        ll = to_ll([6,2])
        ll.couple_sort()
        self.assertEqual(to_py(ll), [2,6])

    def test_05_621(self):
        ll = to_ll([6,2,1])
        ll.couple_sort()
        self.assertEqual(to_py(ll), [2,6,1])


    def test_06_6241(self):
        ll = to_ll([6,2,4,1])
        ll.couple_sort()
        self.assertEqual(to_py(ll), [2,6,1,4])

    def test_07_512763(self):
        ll = to_ll([5,1,2,7,6,3])
        ll.couple_sort()
        self.assertEqual(to_py(ll), [1,5,2,7,3,6])

    def test_08_complex(self):
        ll = to_ll([4,3,5,2,6,7,6,3,2,4,5,3,2])
        ll.couple_sort()
        self.assertEqual(to_py(ll), [3,4,2,5,6,7,3,6,2,4,3,5,2])
