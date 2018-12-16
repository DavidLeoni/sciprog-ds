import pytest
from relmath import *

def m1():
    return Rel([[RD(1)]], ['a'], ['x'] , name='M')

def minus_m1():
    return Rel([[RD(-1)]], ['a'], ['x'] , name='M')


def m21():
    return Rel([
                [RD(7)],
                [RD(9)]
               ],
               ['a','b'], ['x'] , name='M21')

def m12():
    return Rel([
                [RD(7),RD(9)]
               ], ['x'], ['a','b'] , name='M12')


class TestRD:
    def test_eq(self):
        assert RD(1) == RD(1)

class TestRel:

    def test_dom_dim(self):
        with pytest.raises(ValueError):
            Rel([[RD(1)]], ['a','b'], ['x'])

    def test_cod_dim(self):
        with pytest.raises(ValueError):
            Rel([[RD(1)]], ['a'], ['x', 'y'])

    def test_min_dim(self):
        with pytest.raises(ValueError):
            Rel([[]], ['a'], [])

    def test_min_dim(self):
        with pytest.raises(ValueError):
            Rel([[], []], ['a','b'], [])

    def test_min_dim(self):
        with pytest.raises(ValueError):
            Rel([], [], [])

    def test_list_of_lists(self):
        with pytest.raises(ValueError):
            Rel([(RD(1),RD(2))], ['a','b'], ['x'])

        with pytest.raises(ValueError):
            Rel(([RD(1),RD(2)]), ['a','b'], ['x'])


    def test_name(self):
        assert m1().name == 'M'

    def test_eq(self):
        M1 = m1()
        assert M1 == m1()

    def test_T(self):
        M1 = m1()
        assert M1.T.g == m1().g

        M21 = m21()
        assert M21.T == m12()
        
    def test_TT(self):
        M21 = m21()
        assert M21.T.T == m21()

        M12 = m12()
        assert M12.T.T == m12()

    def test_neg(self):
        M1 = m1()
        assert -M1 == minus_m1()

    def test_neg_neg(self):
        M1 = m1()
        assert -(-M1) == m1()

        M12 = m12()
        assert -(-M12) == m12()

        M21 = m21()
        assert -(-M21) == m21()
