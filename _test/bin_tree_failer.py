
"""
Test suite to fail all tree tests, so we see what happens when students make something wrong.

David Leoni - December 2018
"""

import sys
sys.path.append('trees')

import unittest

from bin_tree_test import bt
from bin_tree_test import BinaryTreeTest


class BinaryTreeFailTest(BinaryTreeTest):

    def test_01_both_none(self):
        self.assertTreeEqual(None, None)
    
    def test_02_none_left(self):
        self.assertTreeEqual(None, bt('b', None, None))

    def test_03_none_right(self):
        self.assertTreeEqual(bt('b', None, None), None)
    
    def test_04_wrongClass(self):
        self.assertTreeEqual('hello', bt('a', None, None))
    
    def test_05_data(self):
        self.assertTreeEqual(bt('a',None,None), bt('b',None,None))
        
    def test_06_different_length_left(self):
        self.assertTreeEqual(bt('a',bt('b'),bt('c')), bt('a',bt('b')))


    def test_07_different_length_right(self):
        self.assertTreeEqual(bt('a',bt('b')), bt('a',bt('b'), bt('c')))


    def test_08_big_tree(self):
        self.assertTreeEqual(bt('b', bt('hellooooooooooo', bt('d'), bt('e')),None), bt('b', bt('e'),None))

    def test_09_number_tree(self):
        self.assertTreeEqual(bt(2, bt(3232323123123123, bt(3), bt(1)),None), bt(2, bt(1),None))

    def test_10_mixed_tree(self):
        self.assertTreeEqual(bt(2, bt('hellllloooooooooooooo', bt(1234,None,None), bt(None,None,None))), bt('a', bt(1,None,None),None))
        
    def test_11_wrong_datatype_left(self):
        ta = bt('a')
        ta._left = 666
                        
        self.assertTreeEqual(ta, bt('a', bt('b')))
        
        
    def test_12_wrong_datatype_right(self):
        ta = bt('a')
        ta._right = 666
                        
        self.assertTreeEqual(ta, bt('a', None, bt('b')))


    def test_13_wrong_datatype_both(self):
        ta = bt('a')
        ta._left = 666
        ta._right = 666
                        
        self.assertTreeEqual(ta, bt('a', bt('b'), bt('c')))
        
    def test_14_data_datatype_root(self):
        ta = bt('666')
                                
        self.assertTreeEqual(ta, bt(666))
        
    def test_15_data_datatype_root_None(self):
        ta = bt(None)
                                
        self.assertTreeEqual(ta, bt('None'))            
        
    def test_16_data_datatype_left(self):
        ta = bt('a',
                     bt('666'))
                                
        self.assertTreeEqual(ta, bt('a', 
                                        bt(666)))
        
    def test_17_data_datatype_right(self):
        ta = bt('a',
                     None,
                     bt('666'))
                                
        self.assertTreeEqual(ta, bt('a', 
                                        None,
                                        bt(666)))
        
    def test_18_data_datatype_both(self):
        ta = bt('a',
                     bt('666'),
                     bt('666'))
                                
        self.assertTreeEqual(ta, bt('a', 
                                        bt(666),
                                        bt(666)))        