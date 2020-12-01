
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

    def test_06_big_tree(self):
        self.assertTreeEqual(bt('b', bt('hellooooooooooo', bt('d'), bt('e')),None), bt('b', bt('e'),None))

    def test_07_number_tree(self):
        self.assertTreeEqual(bt(2, bt(3232323123123123, bt(3), bt(1)),None), bt(2, bt(1),None))

    def test_08_mixed_tree(self):
        self.assertTreeEqual(bt(2, bt('hellllloooooooooooooo', bt(1234,None,None), bt(None,None,None))), bt('a', bt(1,None,None),None))
        