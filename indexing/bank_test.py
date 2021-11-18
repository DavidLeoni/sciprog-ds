
from bank_sol import *
import unittest


class StrTest(unittest.TestCase):
    
    def test_str(self):
        b = Bank()
        b._trans = ['a','b','c']
        self.assertTrue('Bank' in str(b))
        self.assertTrue('a,b,c' in str(b))


class LogTest(unittest.TestCase):

    
    def test_01_abc(self):
        b = Bank()
        b.log('a')
        self.assertEqual(b.pos(('a','b','c')), [])
        b.log('b')
        
        ret = b.pos(('a','b','c'))
        self.assertEqual(ret, [])

        b.log('c')
        ret = b.pos(('a','b','c'))
        self.assertEqual(ret, [0])

        # check it's returning a NEW list
        ret.append(666)   
        self.assertEqual(b.pos(('a','b','c')), [0])
        
        self.assertEqual(b.pos(('b','a','c')), [])
        self.assertEqual(b.pos(('a','c','b')), [])
        self.assertEqual(b.pos(('a','a','a')), [])
        self.assertEqual(b.pos(('b','b','b')), [])

                
    def test_02_cbabc(self):
        b = Bank()
        b.log('c')
        self.assertEqual(b.pos(('a','b','c')), [])
        b.log('b')
        self.assertEqual(b.pos(('b','a','c')), [])
        b.log('a')
        self.assertEqual(b.pos(('c','b','a')), [0])
        self.assertEqual(b.pos(('a','b','c')), [])
        b.log('b')
        self.assertEqual(b.pos(('c','b','a')), [0])
        self.assertEqual(b.pos(('b','a','b')), [1])
        self.assertEqual(b.pos(('a','b','a')), [])
        b.log('c')        
        self.assertEqual(b.pos(('c','b','a')), [0])
        self.assertEqual(b.pos(('b','a','b')), [1])
        self.assertEqual(b.pos(('a','b','c')), [2])        
        self.assertEqual(b.pos(('a','c','b')), [])
        self.assertEqual(b.pos(('a','a','a')), [])
        self.assertEqual(b.pos(('c','c','c')), [])


    def test_03_aaaa(self):
        b = Bank()
        b.log('a')
        self.assertEqual(b.pos(('a','a','a')), [])
        b.log('a')
        self.assertEqual(b.pos(('a','a','a')), [])        
        b.log('a')
        self.assertEqual(b.pos(('a','a','a')), [0])
        b.log('a')
        self.assertEqual(b.pos(('a','a','a')), [0,1])
        self.assertEqual(b.pos(('a','a','b')), [])
        self.assertEqual(b.pos(('b','a','a')), [])

    #           012345678910 
    def test_04_abcdabcabca(self):
        b = Bank()
        b.log('a')
        self.assertEqual(b.pos(('a','b')), [])
        b.log('b')
        self.assertEqual(b.pos(('a','b')), [])
        b.log('c')
        self.assertEqual(b.pos(('a','b','c')), [0])
        self.assertEqual(b.pos(('a','c')), [])
        b.log('d')        
        self.assertEqual(b.pos(('b','c','d')), [1])
        b.log('a')
        self.assertEqual(b.pos(('a','b','c')), [0])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.pos(('c','d','a')), [2])
        b.log('b')
        self.assertEqual(b.pos(('a','b','c')), [0])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.pos(('c','d','a')), [2])
        self.assertEqual(b.pos(('d','a','b')), [3])
        b.log('c')
        self.assertEqual(b.pos(('a','b','c')), [0,4])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.pos(('c','d','a')), [2])
        self.assertEqual(b.pos(('d','a','b')), [3])        
        b.log('a')
        self.assertEqual(b.pos(('a','b','c')), [0,4])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.pos(('c','d','a')), [2])
        self.assertEqual(b.pos(('d','a','b')), [3])        
        self.assertEqual(b.pos(('b','c','a')), [5])
        b.log('b')
        self.assertEqual(b.pos(('a','b','c')), [0,4])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.pos(('c','d','a')), [2])
        self.assertEqual(b.pos(('d','a','b')), [3])        
        self.assertEqual(b.pos(('b','c','a')), [5])
        self.assertEqual(b.pos(('c','a','b')), [6])
        b.log('c')
        self.assertEqual(b.pos(('a','b','c')), [0,4,7])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.pos(('c','d','a')), [2])
        self.assertEqual(b.pos(('d','a','b')), [3])        
        self.assertEqual(b.pos(('b','c','a')), [5])
        self.assertEqual(b.pos(('c','a','b')), [6])
        b.log('a')
        self.assertEqual(b.pos(('a','b','c')), [0,4,7])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.pos(('c','d','a')), [2])
        self.assertEqual(b.pos(('d','a','b')), [3])        
        self.assertEqual(b.pos(('b','c','a')), [5,8])
        self.assertEqual(b.pos(('c','a','b')), [6])
    
        
