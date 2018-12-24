import pytest
from relmath import *

def m0():
    return Rel([[RD(0)]], ['a'], ['x'] , name='M')


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

    def test_min_dim_1(self):
        with pytest.raises(ValueError):
            Rel([[]], ['a'], [])

    def test_min_dim_2(self):
        with pytest.raises(ValueError):
            Rel([[], []], ['a','b'], [])

    def test_min_dim_3(self):
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


    def test_neg(self):
        M1 = m1()
        assert -M1 == minus_m1()

    def test_neg_neg(self):
        M1 = m1()
        assert - (-M1) == m1()

        M12 = m12()
        assert -(-M12) == m12()

        M21 = m21()
        assert -(-M21) == m21()

class TestTranspose:
    def test_T(self):
        M1 = m1()
        M1.T
        assert M1.T.g == m1().g

        M21 = m21()
        assert M21.T == m12()

    def test_simp_T(self):
        M1 = m1()
        with Q(S):
            M1T = M1.T
        assert M1T.simp().g == m1().g

        M21 = m21()
        with Q(S):
            M21T = M21.T 
        assert M21T.simp() == m12()


    def test_TT(self):
        M21 = m21()
        assert M21.T.T == m21()

        M12 = m12()
        assert M12.T.T == m12()

    def test_simp_TT(self):
        M21 = m21()
        with Q(S):
            M21TT = M21.T.T
        assert M21TT.simp() == m21()

        M12 = m12()
        with Q(S):
            M12TT = M12.T.T
        assert M12TT.simp() == m12()


class TestMul:

    def test_id(self):
        M1 = m1()
        M1p = m1()
        M1r = m1()
        assert round(M1 * M1p, 7) == round(M1r, 7)

    def test_zero_10(self):
        M1 = m1()
        M0 = m0()
        Mr = m0()
        assert round(M1 * M0, 7) == round(Mr, 7)
    def test_zero_01(self):
        
        M1 = m1()
        M0 = m0()
        Mr = m0()
        assert round(M0 * M1, 7) == round(Mr, 7)

    def test_m21_id(self):
        
        M12 = m21()
        M1 = m1()
        Mr = m21()
        assert round(M12 * M1, 7) == round(Mr, 7)

    def test_m12_m21(self):
        
        M12 = m12()
        M21 = m21()
        Mr = Rel([[M12.g[0][0]*M21.g[0][0]+ M12.g[0][1]*M21.g[1][0] ]],M12.dom, M21.cod)
        assert round(M12 * M21, 7) == round(Mr, 7)


def pexpr(msg, expr):
    info("python:  %s" % msg)
    info('repr:    %r ' % expr) 
    info('str:\n%s' % str(expr))

def test_trial():
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

    with Q(S):
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
