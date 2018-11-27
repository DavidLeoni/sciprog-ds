
class Expr:
    def __init__(self):
        ""

    @property
    def dom(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    @property
    def cod(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    def simp(self):
        return self

class BinOp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def python_token(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    def python_method(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    def __str__(self):
        return "%s%s%s" % (str(self.left), self.python_token(), str(self.right))

    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    
class RelMul(BinOp):
    def __init__(self, left, right):
        super().__init__(left, right)
    
    def python_token(self):
        return '*'

    def python_method(self):
        return '__mul__'

    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    @property
    def dom(self):
        return self.left.dom

    @property
    def cod(self):
        return self.right.cod
   
    def simp(self):
        lsimp = self.left.simp()
        rsimp = self.right.simp()
        return lsimp * rsimp

class UnOp(Expr):
    def __init__(self, val):
        self.val = val

    def python_token(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    def __str__(self):
        raise NotImplementedError("IMPLEMENT ME!")    


    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    


class T(UnOp):


    def python_token(self):
        raise NotImplementedError

    def python_method(self):
        return '.T'

    def __str__(self):
        return "%s%s" % (self.val, self.python_method())

    @property
    def dom(self):
        return self.val.cod

    @property
    def cod(self):
        return self.val.dom
   
    def simp(self):
        return self.val.T

    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    


class Neg(UnOp):

    def python_token(self):
        return '-'

    def python_method(self):
        return '__neg__'

    def __str__(self):
        return "%s%s" % (self.python_token(), self.val)

    def simp(self):
        return -self.val

    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    @property
    def dom(self):
        return self.val.dom

    @property
    def cod(self):
        return self.val.cod

class Val(Expr):
    def __init__(self, val,name=''):
        ""
        self.val=val
        self.name = name


class Dioid(Val):
    def __init__(self, val, name=''):
        ""        
        super().__init__(val, name=name)
        
    def __add__(self, d2):
        raise NotImplementedError("IMPLEMENT ME!")
    
    def __mul__(self, d2):
        raise NotImplementedError("IMPLEMENT ME!")    

    def __neg__(self):
        """ NOTE: in a dioid, negation is _not_ mandatory. See page 7 of Graphs, Dioids and Semirings book
        """
        raise NotImplemented("Not available for this dioid !")

    def s(self):
        raise NotImplementedError("IMPLEMENT ME!")    
                
    def zero(self):
        raise NotImplementedError("IMPLEMENT ME!")    
        
    def one(self):
        raise NotImplementedError("IMPLEMENT ME!")    
        
    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()    
    


class RD(Dioid):
    def __init__(self, val, name=''):
        super().__init__(val, name=name)
    
    def zero(self):
        return 0
    
    def one(self):
        return 1
    
    def s(self):
        return "TODO R^ set "

    def __neg__(self):
        """ NOTE: in a dioid, negation is _not_ mandatory. See page 7 of Graphs, Dioids and Semirings book
        """
        return - self.val
        
    def __add__(self, d2):
        return self.val + d2.val
    
    def __mul__(self, d2):
        return self.val * d2.val

class Rel(Val):
    
    def __init__(self,  g, dom, cod, name=''):
        "" 
        self.g = g
        self._dom = dom
        self._cod = cod
        super().__init__(self, name=name)
    
    @property
    def dom(self):
        return self._dom

    @property
    def cod(self):
        return self._cod

    def nodes(self):
        """ Ordered list of unique nodes. First dom, then cod
        """
        inter = set(self.dom).intersection(self.cod)
        if len(inter) > 0:
            return [x for x in self.dom if x not in inter] + self.cod
        else:
            return self.dom + self.cod

    def dioid(self):
        """ TODO assumes graph has at least one element
        """
        return self.g[0][0]

    def __add__(self, r2):
        res_g = []
        for i in range(len(self.dom)):
            row = []
            res_g.append(row)
            for j in range(len(self.cod)):
                row.append(self.g[i][j] + r2.g[i][j])
        return Rel(res_g, self.dom, self.cod)
                
    def __mul__(self, r2):
        """ we don't consider __matmul__ for now (dont like the '@')
        """
        res_g = []
        
        for i in range(len(self.dom)):
            row = []
            res_g.append(row)
            for j in range(len(r2.cod)):
                val = self.dioid().zero()
                for k in range(len(self.cod)):
                    val = self.g[i][k] * r2.g[k][j]
                row.append(val)
        return Rel(res_g, self.dom, r2.cod)

    def __str__(self):
        return str(self.g)

    
    def transpose(self):
        res_g = []
        for i in range(len(self.cod)):
            row = []
            res_g.append(row)
            for j in range(len(self.dom)):
                row.append(self.g[j][i])

        return Rel(res_g, self.cod, self.dom)

    T = property(transpose, None, None, "Matrix transposition.")

    def __neg__(self):
        res_g = []
        for i in range(len(self.dom)):
            row = []
            res_g.append(row)
            for j in range(len(self.cod)):
                row.append(-self.g[i][j])

        return Rel(res_g, self.cod, self.dom)


    
M = Rel([[RD(9),RD(0), RD(6)], [RD(0),RD(5), RD(7)]], ['a','b'], ['x','y','z'] )


print('M = \n%s' % M)
print('M.T = \n%s' % M.T)
print('-M = \n%s' % -M)

E = RelMul(M, T(M))
print('M*M.T=\n%s' % (M*M.T))
print("RelMul(M, T(M))\n%s" % RelMul(M, T(M)))
print("RelMul(M, T(M)).simp()\n%s" % RelMul(M, T(M)).simp())

