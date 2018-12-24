from eqlist_solution import *
import unittest

def to_py(eq_list):
    """ Returns eq_list as a regular Python list - very handy for testing.
    """
    python_list = []
    current = eq_list._head        
    
    while (current != None):
        python_list.append(current.get_data())
        current = current.get_next()                       
    return python_list        


class EqListTest(unittest.TestCase):

    def myAssert(self, eq_list, python_list):
        """ Checks provided eq_list can be represented as the given python_list.
        """
        self.assertEqual(to_py(eq_list), python_list)
        # check this new invariant about the size        
        self.assertEqual(eq_list.size(), len(python_list)) 
    

class AddTest(EqListTest):
    
    def test_01_init(self):
        ul = EqList()
    
    def test_02_str(self):
        ul = EqList()
        self.assertTrue('EqList' in str(ul))
        ul.add('z')
        self.assertTrue('z' in str(ul))
        ul.add('w')
        self.assertTrue('z' in str(ul))
        self.assertTrue('w' in str(ul))
                
    def test_03_is_empty(self):
        ul = EqList()
        self.assertTrue(ul.is_empty())        
        ul.add('a')
        self.assertFalse(ul.is_empty())        
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = EqList()
        self.assertEqual(to_py(ul), [])
        ul.add('b')
        self.assertEqual(to_py(ul), ['b'])
        ul.add('a')
        self.assertEqual(to_py(ul), ['a', 'b'])
               
class EqTest(EqListTest):

    def test_01_empty(self):
        list1 = EqList()
        list2 = EqList()
        self.assertEqual(list1, list2)

    def test_02_one_same(self):
        list1 = EqList()
        list1.add('a')
        list2 = EqList()
        list2.add('a')
        self.assertEqual(list1, list2)

    def test_03_one_diff(self):
        list1 = EqList()
        list1.add('a')
        list2 = EqList()
        list2.add('b')
        self.assertNotEqual(list1, list2)

    def test_04_one_two(self):
        list1 = EqList()
        list1.add('a')
        list2 = EqList()
        list2.add('b')
        list2.add('a')
        self.assertNotEqual(list1, list2)

    def test_05_two_one(self):
        list1 = EqList()
        list1.add('b')
        list1.add('a')
        list2 = EqList()
        list2.add('a')
        self.assertNotEqual(list1, list2)

        
    def test_06_two_eq(self):
        list1 = EqList()
        list1.add('b')
        list1.add('a')
        list2 = EqList()
        list2.add('b')
        list2.add('a')
        self.assertEqual(list1, list2)
        
    def test_07_two_not_eq(self):
        list1 = EqList()
        list1.add('b')
        list1.add('a')
        list2 = EqList()
        list2.add('c')
        list2.add('a')
        self.assertNotEqual(list1, list2)
        
    def test_08_three_rep_eq(self):
        list1 = EqList()
        list1.add('a')
        list1.add('b')
        list1.add('a')
        list2 = EqList()
        list2.add('a')
        list2.add('b')
        list2.add('a')
        self.assertEqual(list1, list2)

    def test_09_three_rep_diff(self):
        list1 = EqList()
        list1.add('a')
        list1.add('c')
        list1.add('a')
        list2 = EqList()
        list2.add('a')
        list2.add('b')
        list2.add('a')
        self.assertNotEqual(list1, list2)

class RemsubTest(EqListTest):
    
    def test_01_empty(self):
        list1 = EqList()
        list2 = EqList()
        list1.remsub(list2)
        self.assertEqual(to_py(list1), [])

    def test_02_one_same(self):
        list1 = EqList()
        list1.add('a')
        list2 = EqList()
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(to_py(list1), [])

    def test_03_one_diff(self):
        list1 = EqList()
        list1.add('a')
        list2 = EqList()
        list2.add('b')
        list1.remsub(list2)
        self.assertEqual(to_py(list1), ['a'])
        
    def test_04_two_one_match(self):
        list1 = EqList()
        list1.add('a')
        list1.add('a')
        list2 = EqList()
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(to_py(list1), ['a'])
        
    def test_05_two_two_match(self):
        list1 = EqList()
        list1.add('a')
        list1.add('a')
        list2 = EqList()
        list2.add('a')
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(to_py(list1), [])
        
    def test_06_three_borders(self):
        list1 = EqList()
        list1.add('c')
        list1.add('b')
        list1.add('a')
        list2 = EqList()
        list2.add('c')
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(to_py(list1), ['b'])

    def test_07_three_middle(self):
        list1 = EqList()
        list1.add('c')
        list1.add('b')
        list1.add('a')        
        list2 = EqList()
        list2.add('b')
        list1.remsub(list2)
        self.assertEqual(to_py(list1), ['a', 'c'])
        
    def test_08_three_end(self):
        list1 = EqList()
        list1.add('b')
        list1.add('b')
        list1.add('a')        
        list2 = EqList()
        list2.add('b')
        list2.add('b')
        list1.remsub(list2)
        self.assertEqual(to_py(list1), ['a'])
        
        