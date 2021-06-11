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

class SepelTest(LinkedListTest):
    
    # NEW
    def test_00_empty(self):
        la = to_ll([])
        lb = la.sepel('z')
        self.assertEqual(to_py(la), [])
        self.assertEqual(to_py(lb), [])
    
    def test_01_a_sa(self):
        la = to_ll(['a'])
        lan0 = la._head
        lb = la.sepel('a')
        
        self.assertEqual(to_py(la), [])
        self.assertEqual(to_py(lb), ['a'])
        
        lan0._data = 'x'  # checks node reuse
        self.assertEqual(to_py(lb), ['x'])

    def test_02_a_sb(self):
        la = to_ll(['a'])
        lan0 = la._head
        lb = la.sepel('b')

        self.assertEqual(to_py(la), ['a'])
        self.assertEqual(to_py(lb), [])

        lan0._data = 'x'  # checks no new nodes
        self.assertEqual(to_py(la), ['x'])

    def test_03_ab_sa(self):
        la = to_ll(['a','b'])
        lan0 = la._head
        lan1 = la._head._next
        lb = la.sepel('a')

        self.assertEqual(to_py(la), ['b'])
        self.assertEqual(to_py(lb), ['a'])

        lan0._data = 'x'  # checks no new nodes
        lan1._data = 'y'  
        self.assertEqual(to_py(la), ['y'])
        self.assertEqual(to_py(lb), ['x'])


    def test_04_ab_sb(self):
        la = to_ll(['a','b'])
        lan0 = la._head
        lan1 = la._head._next
        lb = la.sepel('b')

        self.assertEqual(to_py(la), ['a'])
        self.assertEqual(to_py(lb), ['b'])

        lan0._data = 'x'  # checks no new nodes
        lan1._data = 'y'  
        self.assertEqual(to_py(la), ['x'])
        self.assertEqual(to_py(lb), ['y'])


    def test_05_aba_sa(self):
        la = to_ll(['a','b','a'])
        lan0 = la._head
        lan1 = la._head._next
        lan2 = la._head._next._next
        lb = la.sepel('a')

        self.assertEqual(to_py(la), ['b'])
        self.assertEqual(to_py(lb), ['a','a'])

        lan0._data = 'x'  # checks no new nodes
        lan1._data = 'y'  
        lan2._data = 'z'  
        self.assertEqual(to_py(la), ['y'])
        self.assertEqual(to_py(lb), ['x','z'])        

    def test_06_aba_sb(self):
        la = to_ll(['a','b','a'])
        lan0 = la._head
        lan1 = la._head._next
        lan2 = la._head._next._next
        lb = la.sepel('b')

        self.assertEqual(to_py(la), ['a','a'])
        self.assertEqual(to_py(lb), ['b'])

        lan0._data = 'x'  # checks no new nodes
        lan1._data = 'y'  
        lan2._data = 'z'  
        self.assertEqual(to_py(la), ['x','z'])        
        self.assertEqual(to_py(lb), ['y'])

    def test_07_complex(self):
        la = to_ll(['c','a','b','c','c','d','c','e','c'])        
        lan0 = la._head
        lan3 = la._head._next._next._next
        lan4 = la._head._next._next._next._next
        lb = la.sepel('c')

        self.assertEqual(to_py(la), ['a','b','d','e'])
        self.assertEqual(to_py(lb), ['c','c','c','c','c'])
        lan0._data = 'x'
        lan3._data = 'y'
        lan4._data = 'z'
        self.assertEqual(to_py(la), ['a','b','d','e'])
        self.assertEqual(to_py(lb), ['x','y','z','c','c'])        
