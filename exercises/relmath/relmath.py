
from tabulate import tabulate
from wcwidth import wcswidth

from contextlib import contextmanager

class LogLevel:
    NOTHING = 0
    FATAL = 1
    ERROR = 2
    WARNING = 3
    INFO = 4
    DEBUG = 5

class S:
    _quotes = [False]
    level = 0
    
    verbosity = LogLevel.INFO

    @staticmethod
    def q():
        """ Return True if system is operating under quotation, False otherwise
        """
        return S._quotes[-1]

@contextmanager
def Q(p):
    debug('quoted')
    S._quotes.append(True)
    S.level += 2
    yield 
    S.level -= 2   
    debug('/quoted')
    S._quotes.pop()

@contextmanager
def UQ(p):
    debug('unquoted')
    S._quotes.append(False)
    S.level += 2
    yield 
    S.level -= 2   
    debug('/unquoted')
    S._quotes.pop()



def sheight(s):
    """ Return the height of provided text block.
        Min height is one.
    """
    return s.strip().count("\n") + 1

def swidth(s):
    """ Return the width of provided text block.
        Min height is one.
    """

    return max( [wcswidth(row) for row in s.strip().split('\n')] ) 


def sjoin(s1,s2, valign='top'):
    """ Horizontally joins two blocks of text possibly containing \n
        and retrun the newly formed block as a string
    """

    h1 = sheight(s1)
    h2 = sheight(s2)

    # TODO hack for one liners, prevents weird results as ['M*M.T\n  \n \n']: 
    if h1 == 1 and h2 == 1:
        return s1 + s2

    if valign == 'center' and h2 > h1:
        left_extra_rows =  (h2-h1) // 2
    else:
        left_extra_rows =  0


    rows1 = ['\n']*left_extra_rows + s1.split('\n')
    rows2 = s2.split('\n')
    ret = ""
    left_width = swidth(s1)
    for i in range(min(len(rows1), len(rows2))):
        ret += "%-*s%s\n" % (left_width,rows1[i].strip('\n'),rows2[i])

    if len(rows1) > len(rows2):
        for j in range(i+1, len(rows1)):
            ret += rows1[j] + '\n'
    else:
        for j in range(i+1, len(rows2)):
            ret += " "*left_width + rows2[j] + '\n'
    return ret

def format_log(msg=""):
    pad = " "* S.level
    return pad + str(msg).replace('\n','\n' + pad)

def fatal(msg, ex=None):
    """ Prints error and exits (halts program execution immediatly)
    """
    if S.verbosity >= LogLevel.FATAL:    

        if ex == None:
            exMsg = ""
        else:
            exMsg = " \n  " + repr(ex)
        s = format_log("\n\n    FATAL ERROR! %s%s\n\n" % (msg,exMsg))
        print(s)
    exit(1)

def log_error(msg, ex=None):
    """ Prints error but does not rethrow exception
    """
    if ex == None:
        exMsg = ""
        the_ex = Exception(msg)
    else:
        exMsg = " \n  " + repr(ex)
    the_ex = ex
    s = format_log("\n\n    ERROR! %s%s\n\n" % (msg,exMsg))
    print(s)

def error(msg, ex=None):
    """ Prints error and reraises Exception
    """
    if S.verbosity >= LogLevel.ERROR:    

        log_error(msg, ex)
        if ex != None:
            raise new_ex
        else:
            raise Exception(msg)

def warn(msg, ex=None):
    if S.verbosity >= LogLevel.WARNING:    
        if ex == None:
            exMsg = ""
        else:
            exMsg = " \n  " + repr(ex)

        s = format_log("\n\n   WARNING: %s%s\n\n" % (msg,exMsg))
        print(s)

def info(msg=""):
    if S.verbosity >= LogLevel.INFO:
        print(format_log(msg))

def debug(msg=""):
    
    if S.verbosity >= LogLevel.DEBUG:
        print(format_log("DEBUG=%s" % msg))




