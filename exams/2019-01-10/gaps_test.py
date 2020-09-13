import unittest
from gaps_solution import *

def to_py(linked_list):
    """ Returns linked_list as a regular Python list - very handy for testing.
    """
    python_list = []
    current = linked_list._head        
    
    while (current != None):
        python_list.append(current.get_data())
        current = current.get_next()                       
    return python_list        


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


class GapsTest(LinkedListTest):

    def test_empty(self):
        ul = LinkedList()

        self.assertEqual(ul.gaps(), [])

    def test_one(self):
        ul = LinkedList()
        ul.add(5)
        self.assertEqual(ul.gaps(), [])

    def test_5_7_one_gap(self):
        """    data: 5 7
              index: 0 1
        """
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        self.assertEqual(ul.gaps(), [1])  

    def test_7_5_no_gap(self):
        """    data: 7 5
              index: 0 1
        """
        ul = LinkedList()
        ul.add(5)
        ul.add(7)
        self.assertEqual(ul.gaps(), [])  

    def test_5_5_same(self):
        """   data:  5 5
              index: 0 1
        """
        ul = LinkedList()
        ul.add(5)
        ul.add(5)
        self.assertEqual(ul.gaps(), [])  


    def test_5_7_8_two_gaps(self):
        """    data: 5 7 8
              index: 0 1 2
        """
        ul = LinkedList()
        ul.add(8)
        ul.add(7)
        ul.add(5)
        self.assertEqual(ul.gaps(), [1,2])  

    def test_9_7_8_one_gap(self):
        """   9 7 8
              0 1 2
        """
        ul = LinkedList()
        ul.add(8)
        ul.add(7)
        ul.add(9)
        self.assertEqual(ul.gaps(), [2])  


    def test_complex(self):
        """   
              data:  9 7 6 8 9 2 2 5 
              index: 0 1 2 3 4 5 6 7              
        """
        ul = LinkedList()
        
        ul.add(5)
        ul.add(2)
        ul.add(2)
        ul.add(9)
        ul.add(8)
        ul.add(6)
        ul.add(7)
        ul.add(9)
        self.assertEqual(ul.gaps(), [3,4,7])  
