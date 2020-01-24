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


class DigiList:
    """
        This is a stripped down version of the LinkedList as previously seen, 
        which can only hold integer digits 0-9.

        NOTE: there is also a _last pointer

    """
        
    def __init__(self):
        self._head = None
        self._last = None
        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "DigiList: " + ",".join(strings)
        
    def is_empty(self):
        return self._head == None

    def last(self):
        """ Returns the last element in the list, in O(1). 
        
            - If list is empty, raises ValueError. 
        """
        
        if (self._head == None):
            raise ValueError("Tried to get the last element of an empty list!")
        else:    
            return self._last.get_data()

    def add(self,item):    
        """ Adds item at the beginning of the list """

        if type(item) != int:
            raise ValueError("Expected an integer digit, found instead %s " % item)
        if item < 0 or item > 9:
            raise ValueError("Expected a single digit integer, found instead %s " % item)

        new_head = Node(item)
        new_head.set_next(self._head)
        if self._last == None:
            self._last = new_head
        self._head = new_head
        

    def plus_one(self):
        """ MODIFIES the digi list by summing one to the integer number it represents                    
            - you are allowed to perform multiple scans of the linked list
            - remember the list has a _last pointer
            
            - MUST execute in O(N) where N is the size of the list          
            - DO *NOT* create new nodes EXCEPT for special cases:
                a. empty list ( [] -> [1] )
                b. all nines ( [9,9,9] -> [1,0,0,0] )                     
            - DO *NOT* convert the digi list to a python int            
            - DO *NOT* convert the digi list to a python list            
            - DO *NOT* reverse the digi list            
        """
        #jupman-raise

        if self._last == None:
            self.add(1)
        
        else:
            if self._last.get_data() < 9:
                self._last.set_data(self._last.get_data() + 1)
                return
            else:

                inc_node = None
                current = self._head                
                
                while current != None:
                    if current.get_data() < 9:
                        inc_node = current

                    current = current.get_next()
                
                if inc_node == None:
                    self.add(0)
                    inc_node = self._head
                
                inc_node.set_data(inc_node.get_data() + 1)
                current = inc_node.get_next()
                while current != None:
                    current.set_data(0)
                    current = current.get_next()
            
        #/jupman-raise
        