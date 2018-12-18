
from circular_queue_solution import *
import unittest


class InitCapacityTest(unittest.TestCase):
    
    def test_01_type(self):
        
        with self.assertRaises(ValueError):
            q = CircularQueue(3.5)

    def test_02_negative(self):
        
        with self.assertRaises(ValueError):
            q = CircularQueue(-2)
            
    def test_03_zero(self):
        
        with self.assertRaises(ValueError):
            q = CircularQueue(0)
            
    def test_04_one(self):
        q = CircularQueue(1)
        self.assertEqual(q.capacity(), 1)
        self.assertTrue(q.is_empty())

    def test_05_two(self):           
        self.assertEqual(CircularQueue(2).capacity(), 2)

class EnqueueTest(unittest.TestCase):

    def test_01_exceed_capacity(self):
        q = CircularQueue(1)
        q.enqueue('a')
        self.assertFalse(q.is_empty())
        
        with self.assertRaises(BufferError):
            q.enqueue('b')
    
    def test_02_empty(self):
        q = CircularQueue(5)
                
        self.assertEqual(q.size(), 0)
        with self.assertRaises(LookupError):
            q.top()
                
    def test_03_simple(self):
        q = CircularQueue(5)
                
        q.enqueue('a')                    
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.size(), 1)
        q.enqueue('b')        
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.size(), 2)
                        
    def test_04_circular(self):
        q = CircularQueue(2)    # 2 elements capacity  [head->None,None]

        q.enqueue('a')                     # [head->a, None]                    
        self.assertEqual(q.top(), 'a')   
        self.assertEqual(q.size(), 1)
        
        q.enqueue('b')                     # [head->a, b]
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.size(), 2)
        
        with self.assertRaises(BufferError):
            q.enqueue('c')
    
        
class DequeueTest(unittest.TestCase):
    
    def test_01_empty(self):
        q = CircularQueue(5)      
        with self.assertRaises(LookupError):
            q.dequeue()
        
            
    def test_02_simple(self):
        q = CircularQueue(5)        
        q.enqueue('a')                        # [head->a, None]
        q.enqueue('b')                        # [head->a, b]  
    
        self.assertEqual(q.dequeue(), 'a')    # [a, head->b]
        self.assertEqual(q.top(), 'b')
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 'b')    # [head->a, b]     
        self.assertEqual(q.size(), 0)
        
    def test_03_circular(self):
        q = CircularQueue(2)    # 2 elements capacity  [head->None,None]
        q.enqueue('z')  # [head->z,None]
        q.dequeue()     # so head is moved of 1 left [z,head->None]
        self.assertEqual(q.size(), 0)

        q.enqueue('a')                     # [z,head->a]                    
        self.assertEqual(q.top(), 'a')   
        self.assertEqual(q.size(), 1)
        q.enqueue('b')                     # [b,head->a]
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.size(), 2)
        
        self.assertEqual(q.dequeue(), 'a') # [head->b,a] 
        self.assertEqual(q.top(), 'b')
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 'b') # [b,head->a]
        self.assertEqual(q.size(), 0)

        