import unittest
from lists_sol import *

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


class FlatvTest(unittest.TestCase):

    def test_01_empty(self):
        ul = LinkedList()
        ul.flatv()
        self.assertEqual(to_py(ul),[] )

    def test_02_5(self): 
        ul = LinkedList()
        ul.add(5)
        ul.flatv()
        self.assertEqual(to_py(ul),[5] )

    def test_03_57(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.flatv()
        self.assertEqual(to_py(ul),[5,7] )

    def test_04_757(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.add(7)
        ul.flatv()
        self.assertEqual(to_py(ul),[7,5,5,7] )

    def test_05_657(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.add(6)
        ul.flatv()
        self.assertEqual(to_py(ul),[6,5,5,7] )

    def test_06_9557(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.add(5)
        ul.add(9)
        ul.flatv()
        self.assertEqual(to_py(ul),[9,5,5,7] )

    def test_07_757636(self): 
        """ Changes only first v
        """
        ul = LinkedList()
        ul.add(6)
        ul.add(3)
        ul.add(6)
        ul.add(7)
        ul.add(5)
        ul.add(7)
        ul.flatv()
        self.assertEqual(to_py(ul),[7,5,5,7,6,3,6] )

    def test_08_388758639(self): 
        """ Changes only first v
        """
        ul = LinkedList()
        ul.add(9)
        ul.add(3)
        ul.add(6)
        ul.add(8)
        ul.add(5)
        ul.add(7)
        ul.add(8)
        ul.add(8)
        ul.add(3)        
        ul.flatv()
        self.assertEqual(to_py(ul),[3,8,8,7,5,5,8,6,3,9] )      

 
