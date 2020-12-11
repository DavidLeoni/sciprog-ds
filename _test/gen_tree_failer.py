
"""
Test suite to fail all tree tests, so we see what happens when students make something wrong.

David Leoni - December 2018
"""


import sys
sys.path.append('trees/')

import unittest

from gen_tree_test import gt
from gen_tree_test import GenericTreeTest
from gen_tree_sol import GenericTree

class TreeFailTest(GenericTreeTest):

    def test_01_both_none(self):
        self.assertTreeEqual(None, None)
    
    def test_02_none_left(self):
        self.assertTreeEqual(None, gt('b'))

    def test_03_none_right(self):
        self.assertTreeEqual(gt('b'), None)
    
    def test_04_wrongClass(self):
        self.assertTreeEqual('hello', gt('a'))
    
    def test_05_data(self):
        self.assertTreeEqual(gt('a'), gt('b'))
        
    def test_06_length_left(self):
        self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b'), gt('c')))
                             
    def test_07_length_right(self):
        self.assertTreeEqual(gt('a', gt('b'), gt('c')), gt('a', gt('b')))

    def test_08_big_tree(self):
        self.assertTreeEqual(gt('b', gt('hellooooooooooo', gt('d'), gt('e'))), gt('b', gt('e')))

    def test_09_number_tree(self):
        self.assertTreeEqual(gt(2, gt(3232323123123123, gt(3), gt(1))), gt(2, gt(1)))

    def test_10_mixed_tree(self):
        self.assertTreeEqual(gt(2, gt('hellllloooooooooooooo', gt(1234), gt(None))), gt('a', gt(1)))
        
    def test_11_bad_parent(self):
        tb = GenericTree('b')
        ta = GenericTree('a')
        ta.insert_child(tb)
        tb._parent = None
        self.assertTreeEqual(gt('a', gt('b')), ta)

    def test_12_wrong_datatype_child(self):
        ta = gt('a')
        ta._child = 666
                        
        self.assertTreeEqual(ta, gt('a', gt('b')))
                
    def test_13_wrong_datatype_sibling(self):
        tb = gt('b')
        ta = gt('a', tb)
        tb._sibling = 666
                        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('c')))


    def test_14_wrong_datatype_parent(self):
        tb = gt('b')
        ta = gt('a', tb)
        tb._parent = 666
                        
        self.assertTreeEqual(ta, gt('a', gt('b')))
                             