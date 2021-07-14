import unittest
from pyrastack_sol import *

class PyraStackTest (unittest.TestCase):

    def test_01_zero(self):
        s = PyraStack()
        s.drop(0)
        self.assertEqual(s._rows,[])

    def test_02_neg(self):
        s = PyraStack()
        with self.assertRaises(ValueError):            
            s.drop(-1)
                
    def test_03_1(self):
        s = PyraStack()    
        s.drop(1)
        self.assertEqual(s._rows,[['-']*1])
        
    def test_04_3_0(self):
        s = PyraStack()    
        s.drop(3)
        s.drop(0)        
        self.assertEqual(s._rows,[['-']*3])

    def test_05_5_2(self):
        s = PyraStack()    
        s.drop(5)
        s.drop(2)
        self.assertEqual(s._rows,[['-']*5,
                                  ['-']*2])

    def test_06_3_3(self):
        s = PyraStack()    
        s.drop(3)
        s.drop(3)
        self.assertEqual(s._rows,[['-']*3,
                                  ['-']*3])

    def test_07_3_4(self):
        s = PyraStack()    
        s.drop(3)
        s.drop(4)
        self.assertEqual(s._rows,[['-']*7])

    def test_08_8_3_4(self):
        s = PyraStack()    
        s.drop(8)
        s.drop(3)
        s.drop(4)
        self.assertEqual(s._rows,[['-']*8,
                                  ['-']*7])

    def test_09_complex(self):

        s = PyraStack()
        s.drop(10)
        """
        1234567890
        ----------
        """ 
        self.assertEqual(s._rows, [['-']*10])
        
        s.drop(7)
        """
        1234567890
        -------
        ----------
        """
        self.assertEqual(s._rows, [['-']*10,
                                   ['-']*7])
        
        s.drop(5)
        """
        1234567890
        -----
        -------
        ----------
        """
        self.assertEqual(s._rows, [['-']*10,
                                   ['-']*7,
                                   ['-']*5])
        s.drop(2)        
        """
        1234567890
        --
        -----
        -------
        ----------
        """
        self.assertEqual(s._rows, [['-']*10,
                                   ['-']*7,
                                   ['-']*5,
                                   ['-']*2,])

        s.drop(3)
        """
        1234567890
        -----
        -----
        -------
        ----------
        """
        self.assertEqual(s._rows, [['-']*10,
                                   ['-']*7,
                                   ['-']*5,
                                   ['-']*5,])

        s.drop(6)
        """
        1234567890123456
        -----
        -----
        -------
        ----------------
        """
        self.assertEqual(s._rows, [['-']*16,
                                   ['-']*7,
                                   ['-']*5,
                                   ['-']*5,])
        s.drop(6)
        """
        1234567890123456
        -----
        -----
        -------------
        ----------------
        """
        self.assertEqual(s._rows, [['-']*16,
                                   ['-']*13,
                                   ['-']*5,
                                   ['-']*5,])
        s.drop(1)
        """
        1234567890123456
        -
        -----
        -----
        -------------
        ----------------
        """
        self.assertEqual(s._rows, [['-']*16,
                                   ['-']*13,
                                   ['-']*5,
                                   ['-']*5,
                                   ['-']*1])
        s.drop(7)
        """
        1234567890123456        
        -
        -----
        ------------
        -------------
        ----------------
        """
        self.assertEqual(s._rows, [['-']*16,
                                   ['-']*13,
                                   ['-']*12,
                                   ['-']*5,
                                   ['-']*1])
