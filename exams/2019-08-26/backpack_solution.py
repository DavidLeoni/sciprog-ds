DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", str(msg).replace('\n', '\n' + (' '*8)))

class Backpack:
    
    def __init__(self, max_weight):
        """ Creates a Backpack with given max_weight.

            - if max_weight is negative, raises ValueError
        """
        if max_weight < 0:
            raise ValueError("Expected a non-zero weight, got instead: %s "  % max_weight)
        self._elements = []
        self._max_weight = max_weight
        #jupman-raise
        self._weight = 0
        #/jupman-raise

    def size(self):
        """ RETURN the number of items in the backpack

            - MUST run in O(1)
        """
        #jupman-raise
        return len(self._elements)
        #/jupman-raise
    
    def max_weight(self):
        """ Return the maximum allowed weight
        """
        return self._max_weight

    def weight(self):
        """  Return the backpack total current weight

             ************  MUST RUN IN O(1)  ***************
        """
        #jupman-raise
        return self._weight
        #/jupman-raise

    def is_empty(self):
        """ RETURN True if the backpack empty, False otherwise

            - MUST run in O(1)
        """
        #jupman-raise
        return len(self._elements) == 0
        #/jupman-raise

    def __str__(self):
        """ Return a string like  
        
                Backpack: weight=8 max_weight=10 elements=[('a',5), ('b',3)]
        """
        #jupman-raise
        return "Backpack: weight=%s max_weight=%s\n          elements=%s" % (self._weight, self._max_weight,self._elements)
        #/jupman-raise


    def peek(self):
        """ RETURN the top element in the stack (without removing it!)
            
            - if stack is empty, raise IndexError
            - Must run in O(1)  

        """
        #jupman-raise
        if len(self._elements) == 0:
            raise IndexError("Empty backpack !")
        
        return self._elements[-1]
        #/jupman-raise


    def push(self, item, w):
        """ Adds item of weight w on the top of the backpack.
            
            - if w is negative, raises ValueError
            - if w is heavier than topmost item, raises ValueError
            - if max_weight is exceeded, raises ValueError
            - MUST run in O(1)
            
        """
        #jupman-raise                        
        debug("Pushing (%s,%s)" % (item, w))
        if w < 0:
            raise ValueError("Expected a non-negative number, got instead %s" % w)
        candidate_weight = self._weight + w
        if not self.is_empty():
            if w > self.peek()[1]:
                raise ValueError("Pushing weight greater than top element ! %s > %s", (w, self.peek()[1]))
        if candidate_weight > self._max_weight:
            raise ValueError("Can't exceed max_weight ! (%s > %s)" % (candidate_weight, self._max_weight))
        self._weight = candidate_weight
        self._elements.append((item, w))
        #/jupman-raise

    def pop(self):
        """ Removes the top element in the backpack and RETURN it
            as a tuple (element_id, weight) like ('a', 3)

            - if backpack is empty, raise IndexError
            - MUST run in O(1)
        """
        #jupman-raise
        if len(self._elements) == 0:
            raise IndexError("Empty stack !")
        else:
            debug("Popping %s " % str(self._elements[-1]))

            el = self._elements.pop()
            self._weight -= el[1]
            return el
        #/jupman-raise


# NOTE: this function is implemented *outside* the class !

def remove(backpack, el):
    """
        Remove topmost occurrence of el found in the backpack, 
        and RETURN it (as a tuple name, weight)
        
        - if el is not found, raises ValueError        

        - DO *NOT* ACCESS DIRECTLY FIELDS OF BACKPACK !!!
          Instead, just call methods of the class!

        - MUST perform in O(n), where n is the backpack size

        - HINT: To remove el, you need to call Backpack.pop() until
                the top element is what you are looking for. You need 
                to save somewhere the popped items except the one to 
                remove, and  then push them back again.
    
    """
    #jupman-raise
    rem = []
    ret = None
    while not backpack.is_empty():
        tup = backpack.peek()
        if tup[0] == el:
            ret = backpack.pop()
            break
        else:
            rem.append(backpack.pop())

    # restores backpack
    while len(rem) != 0:
        restored = rem.pop()
        backpack.push(restored[0], restored[1])
    
    if ret:
        return ret
    else:
        raise ValueError("Couldn't find element %s" % el)

    #/jupman-raise

