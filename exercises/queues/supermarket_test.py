import unittest
from supermarket_sol import *


def to_list(supermarket):
    """ Return the supermarket as a list of lists.
    """
    ret = []
    for q in supermarket._queues:
        ret.append(list(q._list))        
    return ret

class InitTest(unittest.TestCase):

    def test_01_empty(self):
        
        with self.assertRaises(ValueError):
            s = Supermarket([])
        
    def test_02_one(self):

        s = Supermarket([   
                            ['a','b'], 
                            [],
                            ['a','c','d']
                        ])

        self.assertEqual(to_list(s), [   
                                       ['a','b'], 
                                       [],
                                       ['a','c','d']
                                    ])
        
class StrTest(unittest.TestCase):

    def test_01_str(self):

        s = Supermarket([   
                        ['x','y'], 
                        [],
                        ['z','w','t']
                   ])
        self.assertTrue('0' in str(s))
        self.assertTrue('2' in str(s))
        self.assertTrue("w" in str(s))

class SizeTest(unittest.TestCase):

    def test_size(self):
        self.assertEqual(Supermarket([[]]).size(), 0) 
        self.assertEqual(Supermarket([['a']]).size(), 1) 
        self.assertEqual(Supermarket([   
                            ['a','b'], 
                            [],
                            ['a','c','d']
                        ]).size(), 5) 

class DequeueTest(unittest.TestCase):

    def test_01_empty(self):
        s = Supermarket([[]])

        self.assertEqual(s.dequeue(), [])
        self.assertEqual(to_list(s), [[]])

    def test_02_a(self):
        s = Supermarket([['a']])

        self.assertEqual(s.dequeue(), ['a'])
        self.assertEqual(to_list(s), [[]])

    def test_03_a_b(self):
        s = Supermarket([['a'], ['b']])

        self.assertEqual(s.dequeue(), ['a', 'b'])
        self.assertEqual(to_list(s), [[], []])

    def test_04_a_empty(self):
        s = Supermarket([['a'], []])

        self.assertEqual(s.dequeue(), ['a'])
        self.assertEqual(to_list(s), [[], []])

    def test_05_empty_a(self):
        s = Supermarket([[], ['a']])

        self.assertEqual(s.dequeue(), ['a'])
        self.assertEqual(to_list(s), [[], []])

    def test_06_ab_c(self):
        s = Supermarket([['a','b'], ['c']])

        self.assertEqual(s.dequeue(), ['a','c'])
        self.assertEqual(to_list(s), [['b'], []])
        self.assertEqual(s.dequeue(), ['b'])
        self.assertEqual(to_list(s), [[], []])

    def test_07_abc_c_de(self):
        s = Supermarket([['a','b','c'], ['c'], ['d', 'e']])

        self.assertEqual(s.dequeue(), ['a','c','d'])
        self.assertEqual(to_list(s), [['b','c'], [], ['e']])
        self.assertEqual(s.dequeue(), ['b','e'])
        self.assertEqual(to_list(s), [['c'],[],[]])
        self.assertEqual(s.dequeue(), ['c'])
        self.assertEqual(to_list(s), [[],[],[]])
        

class EnqueueTest(unittest.TestCase):

    def test_01_abc(self):
        s = Supermarket([[]])
        s.enqueue('a')                   
        self.assertEqual(to_list(s), [['a']])
        s.enqueue('b')                   
        self.assertEqual(to_list(s), [['a','b']])
        s.enqueue('c')                   
        self.assertEqual(to_list(s), [['a','b','c']])

    def test_02_a_empty(self):
        s = Supermarket([['a'],[]])
        s.enqueue('b')                   
        self.assertEqual(to_list(s), [['a'],['b']])

    def test_03_empty_a(self):
        s = Supermarket([[],['a']])
        s.enqueue('b')                   
        self.assertEqual(to_list(s), [['b'],['a']])

    def test_04_abg_ce_df(self):
        s = Supermarket([['a','b'],['c'],['d']])
        s.enqueue('e')
        self.assertEqual(to_list(s), [['a','b'],['c','e'],['d']])
        s.enqueue('f')
        self.assertEqual(to_list(s), [['a','b'],['c','e'],['d','f']])
        s.enqueue('g')
        self.assertEqual(to_list(s), [['a','b','g'],['c','e'],['d','f']])

