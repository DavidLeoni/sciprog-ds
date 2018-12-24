class Node:
    """ A Node of an LinkedList. Holds data provided by the user. """
    
    def __init__(self,initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext


class LinkedList:
    """
        This is a stripped down version of the LinkedList as previously seen.
        
    """
        
    def __init__(self):
        self._head = None

        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def add(self,item):    
        """ Adds item at the beginning of the list """
        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

    def remove(self, item):
        """ Removes first occurrence of item from the list
        
            If item is not found, raises an Exception.
        """
        current = self._head        
        prev = None
        
        while (current != None):
            if (current.get_data() == item):
                if prev == None:  # we need to remove the head 
                    self._head = current.get_next()
                else:  
                    prev.set_next(current.get_next())
                    current = current.get_next()                    
                return  # Found, exits the function
            else:
                prev = current
                current = current.get_next() 
        
        raise Exception("Tried to remove a non existing item! Item was: " + str(item))

                        
    def occurrences(self, item):
        """ 
            Returns the number of occurrences of item in the list.

            - MUST execute in O(n) where n is the length of the list.
        """
        #jupman-raise
        current = self._head            
        
        i = 0        
        
        while current != None:            
            if current.get_data() == item:            
                i += 1
            current = current.get_next()
                
        return i
        #/jupman-raise
        
    def shrink(self):
        """ 
            Removes from this LinkedList all nodes at odd indeces (1, 3, 5, ...), 
            supposing that the first node has index zero, the second node 
            has index one, and so on. 
            
            So if the LinkedList is 
                'a','b','c','d','e' 
            a call to shrink() will transform the LinkedList into 
                'a','c','e'
            
            - MUST execute in O(n) where 'n' is the length of the list.
            - Does *not* return anything.
        """
        #jupman-raise
        current = self._head            
                
        while current != None:                                    
            if current.get_next() != None:
                    current.set_next(current.get_next().get_next())
            current = current.get_next()
        #/jupman-raise

    def dup_first(self):
        """ Modifies this list by adding a duplicate of first node right after it. 
        
            For example, the list 'a','b','c' should become 'a','a','b','c'.            
            An empty list remains unmodified.            

            ** DOES NOT RETURN ANYTHING !!! **          

        """
        #jupman-raise
        if self._head != None:            
            new_node = Node(self._head.get_data())
            new_node.set_next(self._head.get_next())
            self._head.set_next(new_node)            
        #/jupman-raise
            
    def dup_all(self):
        """ Modifies this list by adding a duplicate of each node right after it.
        
            For example, the list 'a','b','c' should become 'a','a','b','b','c','c'.
            An empty list remains unmodified.      
            
            ** MUST PERFORM IN O(n) WHERE n is the length of the list. **
            
            ** DOES NOT RETURN ANYTHING !!! **
        """
        #jupman-raise
        current = self._head                
        
        while current != None:            
            new_node = Node(current.get_data())
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            current = new_node.get_next()          
        #/jupman-raise

    def norep(self):
        """ MODIFIES this list by removing all the consecutive 
            repetitions from it.
            
            - MUST perform in O(n), where n is the list size.
        
            For example, after calling norep:

            'a','a','b','c','c','c'   will become  'a','b','c'
            
            'a','a','b','a'   will become   'a','b','a'            
            
        """
        #jupman-raise
        if self._head == None:
            return
        else:
            current = self._head.get_next()
            last = self._head        
        
        
        while current != None:
            
            if last.get_data() == current.get_data():    
                last.set_next(current.get_next())                
            else:
                last = current            
            current = current.get_next()
        #/jupman-raise
                
    def find_couple(self,a,b):
        """ Search the list for the first two consecutive elements having data equal to 
            provided a and b, respectively. If such elements are found, the position
            of the first one is returned, otherwise raises LookupError.
            
            - MUST run in O(n), where n is the size of the list.
            - Returned index start from 0 included
            
        """
        #jupman-raise                
        current = self._head
        i = 0
        
        while current != None:
            if current._data == a:
                if current._next != None:
                    if current._next._data == b:
                        return i
            i += 1
            current = current._next
            
        raise LookupError("Couldn't find couple " + str(a) + "," + str(b) + "!")
        #/jupman-raise

    def swap (self, i, j):
        """
            Swap the data of nodes at index i and j. Indeces start from 0 included.
            If any of the indeces is out of bounds, rises IndexError.
            
            NOTE: You MUST implement this function with a single scan of the list.
            
        """
        #jupman-raise
        if i < 0 or j < 0:
            raise IndexError("Invalid indeces! Both must be non-negative, found instead: i="+str(i) +", j="+str(j))
        
        current = self._head

        k = 0
        nodei = None
        nodej = None
        while current != None:
            if k == i:
                nodei = current
                if nodej != None:
                    break
            if k == j:
                nodej = current
                if nodei != None:
                    break
            current = current.get_next()
            k += 1
        
        if nodei == None or nodej == None:
            raise IndexError("Out of bounds ! i = " + str(i) + " j = " + str(j) )
        
        tmp = nodej.get_data()
        nodej.set_data(nodei.get_data())
        nodei.set_data(tmp)
        #/jupman-raise

def mirror(lst):
    """ RETURN a NEW LinkedList having double the nodes of provided lst
        First nodes will have same elements of lst, following nodes will 
        have the same elements but in reversed order.
        
        For example:
            
            >>> mirror(['a'])
            LinkedList: a,a            
            
            >>> mirror(['a','b'])
            LinkedList: a,b,b,a

            >>> mirror(['a','c','b'])
            LinkedList: a,c,b,b,c,a
    
    """
    #jupman-raise
    ret = LinkedList()
    for e in lst:
        ret.add(e)
    for e in reversed(lst):
        ret.add(e)
    return ret
    #/jupman-raise

