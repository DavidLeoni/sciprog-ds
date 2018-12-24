import unittest
from more_solution import *

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
        with self.assertRaises(Exception):
            ul.remove('a')

            
    def test_02_remove_one_element(self):
        ul = LinkedList()
        ul.add('a')
        with self.assertRaises(Exception):
            ul.remove('b')
        ul.remove('a')
        self.assertEqual(to_py(ul), [])
        
    def test_03_remove_two_element(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        with self.assertRaises(Exception):
            ul.remove('c')
        ul.remove('b')
        self.assertEqual(to_py(ul), ['a'])        
        ul.remove('a')
        self.assertEqual(to_py(ul), [])        

        
    def test_04_remove_first_occurrence(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('b')
        with self.assertRaises(Exception):
            ul.remove('c')
        ul.remove('b')
        self.assertEqual(to_py(ul), ['b'])        
        ul.remove('b')
        self.assertEqual(to_py(ul), [])
  

class OccurrencesTest(LinkedListTest):

    def test_01_occurrences_zero(self):
        self.assertEqual(LinkedList().occurrences('a') , 0)
        self.assertEqual(LinkedList().occurrences(7) , 0 )
        
    def test_02_occurrences_one(self):
        
        ul = LinkedList()
        ul.add('a')
        self.assertEqual(ul.occurrences('a') , 1)
        self.assertEqual(ul.occurrences('b') , 0)
        self.assertEqual(ul.occurrences(7) , 0)

    def test_03_occurrences_three(self):
        
        ul = LinkedList()
        ul.add('a')
        ul.add('b')
        ul.add('a')        
        self.assertEqual(ul.occurrences('a'), 2 )
        self.assertEqual(ul.occurrences('b'), 1 )
        self.assertEqual(ul.occurrences('c'), 0 )

class ShrinkTest(LinkedListTest):
    def test_01_shrink_return_none(self):
        ul = LinkedList()         
        self.assertEqual(ul.shrink(), None)
        
    def test_02_shrink_empty(self):
        ul = LinkedList()            
        ul.shrink()
        self.assertEqual(to_py(ul), [])

    def test_03_shrink_one(self):
        ul = LinkedList()
        ul.add('a')
        ul.shrink()
        self.assertEqual(to_py(ul), ['a'])

    def test_04_shrink_two(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        ul.shrink()
        self.assertEqual(to_py(ul), ['a'])

    def test_05_shrink_three(self):
        ul = LinkedList()
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.shrink()
        self.assertEqual(to_py(ul), ['a', 'c'])

        
    def test_06_shrink_four(self):
        ul = LinkedList()
        ul.add('d')
        ul.add('c')
        ul.add('b')        
        ul.add('a')        
        
        ul.shrink()
        self.assertEqual(to_py(ul), ['a','c'])

class DupFirstTest(LinkedListTest):

    def test_01_return_none(self):
        ul = LinkedList()        
        self.assertEqual(ul.dup_first(), None)

    def test_02_empty(self):
        ul = LinkedList()        
        ul.dup_first()
        self.assertEqual(to_py(ul), [])

    def test_03_one(self):
        ul = LinkedList()        
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a'])

    def test_04_two(self):
        ul = LinkedList()        
        ul.add('b')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a', 'b'])

    def test_05_two_dups(self):
        ul = LinkedList()        
        ul.add('a')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a', 'a'])

    def test_06_three(self):
        ul = LinkedList()        
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a', 'b', 'c'])


class DupAllTest(LinkedListTest):

    def test_01_return_none(self):
        ul = LinkedList()        
        self.assertEqual(ul.dup_all(), None)

    def test_02_empty(self):
        ul = LinkedList()        
        ul.dup_all()
        self.assertEqual(to_py(ul), [])

    def test_03_one(self):
        ul = LinkedList()        
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a'])

    def test_04_two(self):
        ul = LinkedList()        
        ul.add('b')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a', 'b', 'b'])

    def test_05_two_dups(self):
        ul = LinkedList()        
        ul.add('a')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a', 'a', 'a'])

    def test_06_three(self):
        ul = LinkedList()        
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a', 'b', 'b', 'c', 'c'])


        
class MirrorTest(LinkedListTest):
    
    def test_01_empty(self):
        self.assertEqual(to_py(mirror([])), [])
    
    def test_02_one(self):
        self.assertEqual(to_py(mirror(['a'])), ['a','a'])
        
    def test_03_two(self):
        self.assertEqual(to_py(mirror(['a', 'b'])), ['a','b','b','a'])

    def test_04_three(self):
        self.assertEqual(to_py(mirror(['a', 'b', 'c'])), ['a','b','c','c','b','a'])



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



#unittest.main()        