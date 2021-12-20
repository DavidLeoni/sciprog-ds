
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


class NorepTest(LinkedListTest):
    
    def test_01_empty(self):
        ul = LinkedList()
        ul.norep()
        self.assertEqual(to_py(ul), [])    
    
    def test_02_a(self):
        ul = LinkedList()
        ul.add('a')
        ul.norep()
        self.assertEqual(to_py(ul), ['a'])    
                
    def test_03_aa(self):
        ul = LinkedList()
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a'])    

    def test_04_aaa(self):
        ul = LinkedList()
        ul.add('a')
        ul.add('a')        
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a'])    

    def test_05_aaab(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b'])    


    def test_06_baa(self):
        ul = LinkedList()               
        ul.add('a')
        ul.add('a')        
        ul.add('b')        
        ul.norep()
        self.assertEqual(to_py(ul), ['b', 'a'])    


    def test_07_aabb(self):
        ul = LinkedList()                               
        ul.add('b')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b'])    


    def test_08_aabba(self):
        ul = LinkedList()                               
        ul.add('a')
        ul.add('b')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b', 'a'])    

    def test_09_aabcc(self):
        ul = LinkedList()                               
        ul.add('c')
        ul.add('c')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b', 'c'])    

    def test_10_aaaccaabddccce(self):
        ll = LinkedList()                                               
        ll.add('e')
        ll.add('c')
        ll.add('c')
        ll.add('c')
        ll.add('d')
        ll.add('d')
        ll.add('b')
        ll.add('a')
        ll.add('a')
        ll.add('c')
        ll.add('c')
        ll.add('a')
        ll.add('a')        
        ll.add('a')
        ll.norep()
        self.assertEqual(to_py(ll), ['a', 'c', 'a', 'b', 'd', 'c', 'e'])
