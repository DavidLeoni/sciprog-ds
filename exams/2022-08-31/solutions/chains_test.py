import unittest
from chains_sol import *


class TestChain(unittest.TestCase):

    def test_01_ab(self):
        self.assertEqual(chain( [
                                    ['a', 'b']
                                ]),
                                ['a', 'b'])

    def test_02_ab_c(self):
        self.assertEqual(chain( [
                                    ['ab', 'c']
                                ]),
                                ['ab', 'c'])


    def test_03_ab_c_de(self):
        self.assertEqual(chain( [
                                    ['ab', 'c', 'de']
                                ]),
                                ['ab', 'c', 'de'])

    def test_04_b_a__a_c(self):
        self.assertEqual(chain( [
                                    ['b', 'a'],
                                    ['a', 'c']
                                ]),
                                ['b', 'a', 'c'])
    
    def test_05_not_chainable(self):
        with self.assertRaises(ValueError):
            chain([
                    ['a','b'],
                    ['b','c'],
                    ['g','h']
                  ])

    def test_06_a_b_c__c_d(self):
        self.assertEqual(chain( [
                                    ['a', 'b','c'],
                                    ['c', 'd']
                                ]),
                                ['a', 'b', 'c', 'd'])

    def test_07_a_b_c__d_e_f__c_d(self):
        self.assertEqual(chain( [
                                    ['a', 'b','c'],                              
                                    ['d','e','f'],
                                    ['c', 'd'],
                                ]),
                                ['a', 'b', 'c','d','e','f'])


    def test_08_complex(self):
        self.assertEqual(chain( [
                                    ['ab', 'c', 'de'],
                                    ['gh', 'i'],
                                    ['de', 'f', 'gh']
                                    ]), 
                                    ['ab', 'c', 'de', 'f', 'gh', 'i'])
