import unittest
from cloning_solution import *

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