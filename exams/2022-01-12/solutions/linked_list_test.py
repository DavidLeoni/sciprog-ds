import unittest
from linked_list_sol import *

def to_py(linked_list):
    """ Creates a regular Python list from a LinkedList - very handy for testing.
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



        
class FindCoupleTest(LinkedListTest):
    
    def test_01_empty(self):
        ul = LinkedList()
        with self.assertRaises(LookupError):
            ul.find_couple('a','b')
        
    def test_02_a(self):
        ul = LinkedList()
        ul.add('a')
        with self.assertRaises(LookupError):
            ul.find_couple('a','b')

    def test_03_ab(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 0)
        
        with self.assertRaises(LookupError):
            ul.find_couple('b','a')
    
    def test_04_abc(self):
        ul = LinkedList()
        ul.add('c')        
        ul.add('b')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 0)
        self.assertEqual(ul.find_couple('b','c'), 1)
        
        with self.assertRaises(LookupError):
            ul.find_couple('a','c')

    def test_05_aab(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('a')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 1)

    def test_06_abbb(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('b')        
        ul.add('b')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 0)
        self.assertEqual(ul.find_couple('b','b'), 1)
        
        with self.assertRaises(LookupError):
            ul.find_couple('a','a')


class SwapTest(LinkedListTest):
    
    def test_01_empty(self):
        ul = LinkedList()
        with self.assertRaises(IndexError):
            ul.swap(0,3) 
        with self.assertRaises(IndexError):
            ul.swap(2,0)            

    def test_02_one(self):
        ul = LinkedList()
        ul.add('a')
        ul.swap(0,0)
        self.assertEqual(to_py(ul), ['a'])

    def test_03_one_wrong_indeces(self):
        ul = LinkedList()
        ul.add('a')
        with self.assertRaises(IndexError):
            ul.swap(-1,0)            
        with self.assertRaises(IndexError):
            ul.swap(0,-1)            
        with self.assertRaises(IndexError):
            ul.swap(0,2)            

    def test_04_two(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        
        ul.swap(0,1)
        self.assertEqual(to_py(ul), ['b','a'])
        ul.swap(0,1)
        self.assertEqual(to_py(ul), ['a', 'b'])

    def test_05_three(self):
        ul = LinkedList()
        ul.add('c')        
        ul.add('b')
        ul.add('a')
        
        ul.swap(0,1)
        self.assertEqual(to_py(ul), ['b','a','c'])
        ul.swap(1,2)
        self.assertEqual(to_py(ul), ['b', 'c','a'])
