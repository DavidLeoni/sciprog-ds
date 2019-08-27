import unittest
from backpack_solution import *

class BackpackTest(unittest.TestCase):    

    def test_01_init(self): 
        bp = Backpack(10)
        self.assertEqual(bp.max_weight(), 10)
        self.assertEqual(bp._elements, [])

        bp = Backpack(0)  # allowed

        with self.assertRaises(ValueError):
            bpneg = Backpack(-1)


    def test_02_weight(self):
        bp = Backpack(10)
        self.assertEqual(bp.weight(), 0)
        

    def test_03_size(self):
        bp = Backpack(10)        
        self.assertEqual(bp.size(), 0)
        bp.push('a',7)
        self.assertEqual(bp.size(), 1)
        bp.pop()
        self.assertEqual(bp.size(), 0)
    
    def test_04_str(self):
        bp = Backpack(10)
        bp.push('a',5)
        bp.push('b',3)
        self.assertTrue('10' in bp.__str__())
        self.assertTrue('max_weight' in bp.__str__())
        self.assertTrue('weight' in bp.__str__())
        self.assertTrue( "8" in bp.__str__())
        self.assertTrue( "('a', 5)" in bp.__str__())
        self.assertTrue("('b', 3)" in  bp.__str__())


    def test_05_is_empty(self):
        bp = Backpack(10)
        self.assertTrue(bp.is_empty())
        bp.push('a',4)
        self.assertFalse(bp.is_empty())
         
                        
    def test_06_push(self):
        bp = Backpack(30)        
        self.assertEqual(bp.size(), 0)
        bp.push('a',5)
        self.assertEqual(bp.size(), 1)
        self.assertEqual(bp.peek(), ('a',5))
        self.assertEqual(bp.weight(), 5)
        bp.push('b',3)
        self.assertEqual(bp.size(), 2)
        self.assertEqual(bp.peek(), ('b',3))
        self.assertEqual(bp.weight(), 8)
        bp.push('c',1)
        self.assertEqual(bp.size(), 3)
        self.assertEqual(bp.peek(), ('c',1))
        self.assertEqual(bp.weight(), 9)

    def test_07_push_max_weight(self):
        bp = Backpack(5)
        with self.assertRaises(ValueError):
            bp.push('a',7)

        bp = Backpack(5)
        bp.push('a',5)  # ok
        with self.assertRaises(ValueError):
            bp.push('b',1)  # one too much

    def test_08_push_increasing(self):
        bp = Backpack(30)
        bp.push('a',5)
        bp.push('b',5)  # equal allowed
        with self.assertRaises(ValueError):
            bp.push('c',6)


    def test_09_peek(self):
        
        bp = Backpack(30)
        with self.assertRaises(IndexError):
            self.assertEqual(bp.peek(), None)         
        bp.push('a',5)
        self.assertEqual(bp.peek(), ('a',5))
        self.assertEqual(bp.peek(), ('a',5))  # testing peek is not changing the stack
        self.assertEqual(bp.size(), 1)
        bp.push('b',4)
        self.assertEqual(bp.peek(), ('b',4))

    def test_10_pop(self):
        
        bp = Backpack(30) 
        self.assertEqual(bp.weight(), 0)
        with self.assertRaises(IndexError):
            bp.pop()
        bp.push('a',7)
        self.assertEqual(bp.pop(), ('a',7))
        self.assertEqual(bp.weight(), 0)
        bp.push('b',5)
        bp.push('c',4)
        self.assertEqual(bp.weight(), 9)
        self.assertEqual(bp.pop(), ('c',4))
        self.assertEqual(bp.weight(), 5)
        self.assertEqual(bp.pop(), ('b',5))
        self.assertEqual(bp.weight(), 0)

        with self.assertRaises(IndexError):
            bp.pop()

class RemoveTest(unittest.TestCase):

    def test_01_empty_a(self):
        bp = Backpack(10)
        with self.assertRaises(ValueError):
            remove(bp,'a')

    def test_02_a_b(self):
        bp = Backpack(10)
        bp.push('a',5)
        with self.assertRaises(ValueError):
            remove(bp,'b')

    def test_03_a_a(self):
        bp = Backpack(10)
        bp.push('a',5)
        self.assertEqual(remove(bp,'a'), ('a',5))
        self.assertTrue(bp.is_empty())

    def test_04_ba_b(self):
        bp = Backpack(30)
        bp.push('b',7)
        bp.push('a',5)
        self.assertEqual(remove(bp,'b'), ('b',7))
        self.assertEqual(bp._elements, [('a',5)])

    def test_05_ba_a(self):
        bp = Backpack(30)
        bp.push('b',7)
        bp.push('a',5)
        self.assertEqual(remove(bp, 'a'), ('a',5))
        self.assertEqual(bp._elements, [('b',7)])

    def test_06_aba_a(self):
        bp = Backpack(30)
        bp.push('a',5)
        bp.push('b',5)
        bp.push('a',5)
        self.assertEqual(remove(bp,'a'), ('a',5))
        self.assertEqual(bp._elements, [('a',5), ('b', 5)])

    def test_07_abb_a(self):
        bp = Backpack(30)
        bp.push('a',7)
        bp.push('b',5)
        bp.push('b',5)
        self.assertEqual(remove(bp, 'b'), ('b',5))
        self.assertEqual(bp._elements, [('a',7),('b',5)])

    def test_08_complex(self):
        bp = Backpack(50)

        bp.push('a',9)
        bp.push('b',8)
        bp.push('c',8)
        bp.push('b',8)
        bp.push('d',7)
        bp.push('e',5)
        bp.push('f',2)        
        
        remove(bp, 'b')

        self.assertEqual(bp._elements, [('a', 9), ('b', 8), ('c', 8), ('d', 7), ('e', 5), ('f', 2)])

 