class RevertTest(unittest.TestCase):
    
    def test_01_empty(self):
        b = Bank()
        with self.assertRaises(IndexError):
            b.revert()
        
    def test_02_abc(self):
        b = Bank()
        b.log('a')        
        b.log('b')
        b.log('c')
        self.assertEqual(b.pos(('a','b','c')), [0])
        self.assertEqual(b.revert(), 'c')
        self.assertEqual(b.pos(('a','b','c')), [])
        self.assertEqual(b.revert(), 'b')
        self.assertEqual(b.pos(('a','b','c')), [])
        self.assertEqual(b.revert(), 'a')
        with self.assertRaises(IndexError):
            b.revert()

    #           0123456
    def test_03_abcdabc(self):
        b = Bank()
        b.log('a')        
        b.log('b')
        b.log('c')
        b.log('d')
        b.log('a')        
        b.log('b')
        b.log('c')
        self.assertEqual(b.pos(('a','b','c')), [0,4])
        self.assertEqual(b.revert(), 'c')
        self.assertEqual(b.pos(('a','b','c')), [0])
        self.assertEqual(b.pos(('c','d','a')), [2])
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.revert(), 'b')
        self.assertEqual(b.pos(('b','c','d')), [1])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('c','d','a')), [])
        self.assertEqual(b.revert(), 'd')
        self.assertEqual(b.pos(('b','c','d')), [])        
        self.assertEqual(b.pos(('a','b','c')), [0])        
        self.assertEqual(b.revert(), 'c')
        self.assertEqual(b.pos(('a','b','c')), [])                
        self.assertEqual(b.revert(), 'b')
        self.assertEqual(b.pos(('a','b','c')), [])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','b','c')), [])

#               01234
    def test_04_aaaaa(self):
        b = Bank()
        b.log('a')        
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        self.assertEqual(b.pos(('a','a','a')), [0,1,2])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('b','b','b')), [])
        self.assertEqual(b.pos(('a','a','a')), [0,1])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','a','a')), [0])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','a','a')), [])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','a','a')), [])
        self.assertEqual(b.revert(), 'a')
        self.assertEqual(b.pos(('a','a','a')), [])
        with self.assertRaises(IndexError):
            b.revert()  
            
