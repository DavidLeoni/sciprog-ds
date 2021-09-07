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
    """ Creates a LinkedList from a regll.r Python list - very handy for testing.
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
        # check this new invariant about the size        
        self.assertEqual(linked_list.size(), len(python_list)) 
    

class AddTest(LinkedListTest):
    
    def test_01_init(self):
        ll = LinkedList()
    
    def test_02_str(self):
        ll = LinkedList()
        self.assertTrue('LinkedList' in str(ll))
        ll.add('z')
        self.assertTrue('z' in str(ll))
        ll.add('w')
        self.assertTrue('z' in str(ll))
        self.assertTrue('w' in str(ll))
                
    def test_03_is_empty(self):
        ll = LinkedList()
        self.assertTrue(ll.is_empty())        
        ll.add('a')
        self.assertFalse(ll.is_empty())        
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ll = LinkedList()
        self.assertEqual(to_py(ll), [])
        ll.add('b')
        self.assertEqual(to_py(ll), ['b'])
        ll.add('a')
        self.assertEqual(to_py(ll), ['a', 'b'])


class LinalgTest(LinkedListTest):
    
    def test_01_empty(self):
        ll = LinkedList()
        res = ll.linalg()          
        self.assertEqual(to_py(ll), [])
        self.assertEqual(res, None) # should return NOTHING!        
    
    def test_02_1a(self):
        ll = LinkedList()        
        ll.add('1a')
        n0 = ll._head
        res = ll.linalg()                
        self.assertEqual(to_py(ll), ['a'])
        self.assertEqual(res, None) # should return NOTHING!                
        self.assertEqual(id(ll._head), id(n0))  # check didn't replaced original nodes          
        
    
    def test_03_2b(self):
        ll = LinkedList()
        ll.add('2b')
        n0 = ll._head
        ll.linalg()        
        self.assertEqual(to_py(ll), ['b','b'])
        self.assertEqual(id(ll._head), id(n0))  # check didn't replaced original nodes        
        
    def test_04_3a(self):
        ll = LinkedList()
        ll.add('3a')
        ll.linalg()        
        self.assertEqual(to_py(ll), ['a','a','a'])    
    
    def test_05_2a_1b(self):
        ll = LinkedList()
        ll.add('1b')
        ll.add('2a')
        n0 = ll._head
        n1 = ll._head._next
        ll.linalg()        
        self.assertEqual(to_py(ll), ['a','a','b'])
        self.assertEqual(id(ll._head), id(n0))       # check didn't replaced original nodes
        self.assertEqual(id(ll._head._next._next), id(n1))  
        

    def test_06_1a_2b(self):
        ll = LinkedList()
        ll.add('2b')
        ll.add('1a')
        ll.linalg()        
        self.assertEqual(to_py(ll), ['a','b','b'])
        
    def test_07_1a_1b(self):
        ll = LinkedList()
        ll.add('1a')
        ll.add('1b')
        ll.linalg()        
        self.assertEqual(to_py(ll), ['b','a'])

    def test_08_1a_1b_1c(self):
        ll = LinkedList()                
        ll.add('1c')
        ll.add('1b')
        ll.add('1a')
        ll.linalg()        
        self.assertEqual(to_py(ll), ['a','b','c'])


    def test_09_1a_3b_2c(self):
        ll = LinkedList()                
        ll.add('2c')
        ll.add('3b')
        ll.add('1a')
        res = ll.linalg()        
        self.assertEqual(to_py(ll), ['a','b','b','b','c','c'])
        
    def test_10_3a_5b_2c(self):
        ll = LinkedList()
        ll.add('2c')
        ll.add('5b')
        ll.add('3a')
        res = ll.linalg()        
        self.assertEqual(to_py(ll), ['a','a','a','b','b','b','b','b','c','c'])