from sympy import *
from sympy.core.singleton import S
from sympy.core.decorators import call_highest_priority
from sympy.core.decorators import _sympifyit


init_printing(use_unicode=True)
        
class Dioid(Expr):
    
    is_number = True
    is_commutative = True

    @cacheit
    def __new__(cls,*args):
        tmp = []
        for a in args:
            a = sympify(a,strict=True)
            if type(a) is cls:
                tmp.extend(a.args)
            else:
                tmp.append(a)
        return super().__new__(cls,*tmp)    
        
    def __mul__(self, other):
        return self._eval_mul(other)
    
    #@decorators._sympifyit('other', NotImplemented)    
    #@call_highest_priority('__radd__')
    def __add__(self, other):
        return self._eval_add(other)

    def __neg__(self):
        return self._eval_neg()

    def s(self):
        """ The set of discourse """
        raise NotImplementedError("IMPLEMENT ME!")    
                
    def zero(self):
        raise NotImplementedError("IMPLEMENT ME!")    
        
    def one(self):
        raise NotImplementedError("IMPLEMENT ME!")    
        
    def __str__(self):
        
        return "%s(%s)" % (self.__class__.__name__, str(self.args[0]))
    
    def __repr__(self):
        return self.__str__()    

    def _eval_neg(self, other):
        """ NOTE: in a dioid, negation is _not_ mandatory. See page 7 of Graphs, Dioids and Semirings book
        """
        raise NotImplemented("Not available for this dioid !")
        
        raise NotImplementedError("")
        
    def _eval_add(self, other):
        raise NotImplementedError("")
    
    def _eval_mul(self, other):
        raise NotImplementedError("")

    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__add__')
    def __radd__(self, a):
        """Implementation of reverse add method."""
        return a.__add__(self)       
    
    def __rmul__(self, a):
        """Implementation of reverse mul method."""
        return a.__mul__(self)       
  
class RD(Dioid):
    def __init__(self, val):
        self.val = sympify(val)
        super().__init__()
    
    def zero(self):
        return S(0)
    
    def one(self):
        return S(1)
    
    def s(self):
        return "TODO R^ set "

    def _eval_neg(self):
        """ NOTE: in a dioid, negation is _not_ mandatory. See page 7 of Graphs, Dioids and Semirings book
        """
        return self.__class__(- self.args[0])
        
    def _eval_add(self, d2):
        
        if isinstance(d2,int) or isinstance(d2,float):
            return self.__class__(self.args[0] * d2)
        elif isinstance(d2, RD):
            return self.__class__(self.args[0] + d2.args[0])
        else:
            return NotImplemented
        
    def _eval_mul(self, d2):
        if isinstance(d2,int) or isinstance(d2,float):
            return self.__class__(self.args[0] * d2)
        elif isinstance(d2, RD):
            return self.__class__(self.args[0] * d2.args[0])
        else:
            return NotImplemented

    #@classmethod
    #def eval(cls, arg):
        # Phi(x) + Phi(-x) == 1
        #if arg.could_extract_minus_sign():
        #    return 1-cls(-arg)
        
class Rel(ImmutableMatrix):
    def __init__(self, par, dom=[], cod=[]):
        super().__init__()
        self.dom=dom
        self.cod=cod
                
    def _eval_matrix_mul(self, other):
        r = super()._eval_matrix_mul(other)
        r.dom = self.dom
        r.cod = other.cod
        return r
    
    def _eval_transpose(self):
        r = super()._eval_transpose()
        r.dom = self.cod
        r.cod = self.dom
        return r
    
    def __str__(self):
        r = super().__str__()
        if r.startswith("Matrix"):
            return self.__class__.__name__ + r[len("Matrix"):]
        else:
            return "Rel(...)"

    T = property(transpose, None, None, "Matrix transposition.")

a = ImmutableMatrix(['x'])
b = ImmutableMatrix(['x'])
expr = Add(a, b)
simplify(expr)


a = Integer(3)
b = Integer(5)
expr = Add(a, b)
simplify(expr)

a = RD(3)
b = RD(5)
expr = Mul(a, b)
print(expr.doit())
s = simplify(expr)


a = RD(3)
b = RD(5)
expr = Add(a, b)
simplify(expr)

w = Rel([[RD(2),RD(5)]], dom=['a','b'], cod=['x','y','z'])
expr = w*w.T

print(type(expr))
print(expr)
