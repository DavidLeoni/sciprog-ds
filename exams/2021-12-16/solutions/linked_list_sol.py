
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
        
    def norep(self):
        """ MODIFIES this list by removing all the consecutive 
            repetitions from it.

            - MUST perform in O(n), where n is the list size.
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