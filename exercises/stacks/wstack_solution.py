import math
        
class WStack:
    """ A simple stack made only of integer numbers. 
        Can provide quickly the total sum of such numbers with .weight method
    """
    def __init__(self):
        """ Creates a WStack which contains only integers
    
        """
        self._elements = []         
        #jupman-raise
        self._weight = 0
        #/jupman-raise

    def weight(self):
        """ RETURN the total weight of the stack

            - MUST run in O(1)
        """
        #jupman-raise
        return self._weight
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
        
                WStack: weight=7 elements=['5', '2']
        """

        #jupman-raise
        return "WStack: weight=%s elements=%s" % (str(self._weight), str(self._elements))
        #/jupman-raise


    def is_empty(self):
        """ RETURN True if the stack empty, False otherwise

            - Must run in O(1)
        """
        #jupman-raise
        return len(self._elements) == 0
        #/jupman-raise


    def push(self, new_item):
        """ Adds new_item to the top of the stack                        
            
            - Must run in O(1)
            - if item is not an int, raises ValueError
        """        
        #jupman-raise
        
        if type(new_item) != int:
            raise ValueError("Expected an int, found instead %s" % type(new_item))
        self._elements.append(new_item)
        self._weight += new_item
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
            self._weight -= self._elements[-1]
            return self._elements.pop()                
        #/jupman-raise



def accumulate(stack1, stack2, min_amount):
    """ Pushes on stack2 elements taken from stack1 until the weight of
        stack2 is equal or exceeds the given min_amount

        - if the given min_amount cannot possibly be reached because 
          stack1 has not enough weight, raises early ValueError without 
          changing stack1.
        - DO NOT access internal fields of stacks, only use class methods.
        - MUST perform in O(n) where n is the size of stack1
        - NOTE: this function is defined *outside* the class !
    """
    #jupman-raise
    if stack1.weight() + stack2.weight() < min_amount:
        raise ValueError("Cannot reach %s amount" % min_amount)

    while stack2.weight() < min_amount and not stack1.is_empty():
        el = stack1.pop()
        stack2.push(el)
    #/jupman-raise
    