class MaxIntervalTest(unittest.TestCase):
    
    def test_01_empty(self):
        b = Bank()
        with self.assertRaises(LookupError):
            b.max_interval(('a','b','c'), ('d','e','f'))
        
        
    def test_02_abc(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('c')

        with self.assertRaises(LookupError):
            b.max_interval(('c','d','e'), ('a','b','c'))

        with self.assertRaises(LookupError):
            b.max_interval(('a','b','c'), ('c','d','e'))
        
        with self.assertRaises(LookupError):
            b.max_interval(('a','b','c'), ('a','b','c'))
            
    def test_03_abcdef(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('c')
        b.log('d')
        b.log('e')
        b.log('f')
        
        self.assertEqual(b.max_interval(('a','b','c'), ('d','e','f')), [])

        with self.assertRaises(LookupError):
            b.max_interval(('c','d','e'), ('a','b','c'))
        
        with self.assertRaises(LookupError):
            b.max_interval(('a','b','c'), ('a','b','c'))
                           
        with self.assertRaises(LookupError):
            b.max_interval(('c','d','e'), ('c','d','e'))
            
        with self.assertRaises(LookupError):
            b.max_interval(('b','c','d'), ('c','d','e'))
            
        with self.assertRaises(LookupError):
            b.max_interval(('a','b','c'), ('c','d','e'))
                           
    def test_04_abcabc(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('c')
        b.log('a')
        b.log('b')
        b.log('c')

        self.assertEqual(b.max_interval(('a','b','c'), ('a','b','c')), [])

        with self.assertRaises(LookupError):
            b.max_interval(('c','d','e'), ('a','b','c'))
                           
        with self.assertRaises(LookupError):
            b.max_interval(('a','b','c'), ('c','b','a'))
    
    def test_05_abababac(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('a')
        b.log('b')
        b.log('a')
        b.log('b')
        b.log('a')
        b.log('c')
        
        self.assertEqual(b.max_interval(('a','b','a'), ('a','b','a')), ['b'])
        self.assertEqual(b.max_interval(('b','a','b'), ('a','b','a')), [])
        self.assertEqual(b.max_interval(('b','a','b'), ('b','a','c')), ['a'])
        self.assertEqual(b.max_interval(('b','a','b'), ('a','b','a')), [])
        self.assertEqual(b.max_interval(('a','b','a'), ('b','a','c')), ['b','a'])

        with self.assertRaises(LookupError):
            b.max_interval(('a','c'), ('a','b','a'))


    def test_06_abccdabc(self):
        b = Bank()
        b.log('a')
        b.log('b')
        b.log('c')
        b.log('c')
        b.log('d')
        b.log('a')
        b.log('b')
        b.log('c')
        
        self.assertEqual(b.max_interval(('a','b','c'), ('c','d','a')), [])
        self.assertEqual(b.max_interval(('a','b','c'), ('a','b','c')), ['c','d'])
        self.assertEqual(b.max_interval(('b','c','c'), ('a','b','c')), ['d'])
        self.assertEqual(b.max_interval(('a','b','c'), ('d','a','b')), ['c'])
        self.assertEqual(b.max_interval(('c','c','d'), ('a','b','c')), [])
        

        with self.assertRaises(LookupError):            
            b.max_interval(('a','b','c'), ('c','d','c'))

    
    def test_07_a11(self):
        b = Bank()
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        b.log('a')
        
        self.assertEqual(b.max_interval(('a','a','a'), ('a','a','a')), list('aaaaa'))

        with self.assertRaises(LookupError):
            b.max_interval(('a','a','b'), ('a','a','a'))
                           
                           
    def test_08_complex(self):
        bank = Bank()
        
        bank = Bank()
        bank.log('c')
        bank.log('d')
        bank.log('c')
        bank.log('a') #      a
        bank.log('b') # <--- b 
        bank.log('e') #      e
        bank.log('f') #      --- f     |
        bank.log('a') #          a     |
        bank.log('f') #          f     | k
        bank.log('b') #          b     |
        bank.log('c') #          c     |
        bank.log('b') #      --- b     |
        bank.log('a') # <--- a 
        bank.log('f') #      f
        bank.log('b') #      b
        bank.log('e')
        bank.log('a')
        bank.log('b')
        bank.log('e')
        bank.log('l')
        bank.max_interval( ('a','b','e'), ('a','f','b') )

        self.assertEqual(bank.max_interval(('a','b','e'), ('a','f','b')), list('fafbcb'))
        self.assertEqual(bank.max_interval(('b','e','f'), ('b','e','l')), list('afbcbafbea'))
        self.assertEqual(bank.max_interval(('d','c','a'), ('a','b','e')), list('befafbcbafbe'))
        self.assertEqual(bank.max_interval(('a','f','b'), ('a','f','b')), list('cb'))

        with self.assertRaises(LookupError):
            bank.max_interval(('e','a','b'), ('b','c','b'))

