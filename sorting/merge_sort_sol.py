
import itertools

def merge1(a,b):
    """ Takes a and b as two ordered lists (from smallest to greatest) of (possibly negative) integers.
        Lists are of size n and m respectively 
       
        RETURN  a NEW list composed of the items in A and B ordered
        from smallest to greatest
       
       - MUST RUN IN O(m+n)
       - use .pop() on input lists to reduce their size and put _maximal_ elements in tmp
          
    """
    #jupman-raise
    
    ret = []
    
    while len(a) > 0 or len(b) > 0:
        
        if len(a) > 0 and len(b) > 0:
            if a[-1] > b[-1]:
                ret.append(a.pop())
            else:
                ret.append(b.pop())
        elif len(a) > 0:
            ret.append(a.pop())
        else:
            ret.append(b.pop())
            
    ret.reverse()
    return ret
    #/jupman-raise

def merge2(A,B):
    """ Takes A and B as two ordered lists (from smallest to greatest) of (possibly negative) integers.
        Lists are of size n and m respectively 
       
        RETURN  a NEW list composed of the items in A and B ordered
        from smallest to greatest
       
       - MUST RUN IN O(m+n)
       - in this version, do NOT use .pop() on input lists to reduce their size.
         Instead, use indeces to track at which point you are, starting at zero and 
         putting _minimal_ elements in tmp
             
    """
    #jupman-raise
    i = 0
    j = 0
    res = []
    while i + j < len(A) + len(B):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        elif i < len(A):
            res.extend(itertools.islice(A,i, None))
            return res
        else:
            res.extend(itertools.islice(B,j, None))
            return res
    return res
    #/jupman-raise