class Expr:
    def __init__(self, name=""):
        self._name = name

    def _reprname(self):
        """ only to be used inside repr """
        if self.name:
            return ",name='%s'" % self.name        
        else:
            return ''

    @property
    def name(self):
        return self._name

    @property
    def dom(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    @property
    def cod(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    def transpose(self):
        if S.q():
            return T(self)
        else:
            s = self.simp()
            if s == self:
                return T(self)
            else:
                return s.T

    T = property(transpose, None, None, "Matrix transposition.")

    def simp(self):
        return self

    def __eq__(self, expr2):
        return  expr2 != None \
                and self.__class__ == expr2.__class__

class BinOp(Expr):
    def __init__(self, left, right, name=''):
        super().__init__(name)
        self.left = left
        self.right = right

    def python_token(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    def python_method(self):
        raise NotImplementedError("IMPLEMENT ME!")      

    def __str__(self):
        return sjoin(str(self.left), sjoin(str(self.python_token()), str(self.right), valign='center'))

    def __repr__(self):
        
        return "%s(%s,%s%s)" % (self.__class__.__name__, repr(self.left),repr(self.right), self._reprname())


    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    def __eq__(self, binop2):
        return  super().__eq__(binop2) \
                and self.left == binop2.left \
                and self.right == binop2.right



class RelMul(BinOp):
    def __init__(self, left, right, name=''):
        super().__init__(left, right, name)
    

    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    @property
    def dom(self):
        return self.left.dom

    @property
    def cod(self):
        return self.right.cod


    def python_token(self):
        return '*'

    def python_method(self):
        return '__mul__'

    def simp(self):
        with UQ(S):
            lsimp = self.left.simp()
            rsimp = self.right.simp()
            return lsimp * rsimp

class RelAdd(BinOp):
    def __init__(self, left, right, name=''):
        super().__init__(left, right, name=name)
    

    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    @property
    def dom(self):
        return self.left.dom

    @property
    def cod(self):
        return self.right.cod

    def python_token(self):
        return '+'

    def python_method(self):
        return '__add__'

    def simp(self):
        with UQ(S):
            lsimp = self.left.simp()
            rsimp = self.right.simp()
            return lsimp + rsimp


class UnOp(Expr):
    def __init__(self, val, name=''):
        super().__init__(name=name)
        self.val = val

    def python_token(self):
        raise NotImplementedError("IMPLEMENT ME!")    


    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    

    def __str__(self):
        s = str(self.val)
        return sjoin(self.python_token(), str(self.val), valign='center')

    def __repr__(self):

        return "%s(%s%s)" % (self.__class__.__name__ , repr(self.val), self._reprname())

    def __eq__(self, unop2):
        return  super().__eq__(unop2) \
                and self.val == unop2.val


class T(UnOp):


    def python_token(self):
        raise NotImplementedError

    def python_method(self):
        return '.T'

    def __str__(self):
        return sjoin(str(self.val), self.python_method())

    @property
    def dom(self):
        return self.val.cod

    @property
    def cod(self):
        return self.val.dom
   
    def simp(self):
        with UQ(S):
            return self.val.simp().T

    def latex(self):
        raise NotImplementedError("IMPLEMENT ME!")    


class Neg(UnOp):

    def python_token(self):
        return '-'

    def python_method(self):
        return '__neg__'


    def simp(self):
        with UQ(S):
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
        super().__init__(name=name)
        self._val = val

    @property
    def val(self):
        return self._val
        
    def __eq__(self, v2):
        return  super().__eq__(v2)      \
                and self.val == v2.val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return "%s(%s%s)" % (self.__class__.__name__ , repr(self.val), self._reprname())


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
        raise NotImplementedError("Not available for this dioid !")

    def s(self):
        raise NotImplementedError("IMPLEMENT ME!")    
                
    def zero(self):
        raise NotImplementedError("IMPLEMENT ME!")    
        
    def one(self):
        raise NotImplementedError("IMPLEMENT ME!")    
        
    
class RD(Dioid):
    def __init__(self, val, name=''):
        super().__init__(val, name=name)
    
    def zero(self):
        return RD(0)
    
    def one(self):
        return RD(1)
    
    def s(self):
        return "TODO R^ set "

    def __neg__(self):
        """ NOTE: in a dioid, negation is _not_ mandatory. See page 7 of Graphs, Dioids and Semirings book
        """
        return RD(- self.val)
        
    def __add__(self, d2):
        return RD(self.val + d2.val)
    
    def __mul__(self, d2):
        return RD(self.val * d2.val)

    def __str__(self):
        cand = str(self.val)
        formatted = "%.2f" % self.val
        if len(cand) > len(formatted):
            return formatted + (' ...')
        else:
            return cand

    def __round__(self, ndigits=0):
        return RD(round(self.val, ndigits))
    
class BD(Dioid):
    def __init__(self, val, name=''):
        super().__init__(val, name=name)
    
    def zero(self):
        return BD(False)
    
    def one(self):
        return BD(True)
    
    def s(self):
        return "TODO R^ set "

    def __neg__(self):
        """ NOTE: in a dioid, negation is _not_ mandatory. See page 7 of Graphs, Dioids and Semirings book
        """
        return BD(not self.val)
        
    def __add__(self, d2):
        return BD(self.val or d2.val)
    
    def __mul__(self, d2):
        return BD(self.val and d2.val)


class Rel(Expr):
    
    def __init__(self,  g, dom, cod, name=''):
        "" 
        super().__init__(name=name)
        if type(g) is not list:
            raise ValueError("Expected a list of lists, got instead type %s" % type(g))
        if len(g) == 0:
            raise ValueError("Expected at least one row, got instead %s" % g)
        if type(g[0]) is not list:
            raise ValueError("Expected a list of lists, got instead first row type %s" % type(g[0]))
        if len(g[0]) == 0:
            raise ValueError("Expected at least one column, got instead %s" % g)
        if len(dom) != len(g):
            raise ValueError("dom has different size than g rows! dom=%s g=%s" % (len(dom), len(g)))
        if len(cod) != len(g[0]):
            raise ValueError("cod has different size than g columns! cod=%s g=%s" % (len(cod), len(g[0])))

        # fixing values

        for row in g:
            for j in range(len(row)):
                el = row[j]
                if not isinstance(el, Dioid):
                    if type(el) == float or type(el) == int:
                        row[j] = RD(el)
                    elif type(el) == bool:
                        row[j] = BD(el)
                    else:
                        raise ValueError("Found unrecognized type %s for element %s" % (type(el), el))            

        self.g = g
        self._dom = dom
        self._cod = cod        
    
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


    def map(self, f):
        """ Maps f to all elements of the matrix
        """
        res_g = []
        for row in self.g:
            new_row = []
            res_g.append(new_row)
            for x in row:
                new_row.append(f(x))
        return Rel(res_g, self.dom, self.cod, name=self.name)

    def __round__(self, ndigits=0):
        if not isinstance(self.dioid(), RD):
            raise ValueError("Unsupported dioid for round function: %s" % type(self.dioid()))
        
        return self.map(lambda x: round(x, ndigits))
        

    def __add__(self, r2):
        if S.q():
            return RelAdd(self, r2)
        else:

            res_g = []
            for i in range(len(self.dom)):
                row = []
                res_g.append(row)
                for j in range(len(self.cod)):
                    row.append(self.g[i][j] + r2.g[i][j])
            return Rel(res_g, self.dom, self.cod, name=self.name)
                
    def __mul__(self, r2):
        """ we don't consider __matmul__ for now (dont like the '@')
        """
        if r2 == None:
            raise ValueError("Can't multiply by None !")
        if S.q():
            return RelMul(self, r2)
        else:
            res_g = []
            
            for i in range(len(self.dom)):
                row = []
                res_g.append(row)
                for j in range(len(r2.cod)):
                    val = self.dioid().zero()
                    for k in range(len(self.cod)):
                        val += self.g[i][k] * r2.g[k][j]
                    row.append(val)
            return Rel(res_g, self.dom, r2.cod, name=self.name)

    def __str__(self):
        if S.q() and self.name:
            return self.name
        else:
            
            data = []
            header = [" "]
            header.extend(self.cod)
            data.append(header)
            for i in range(len(self.g)):
                row = [self.dom[i]]
                row.extend(self.g[i])
                data.append(row)
            """
            table = DoubleTable(data)
            if self.name:
                table.title = self.name
            return table.table
            """
            return tabulate(data, tablefmt="fancy_grid")
            
    def __repr__(self):
        return "Rel(%s,%s,%s%s)" % (repr(self.g), repr(self.dom), repr(self.cod) , self._reprname())
    
    def transpose(self):
        if S.q():
            return T(self)
        else:
            res_g = []
            for i in range(len(self.cod)):
                row = []
                res_g.append(row)
                for j in range(len(self.dom)):
                    row.append(self.g[j][i])

            return Rel(res_g, self.cod, self.dom, name=self.name)
    T = property(transpose, None, None, "Matrix transposition.")
    
    def __neg__(self):
        if S.q():
            return Neg(self)
        else:
            res_g = []
            for i in range(len(self.dom)):
                row = []
                res_g.append(row)
                for j in range(len(self.cod)):
                    row.append(-self.g[i][j])

            return Rel(res_g, self.dom, self.cod, name=self.name)

