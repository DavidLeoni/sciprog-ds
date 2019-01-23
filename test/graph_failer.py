
"""
Test suite to fail all graph tests, so we see what happens when students make something wrong.

David Leoni - December 2018
"""


import sys
sys.path.append('../exercises/graph-algos/')

import unittest

from graph_test import dig
from graph_test import udig
from graph_test import DiGraphTest


class DiGraphFailTest(DiGraphTest):

    def test_01_both_none(self):
        self.assertDiGraphEqual(None, None)
    
    def test_02_none_left(self):
        self.assertDiGraphEqual(None, dig({'a':[]}))

    def test_03_none_right(self):
        self.assertDiGraphEqual(dig({'a':[]}), None)
    
    def test_04_wrongClass(self):
        self.assertDiGraphEqual('hello', dig({'a':[]}))
    
    def test_05_data(self):
        self.assertDiGraphEqual(dig({'a':[]}), dig({'b':[]}))

    def test_06_big_graph(self):
        self.assertDiGraphEqual(dig({'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa':['bbbbbbb','cccccccc'],
                                  'bbbbbbb':['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']}), dig({'a':[]}))

    def test_07_number_graph(self):
        self.assertDiGraphEqual(dig({4321341234:[3112,879234798272934789723984],
                                  3112:[4321341234]}), dig({66666:[3112]}))

    def test_08_mixed_graph(self):
        ""
        self.assertDiGraphEqual(dig({'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa':[3112,'cccccccc'],
                                      3112:['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']}), dig({66666:[3112]}))
        