       
class CappedStack:
    
    def __init__(self, cap):
        """ Creates a CappedStack capped at provided cap. 
        
            - if cap <= 0, throws a ValueError
        """
        #jupman-raise
        if cap <= 0:
            raise ValueError("Cap must be positive, found instead: %s" % cap)
        # notice we assign to variables with underscore to respect Python conventions        
        self._cap = cap
        # notice with use _elements instead of the A in the pseudocode, because it is
        # clearer, starts with underscore, and capital letters are usual reserved 
        # for classes or constants
        self._elements = []         
        #/jupman-raise

    def cap(self):
        """ RETURN the cap of the stack 

            - Must run in O(1)
        """
        #jupman-raise
        return self._cap
        #/jupman-raise

    def size(self):
        """ RETURN the size of the stack

            - Must run in O(1)
        """
        #jupman-raise
        return len(self._elements)
        #/jupman-raise
    
    def __str__(self):
        """ Return a string like  
        
                CappedStack: cap=4 elements=['a', 'b']
        """

        #jupman-raise
        return "CappedStack: cap=%s elements=%s" % (str(self._cap), str(self._elements))
        #/jupman-raise


    def is_empty(self):
        """ RETURN True if the stack empty, False otherwise

            - Must run in O(1)
        """
        #jupman-raise
        return len(self._elements) == 0
        #/jupman-raise


    def push(self, new_item):
        """ Adds item to the top of the stack, if current size is within cap.
            
            If stack size is already at cap value, new item is silently discarded
            
            - Must run in O(1)
        """        
        #jupman-raise
        if (len(self._elements) < self._cap):
            self._elements.append(new_item)
        # else fail silently
        #/jupman-raise

    def peek(self):
        """ RETURN the top element in the stack (without removing it!)
            
            - if stack is empty, raise IndexError
            - Must run in O(1)  

        """
        #jupman-raise
        if len(self._elements) == 0:
            raise IndexError("Empty stack !")
        
        return self._elements[-1]
        #/jupman-raise

    def pop(self):
        """ Removes the top element in the stack and RETURN it.

            - if stack is empty, raise IndexError
            - Must run in O(1)
        """
        #jupman-raise
        if len(self._elements) == 0:
            raise IndexError("Empty stack !")
        else:
            return self._elements.pop()                
        #/jupman-raise


    def peekn(self, n):
        """
            RETURN a list with the n top elements, in the order in which they
            were pushed. For example, if the stack is the following: 
            
                e
                d
                c
                b
                a
                
            peekn(3) will return the list ['c','d','e']
            If there aren't enough element to peek, raises IndexError
            If n is negative, raises an IndexError
        """
        #jupman-raise
        if n < 0:
            raise IndexError("Negative n! " + str(n))
        
        if (len(self._elements) >= n):
            i = self.size() - n 
            ret = self._elements[i:]            
            return ret
        else:
            raise IndexError("Requested to peek " + str(n) + " elements, but "
                             + " there are only " + str(self.size()) + " in the stack! ")
        #/jupman-raise

    def popn(self, n):
        """ Pops the top n elements, and RETURN them as a list, in the order in 
            which they where pushed. For example, with the following stack:
            
                e
                d
                c
                b
                a
            
            popn(3)
            
            will give back ['c','d','e'], and stack will become:
            
                b
                a
            
            If there aren't enough element to pop, raises an IndexError
            If n is negative, raises an IndexError
        """
        #jupman-raise
        if n < 0:
            raise IndexError("Negative n! " + str(n))
                             
        if (len(self._elements) >= n):
            i = self.size() - n 
            ret = self._elements[i:]
            self._elements = self._elements[:i]
            return ret
        else:
            raise IndexError("Requested to pop " + str(n) + " elements, but "
                             + " there are only " + str(self.size()) + " in the stack! ")
        #/jupman-raise

    def set_cap(self, cap):
        """ MODIFIES the cap setting its value to the provided cap. 
        
            If the cap is less then the stack size, all the elements above 
            the cap are removed from the stack.
            
            If cap < 1, raises an IndexError
            Does *not* return anything!
        
            For example, with the following stack, and cap at position 7:
            
            cap ->  7
                    6
                    5  e
                    4  d
                    3  c
                    2  b
                    1  a
                    
            
            calling method set_cap(3) will change the stack to this:
            
            cap ->  3  c
                    2  b
                    1  a                                
            
        """
        #jupman-raise
        if cap < 1:
            raise IndexError("Invalid cap: " + str(cap))
        
        if cap < self.size():            
            self.popn(self.size() - cap)
        
        self._cap = cap
        #/jupman-raise
        
