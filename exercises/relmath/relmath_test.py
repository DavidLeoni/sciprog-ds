import pytest
from relmath import *

def m1():
    return Rel([[RD(1)]], ['a'], ['x'] , name='M')

class TestRD:
    def test_eq(self):
        assert RD(1) == RD(1)

class TestRel:

    def test_name(self):
        M = m1()
        assert M.name == 'M'

    def test_eq(self):
        M = m1()
        assert M == m1()

    def test_transpose(self):
        M = m1()
        assert M.T == m1()
