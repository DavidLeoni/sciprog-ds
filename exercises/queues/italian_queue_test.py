
from italian_queue_solution import *
import unittest


def to_py(italian_queue):
    """ Returns provided italian_queue as a regular Python list, in the 
        form [(v1,g1), (v2,g2), ...]. 
        
        WARNING: use it ONLY for testing!
    """
    python_list = []
    current = italian_queue._head        
    
    while (current != None):
        python_list.append((current.get_data(), current.get_group()))
        current = current.get_next()                       
    return python_list        


class InitEmptyTest(unittest.TestCase):
                
    def test_01_empty(self):
        q = ItalianQueue()
                
        self.assertEqual(q.size(), 0)        
        self.assertTrue(q.is_empty())
        
        with self.assertRaises(LookupError):
            q.top()
        
        with self.assertRaises(LookupError):
            q.top_group()

        with self.assertRaises(LookupError):
            q.tail()
        
        with self.assertRaises(LookupError):
            q.tail_group()
            
            
class EnqueueTest(unittest.TestCase):

    
    def test_01_ag(self):
        q = ItalianQueue()    

        q.enqueue('a', 'g')                      # [(a,g)]
        self.assertFalse(q.is_empty())        
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.top(), 'a')           
        self.assertEqual(q.top_group(), 'g')
        self.assertEqual(q.tail(), 'a')
        self.assertEqual(q.tail_group(), 'g')

    
    def test_02_agbh(self):
        q = ItalianQueue()    

        q.enqueue('a', 'g')                      # [(a,g)]                         
        
        q.enqueue('b', 'h')                      # [(a,g), (b,h)]        
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'a')           
        self.assertEqual(q.top_group(), 'g')
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'h')
    
    
    def test_03_agbg(self):
        q = ItalianQueue()    

        q.enqueue('a', 'g')                      # [(a,g)]                                 
        q.enqueue('b', 'g')                      # [(a,g), (b,g)]
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.top_group(), 'g')
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'g')                    

    def test_04_agbhcg(self):
        q = ItalianQueue()    

        q.enqueue('a', 'g')                      # [(a,g)]                                 
        q.enqueue('b', 'h')                      # [(a,g), (b,h)]
        q.enqueue('c', 'g')                      # [(a,g), (c,g), (b,h)]
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.top_group(), 'g')
        self.assertEqual(q._head.get_next().get_data(), 'c')   # white box testing: using private '_' fields 
        self.assertEqual(q._head.get_next().get_group(), 'g')  # white box testing: using private '_' fields 
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'h')                    
        
        
        
class DequeueTest(unittest.TestCase):
    
    def test_01_empty(self):
        q = ItalianQueue()      
                
        with self.assertRaises(LookupError):
            q.dequeue()
    
    def test_02_ag(self):
        q = ItalianQueue()      
        q.enqueue('a', 'g')                      # [(a,g)]        
        self.assertEqual(q.dequeue(), 'a')       # []
        self.assertEqual(q.size(), 0)        
        
        with self.assertRaises(LookupError):
            q.top()
    
        with self.assertRaises(LookupError):
            q.top_group()
        
        with self.assertRaises(LookupError):
            q.tail()
        
        with self.assertRaises(LookupError):
            q.tail_group()
        
        with self.assertRaises(LookupError):
            q.dequeue()
    
    
    def test_03_agbh(self):
        q = ItalianQueue()        
        q.enqueue('a','g')                   # [(a,g)]           
        q.enqueue('b','h')                   # [(a,g), (b,h)]  
    
        self.assertEqual(q.dequeue(), 'a')   # [(b,h)] 
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.top(), 'b')      
        self.assertEqual(q.top_group(), 'h')
        self.assertEqual(q.tail(), 'b')      
        self.assertEqual(q.tail_group(), 'h')
        
        self.assertEqual(q.dequeue(), 'b')   # []       
        self.assertEqual(q.size(), 0)        
        