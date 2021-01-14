
from bank_sol import *
import unittest



class StrTest(unittest.TestCase):
    
    def test_str(self):
        b = Bank()
        b._trans = ['a','b','c']
        self.assertTrue('Bank' in str(b))
        self.assertTrue('a,b,c' in str(b))


class LogTest(unittest.TestCase):

    
    def test_01_ab(self):
        b = Bank()
        b.log('a')
        self.assertEqual(b.pos(('a','b')), [])
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [0])
        self.assertEqual(b.pos(('b','a')), [])
        self.assertEqual(b.pos(('a','c')), [])
        self.assertEqual(b.pos(('a','a')), [])
        self.assertEqual(b.pos(('b','b')), [])


    def test_02_bab(self):
        b = Bank()
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [])
        b.log('a')
        self.assertEqual(b.pos(('b','a')), [0])
        self.assertEqual(b.pos(('a','b')), [])
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [1])
        self.assertEqual(b.pos(('b','a')), [0])
        self.assertEqual(b.pos(('a','c')), [])
        self.assertEqual(b.pos(('a','a')), [])
        self.assertEqual(b.pos(('b','b')), [])


    def test_03_aaa(self):
        b = Bank()
        b.log('a')
        self.assertEqual(b.pos(('a','a')), [])
        b.log('a')
        self.assertEqual(b.pos(('a','a')), [0])
        b.log('a')
        self.assertEqual(b.pos(('a','a')), [0,1])
        self.assertEqual(b.pos(('a','b')), [])
        self.assertEqual(b.pos(('b','a')), [])


    def test_04_abcabab(self):
        b = Bank()
        b.log('a')
        self.assertEqual(b.pos(('a','b')), [])
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [0])
        b.log('c')
        self.assertEqual(b.pos(('a','b')), [0])
        self.assertEqual(b.pos(('a','c')), [])
        self.assertEqual(b.pos(('b','c')), [1])
        b.log('a')
        self.assertEqual(b.pos(('a','b')), [0])
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [0, 3])
        b.log('a')
        self.assertEqual(b.pos(('a','b')), [0, 3])
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [0, 3, 5])                             
        
class RevertTest(unittest.TestCase):
    
    def test_01_empty(self):
        b = Bank()
        with self.assertRaises(IndexError):
            b.revert()
    
    
    def test_02_ab(self):
        b = Bank()
        b.log('a')        
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [0])
        self.assertEqual(b.revert(), 'b')
        self.assertEqual(b.pos(('a','b')), [])        
        self.assertEqual(b.revert(), 'a')
        with self.assertRaises(IndexError):
            b.revert()
            
    def test_03_abcab(self):
        b = Bank()
        b.log('a')        
        b.log('b')
        b.log('c')
        b.log('a')        
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [0,3])
        self.assertEqual(b.revert(), 'b')
        self.assertEqual(b.pos(('a','b')), [0])
        self.assertEqual(b.pos(('c','a')), [2])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('c','a')), [])
        self.assertEqual(b.revert(), 'c')
        self.assertEqual(b.pos(('c','a')), [])
        self.assertEqual(b.pos(('a','b')), [0])
        self.assertEqual(b.revert(), 'b')
        self.assertEqual(b.pos(('a','b')), [])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','b')), [])

    def test_04_aaa(self):
        b = Bank()
        b.log('a')        
        b.log('a')
        b.log('a')
        self.assertEqual(b.pos(('a','a')), [0,1])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('b','b')), [])
        self.assertEqual(b.pos(('a','a')), [0])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','a')), [])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','a')), [])        
        with self.assertRaises(IndexError):
            b.revert()  
            
class MaxIntervalTest(unittest.TestCase):
    
    def test_01_empty(self):
        b = Bank()
        with self.assertRaises(LookupError):
            b.max_interval(('a','b'), ('c','d'))
        
        
    def test_02_ab(self):
        b = Bank()
        b.log('a')
        b.log('b')

        with self.assertRaises(LookupError):
            b.max_interval(('c','d'), ('a','b'))

        with self.assertRaises(LookupError):
            b.max_interval(('a','b'), ('c','d'))
        
        with self.assertRaises(LookupError):
            b.max_interval(('a','b'), ('a','b'))
            
    def test_03_abcd(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('c')
        b.log('d')
        
        self.assertEqual(b.max_interval(('a','b'), ('c','d')), [])

        with self.assertRaises(LookupError):
            b.max_interval(('c','d'), ('a','b'))
        
        with self.assertRaises(LookupError):
            b.max_interval(('a','b'), ('a','b'))
                           
        with self.assertRaises(LookupError):
            b.max_interval(('c','d'), ('c','d'))
            
        with self.assertRaises(LookupError):
            b.max_interval(('b','c'), ('c','d'))
            
        with self.assertRaises(LookupError):
            b.max_interval(('a','b'), ('b','c'))
                           
    def test_04_abab(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('a')
        b.log('b')
        
        self.assertEqual(b.max_interval(('a','b'), ('a','b')), [])

        with self.assertRaises(LookupError):
            b.max_interval(('c','d'), ('a','b'))
                           
        with self.assertRaises(LookupError):
            b.max_interval(('a','b'), ('b','a'))

    def test_05_abacd(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('a')
        b.log('c')
        b.log('d')
        
        self.assertEqual(b.max_interval(('a','b'), ('c','d')), ['a'])
        self.assertEqual(b.max_interval(('b','a'), ('c','d')), [])
        self.assertEqual(b.max_interval(('a','b'), ('a','c')), [])

        with self.assertRaises(LookupError):
            b.max_interval(('c','d'), ('a','b'))


    def test_06_abcdab(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('c')
        b.log('d')
        b.log('a')
        b.log('b')
        
        self.assertEqual(b.max_interval(('a','b'), ('c','d')), [])
        self.assertEqual(b.max_interval(('a','b'), ('a','b')), ['c','d'])
        self.assertEqual(b.max_interval(('b','c'), ('a','b')), ['d'])
        self.assertEqual(b.max_interval(('a','b'), ('d','a')), ['c'])
        self.assertEqual(b.max_interval(('c','d'), ('a','b')), [])
        

        with self.assertRaises(LookupError):            
            b.max_interval(('a','b'), ('a','c'))


    def test_07_aaaaaaa(self):
        b = Bank()
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        
        self.assertEqual(b.max_interval(('a','a'), ('a','a')), list('aaa'))

        with self.assertRaises(LookupError):
            b.max_interval(('a','b'), ('a','a'))
                           
                           
    def test_08_complex(self):
        bank = Bank()
        
        bank.log('c')
        bank.log('d')
        bank.log('c')
        bank.log('a')
        bank.log('b') # <--- b 
        bank.log('e') #      e
        bank.log('f') #      --- f     |
        bank.log('a') #          a     |
        bank.log('f') #          f     | k
        bank.log('c') #          c     |
        bank.log('b') #      --- b     |
        bank.log('a') # <--- a 
        bank.log('f') #      f
        bank.log('b')
        bank.log('e')
        bank.log('l')
        
        self.assertEqual(bank.max_interval(('b','e'), ('a','f')), list('fafcb'))
        self.assertEqual(bank.max_interval(('a','f'), ('b','e')), list('cbaf'))
        self.assertEqual(bank.max_interval(('b','e'), ('b','e')), list('fafcbaf'))
        self.assertEqual(bank.max_interval(('a','f'), ('a','f')), list('cb'))

        with self.assertRaises(LookupError):
            bank.max_interval(('f','a'), ('e','b'))

