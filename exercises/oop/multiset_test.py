import unittest
from multiset_sol import * 

class AddGetTest(unittest.TestCase):
    
    def test_01_get_non_existing(self):
        m = MultiSet()
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get(666),0)
        
    
    def test_02_aa(self):
        
        m = MultiSet()        
        self.assertEqual(m.get('a'),0)
        m.add('a')
        self.assertEqual(m.get('a'),1)
        m.add('a')
        self.assertEqual(m.get('a'),2)
        
    def test_03_aabb(self):
        
        m = MultiSet()        
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),0)        
        m.add('a')
        self.assertEqual(m.get('a'),1)
        self.assertEqual(m.get('b'),0)        
        m.add('a')
        self.assertEqual(m.get('a'),2)
        self.assertEqual(m.get('b'),0)        
        m.add('b')
        self.assertEqual(m.get('a'),2)        
        self.assertEqual(m.get('b'),1)
        m.add('b')
        self.assertEqual(m.get('a'),2)        
        self.assertEqual(m.get('b'),2)
    
class RemovenTest(unittest.TestCase):

    def test_01_removen_nothing(self):
        m = MultiSet()
        m.add('a')
        m.removen('a', 0)
        self.assertEqual(m.get('a'), 1)
        m.removen('b', 0)
        self.assertEqual(m.get('b'), 0)
        
    
    def test_02_removen_aa_non_existing(self):
        m = MultiSet()
        m.add('a')
        m.add('a')
        
        with self.assertRaises(LookupError):
            m.removen('a',3)  # too many

        with self.assertRaises(LookupError):            
            m.removen('b',1) # never inserted                
    
    def test_03_aa(self):
        
        m = MultiSet()        
        m.add('a')
        m.add('a')
        self.assertEqual(m.get('a'),2)
        m.removen('a', 1)
        self.assertEqual(m.get('a'),1)        
        m.removen('a', 1)
        self.assertEqual(m.get('a'),0)
        m.removen('a', 0)
        self.assertEqual(m.get('a'),0)
      
    def test_04_aab(self):
        
        m = MultiSet()        
        m.add('a')
        m.add('a')
        m.add('b')
        self.assertEqual(m.get('a'),2)
        self.assertEqual(m.get('b'),1)
        m.removen('a', 2)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),1)
        self.assertEqual(m.get('b'),1)
        m.removen('a',0)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),1)      
        m.removen('b', 1)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),0)      
        m.removen('b', 0)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),0)      
