class SortedStack:
    """ A stack that only accepts integers, which must be pushed already sorted in 
        either ascending or descending order.
    """

    def __init__(self, ascending):
        """ Creates a SortedStack. Expects a boolean value to determine in which 
            sorting order the integers are going to be pushed. 
        
        Example:
        
        Ascending:       Descending
           
           8                 3
           5                 5
           3                 8
        
        """        
        self._elements = []
        self._ascending = ascending
        
    def size(self):
        return len(self._elements)
        
    def is_empty(self):
        return len(self._elements) == 0

    def peek(self):
        """
            Returns the first element in the stack, without modifying the stack.        
        
            If stack is empty, raises an IndexError.
        """        
        
        if (self.is_empty()):
            raise IndexError("Stack is empty!")            
        else:
            return self._elements[-1]


    def pop(self):
        """ Removes the element at the top of the stack and returns it.
            
            If the stack is empty, raises an IndexError
        """
        if (self.is_empty()):
            raise IndexError("Stack is empty!")
              
        return self._elements.pop()                
        
    def push(self, item):        
        """ Inserts an integer item in the stack
            
            If item is not an integer, or does not respect sorting order, raises a ValueError
        """
        
        if (type(item) is not int):
            raise ValueError("Invalid object! Expected an integer, found instead "  
            + str(item) + " of type " + str(type(item)))
       
        if len(self._elements) > 0:
            if self._ascending:
                if item < self._elements[-1]:
                    raise ValueError("Invalid object! Stack is with ascending order, but received number "
                    + str(item) + " which is less than last number: " + str(self._elements[-1])) 
            else:
                if item > self._elements[-1]:
                    raise ValueError("Invalid object! Stack is with descending order, but received number "  
                    + str(item) + " which is greater than last number: " + str(self._elements[-1]))         
        
        self._elements.append(item)
            
    def __str__(self):
        if    self._ascending :    
            asc = 'ascending'
        else:
            asc = 'descending'
        return "SortedStack (" + asc + "):  " + " elements=" + str(self._elements) 

    def ascending(self):
        """ Returns true if stack is ascending, false otherwise. """
        
        return self._ascending

def transfer(s):
    """ Takes as input a SortedStack s (either ascending or descending) and 
        returns a new SortedStack with the same elements of s, but in reverse order. 
        At the end of the call s will be empty.
        
        Example:
        
            s       result
            
            2         5
            3         3
            5         2
    """
    #jupman-raise
    ret = SortedStack(not s.ascending())
    
    while s.size() > 0:
        num = s.pop()
        ret.push(num)
            
    return ret
    #/jupman-raise

def merge(s1,s2):
    """ Takes as input two SortedStacks having both ascending order, 
       and returns a new SortedStack sorted in descending order, which will be the sorted merge 
       of the two input stacks. MUST run in O(n1 + n2) time, where n1 and n2 are s1 and s2 sizes.
       
       If input stacks are not both ascending, raises ValueError.
       At the end of the call the input stacks will be empty.       
       
       Example:
       
       s1 (asc)   s2 (asc)      result (desc)
       
          5          7             2
          4          3             3
          2                        4
                                   5
                                   7
    
    """       
    #jupman-raise
    if not (s1.ascending() and s2.ascending()):
        raise ValueError("Input stacks must be either both ascending! "
                         + "Found instead: s1: " + str(s1.ascending) + " and s2: " + str(s2.ascending) )

    ret = SortedStack(False)

    while s1.size() > 0 or s2.size() > 0:
        
        if s1.size() > 0:
            if s2.size() > 0:
                if s1.peek() > s2.peek():
                    e = s1.pop()
                else:
                    e = s2.pop()           
            else:
                e = s1.pop()
        else:
            e = s2.pop()
                
        ret.push(e)                         

    return ret    
    #/jupman-raise
