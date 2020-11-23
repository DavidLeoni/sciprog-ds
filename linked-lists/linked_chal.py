
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
        LinkedList v1 - slow basic LinkedList
        
        This class is similar to 'UnorderedList' in the book, with these differences:
            - has more pythonic names
            - tries to mimic more closely the behaviour of default Python list, raising exceptions on 
              boundary conditions like removing non exisiting elements.
    """
        
    def __init__(self):
        self._head = None
        
    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to 
            quickly inspect the data by printing it. 
        """
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def is_empty(self):
        """ Return True if the list is empty, False otherwise
        """        
        return self._head == None
        

    def add(self,item):            
        """ Adds item at the beginning of the list 
        """        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

        
    def rshift(self, el):
        """ Shifts toward right the *data* of all nodes by one,
            writing el as data in first node and finally 
            RETURN the data that was in last node 
            
            - if list is empty, raises ValueError
            
            - DO NOT create new nodes nor rearrange links
            - ONLY write node *data*            
            - MUST execute in O(n) where n is the list size            
        """
        raise Exception('TODO IMPLEMENT ME !')

    def lshift(self, el):
        """ Shifts toward left the *data* of all nodes by one,
            writing el as data in last node and finally 
            RETURN the data that was in first node 
            
            - if list is empty, raises ValueError
            
            - DO NOT create new nodes nor rearrange links
            - ONLY write node *data*            
            - MUST execute in O(n) where n is the list size            
        """
        raise Exception("TODO IMPLEMENT ME!")
        
        
                