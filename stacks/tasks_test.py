import unittest
from tasks_sol import * 


class SortedStackTest(unittest.TestCase):
               
    def test_01_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push('a')
        self.assertEqual(s.size(), 1)
        s.pop()
        self.assertEqual(s.size(), 0)

    
    def test_02_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push('a')
        self.assertFalse(s.is_empty())

    def test_05_pop_empty(self):
        s = Stack() 
        with self.assertRaises(IndexError):
            s.pop()
            
    def test_06_pop_one(self):
        s = Stack() 
        with self.assertRaises(IndexError):
            s.pop()
        s.push('a')        
        self.assertEqual(s.pop(), 'a')
        self.assertEqual(s.size(), 0)
        
    def test_07_pop_two(self):
        s = Stack()     
        with self.assertRaises(IndexError):
            s.pop()
        s.push('a')
        s.push('b')        
        self.assertEqual(s.pop(), 'b')
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.pop(), 'a')
        self.assertEqual(s.size(), 0)
        with self.assertRaises(IndexError):
            s.pop()
                        
    def test_09_push(self):
        s = Stack()        
        self.assertEqual(s.size(), 0)
        s.push('a')
        self.assertEqual(s.size(), 1)
        s.push('b')
        self.assertEqual(s.size(), 2)
        s.push('c') 
        self.assertEqual(s.size(), 3)
    
    def test_10_str(self):
        s = Stack()
        s.push('x')
        s.push('y')        
        self.assertTrue( 'x' in str(s))
        self.assertTrue( 'y' in str(s))
        self.assertTrue( 'Stack' in str(s))
    

class DoTest(unittest.TestCase):

    def test_01_a(self):
        subtasks = {
            'a': []
        }
        self.assertEqual(do('a', subtasks), ['a'])

    def test_02_ab(self):
        subtasks = {
            'a': ['b'],
            'b': []
        }
        self.assertEqual(do('a', subtasks), ['a','b'])


    def test_03_abc(self):
        subtasks = {
            'a': ['b','c'],
            'b': [],
            'c': []
        }
        self.assertEqual(do('a', subtasks), ['a','b','c'])


    def test_04_abc(self):
        subtasks = {
            'a': ['b'],
            'b': ['c'],
            'c': []
        }
        self.assertEqual(do('a', subtasks), ['a','b','c'])

    def test_05_abcd(self):
        subtasks = {
            'a': ['b','d'],
            'b': ['c'],
            'c': [],
            'd': []
        }
        self.assertEqual(do('a', subtasks), ['a','b','c','d'])


    def test_06_abcdfeg(self):

        subtasks = subtasks = {
                                'a':['b','g'],
                                'b':['c','d','e'],
                                'c':['f'],
                                'd':['g'],
                                'e':[],
                                'f':[],
                                'g':[]
                            }
        self.assertEqual(do('a', subtasks), ['a', 'b', 'c', 'f', 'd', 'g', 'e', 'g'])
        
class DoLevelTest(unittest.TestCase):

    def test_01_a(self):
        subtasks = {
            'a': []
        }
        self.assertEqual(do_level('a', subtasks),
                         [('a',0)])

    def test_02_ab(self):
        subtasks = {
            'a': ['b'],
            'b': []
        }
        self.assertEqual(do_level('a', subtasks), 
                         [('a',0),('b',1)])


    def test_03_abc(self):
        subtasks = {
            'a': ['b','c'],
            'b': [],
            'c': []
        }
        self.assertEqual(do_level('a', subtasks),
                         [('a',0),('b',1),('c',1)])


    def test_04_abc(self):
        subtasks = {
            'a': ['b'],
            'b': ['c'],
            'c': []
        }
        self.assertEqual(do_level('a', subtasks), 
                         [('a',0),('b',1),('c',2)])

    def test_05_abcd(self):
        subtasks = {
            'a': ['b','d'],
            'b': ['c'],
            'c': [],
            'd': []
        }
        self.assertEqual(do_level('a', subtasks),
                         [('a', 0),('b',1),('c',2),('d',1)])

        
    def test_06_abcde(self):
        """ Remember a level always depend on the *parent* task level !
        
        level 0   1   2
              a
                  b
                      d
                  c
                      e
        """
        subtasks = {
            'a': ['b','c'],
            'b': ['d'],
            'c': ['e'],
            'd': [],
            'e': [] 
        }
        self.assertEqual(do_level('a', subtasks), 
                         [('a',0),('b',1),('d',2),('c',1), ('e',2)])


        
    def test_07_abcdfeg(self):

        subtasks = {
                        'a':['b','g'],
                        'b':['c','d','e'],
                        'c':['f'],
                        'd':['g'],
                        'e':[],
                        'f':[],
                        'g':[]
                   }
        
        self.assertEqual(do_level('a', subtasks), 
                         [('a', 0), ('b', 1), ('c', 2), ('f', 3), ('d', 2), ('g', 3), ('e', 2), ('g', 1)])
        
        


        

