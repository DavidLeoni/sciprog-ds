import unittest
from sorted_stack_sol import *
        
class SortedStackTest(unittest.TestCase):
               
    def test_01_size(self):
        s = SortedStack(True)
        self.assertEqual(s.size(), 0)
        s.push(5)
        self.assertEqual(s.size(), 1)
        s.pop()
        self.assertEqual(s.size(), 0)

    
    def test_02_is_empty(self):
        s = SortedStack(True)
        self.assertTrue(s.is_empty())
        s.push(5)
        self.assertFalse(s.is_empty())

    def test_03_peek_empty(self):
        s = SortedStack(True)
        with self.assertRaises(IndexError):
            s.peek()

    def test_04_peek_one(self):
        s = SortedStack(True)        
        s.push(5)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.peek(), 5)  # testing peek is not changing the stack
        self.assertEqual(s.size(), 1)     
        
    def test_05_pop_empty(self):
        s = SortedStack(True) 
        with self.assertRaises(IndexError):
            s.pop()
            
    def test_06_pop_one(self):
        s = SortedStack(True) 
        with self.assertRaises(IndexError):
            s.pop()
        s.push(5)        
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.size(), 0)
        
    def test_07_pop_two(self):
        s = SortedStack(True)     
        with self.assertRaises(IndexError):
            s.pop()
        s.push(5)
        s.push(6)        
        self.assertEqual(s.pop(), 6)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.size(), 0)
        with self.assertRaises(IndexError):
            s.pop()
                        
    def test_08_push_non_integer(self):
        s = SortedStack(True)        
        with self.assertRaises(ValueError):
            s.push("evil string")
    
    def test_09_push(self):
        s = SortedStack(True)        
        self.assertEqual(s.size(), 0)
        s.push(5)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.peek(), 5)
        s.push(6)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), 6)
        s.push(6) 
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 6)
        with self.assertRaises(ValueError):
            s.push(5)
    

    def test_09_descending(self):
        s = SortedStack(False)        
        self.assertEqual(s.size(), 0)
        s.push(8)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.peek(), 8)
        s.push(6)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), 6)
        s.push(6) 
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 6)
        with self.assertRaises(ValueError):
            s.push(7)

    def test_10_str(self):
        s = SortedStack(True)
        s.push(5)
        s.push(6)        
        self.assertTrue( 'ascending' in str(s))
        self.assertTrue( '5' in str(s))
        self.assertTrue( '6' in str(s))
        self.assertTrue( 'SortedStack' in str(s))

        s2 = SortedStack(False)
        self.assertTrue( 'descending' in str(s2))
    

class TransferTest(unittest.TestCase):
    
    def test_empty(self):
        s1 = SortedStack(True)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 0)                
            
    def test_one(self):
        s1 = SortedStack(True)
        s1.push(5)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 1)
        self.assertEquals(s2.peek(), 5)
                

    def test_two_ascending(self):
        s1 = SortedStack(True)
        s1.push(5)        
        s1.push(6)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 2)
        self.assertEquals(s2.ascending(), False)        
        self.assertEquals(s2.pop(), 5)
        self.assertEquals(s2.pop(), 6)


    def test_two_descending(self):
        s1 = SortedStack(False)
        s1.push(6)        
        s1.push(5)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 2)
        self.assertEquals(s2.ascending(), True)        
        self.assertEquals(s2.pop(), 6)
        self.assertEquals(s2.pop(), 5)

class MergeTest(unittest.TestCase):
    
    def test_empty(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)

        m = merge(s1,s2)
        self.assertEqual(m.size(), 0)        
        
    def test_input_asc(self):
        """ Inputs must be ascending """
        
        with self.assertRaises(ValueError):
            merge(SortedStack(False),SortedStack(True))

        with self.assertRaises(ValueError):
            merge(SortedStack(True),SortedStack(False))

        with self.assertRaises(ValueError):
            merge(SortedStack(False),SortedStack(False))
            
        
    def test_1_empty(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s1.push(1)
        m = merge(s1,s2)

        self.assertEqual(m.size(), 1)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.peek(), 1)

    def test_empty_1(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s2.push(1)
        m = merge(s1,s2)
        self.assertEqual(m.size(), 1)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.peek(), 1)

    def test_1_2(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s1.push(1)
        s2.push(2)
        m = merge(s1,s2)
        
        self.assertEqual(m.size(), 2)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)

    def test_2_1(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s1.push(2)
        s2.push(1)
        m = merge(s1,s2)
        
        self.assertEqual(m.size(), 2)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)        
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)


    def test_12_3(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)

        s1.push(1)
        s1.push(2)        
        s2.push(3)
        m = merge(s1,s2)
        self.assertEqual(m.size(), 3)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)
        self.assertEqual(m.pop(), 3)


    def test_3_12(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)

        s1.push(3)
        s2.push(1)        
        s2.push(2)
        m = merge(s1,s2)
        self.assertEqual(m.size(), 3)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)
        self.assertEqual(m.pop(), 3)
