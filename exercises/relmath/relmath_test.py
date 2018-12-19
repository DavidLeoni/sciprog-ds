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


class TestState:
    
    def test_quotes(self):
        print(S._quotes)

        with Q(S):
            print(S._quotes)
        print(S._quotes)


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

    def test_val_RD(self):
        assert Rel([[1]],['a'],['x']) == Rel([[RD(1)]],['a'],['x'])

    def test_val_BD(self):
        assert Rel([[False]],['a'],['x']) == Rel([[BD(False)]],['a'],['x'])


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

    
def pexpr(msg, expr):
    info("python:  %s" % msg)
    info('repr:    %r ' % expr) 
    info('str:\n%s' % str(expr))

M = Rel([[RD(9),RD(0), RD(6)], [RD(0),RD(5), RD(7)]], ['a','b'], ['x','y','z'] , name='M')
U = Rel([[RD(9),RD(0), RD(6)], [RD(0),RD(5), RD(7)]], ['a','b'], ['x','y','z'])

print(-Rel([[RD(1)]],['a'],['x'],name='M') == Rel([[RD(-1)]],['a'],['x'],name='M'))

pexpr('M.T', M.T)
with Q(S):
    pexpr('M.T', M.T)
pexpr('U.T', U.T)
with Q(S):
    pexpr('U.T', U.T)


pexpr('M', M)

with Q(StopAsyncIteration):
    pexpr('M.T', M.T)
pexpr('-M', -M)
with Q(S):    
    pexpr('-M', -M)

E = RelMul(M, T(M))
pexpr('M*M.T', (M*M.T))
with Q(S):
    pexpr('M*M.T', (M*M.T))

pexpr("RelMul(M, T(M))", RelMul(M, T(M)))
with Q(S):
    pexpr("RelMul(M, T(M))", RelMul(M, T(M)))

pexpr("RelMul(M, T(M)).simp()" , RelMul(M, T(M)).simp())
with Q(S):
    pexpr("RelMul(M, T(M)).simp()" , RelMul(M, T(M)).simp())

print(sjoin("ciao\npippo", "hello\ndear\nworld"))

print(sjoin("ciao\npippo", "hello\ndear\nworld\nciao\nmondo\nche\nbello", valign='center'))


with Q(S):    
    pexpr('-U' , -U)

with Q(S):    
    pexpr('U.T',  U.T)

pexpr("RelMul(M, T(M))" , RelMul(M, T(M)))

pexpr(" -Rel([[RD(1)]],['a'],['x'],name='M')",  -Rel([[RD(1)]],['a'],['x'],name='M'))

