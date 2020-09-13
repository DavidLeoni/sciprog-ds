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


    def slice(self, start, end):
        """ RETURN a NEW LinkedList created by copying nodes of this list
            from index start INCLUDED to index end EXCLUDED

            - if start is greater or equal than end, returns an empty LinkedList
            - if start is greater than available nodes, returns an empty LinkedList
            - if end is greater than the available nodes, copies all items until the tail without errors
            - if start index is negative, raises ValueError
            - if end index is negative, raises ValueError            

            - IMPORTANT: All nodes in the returned LinkedList MUST be NEW
            - DO *NOT* modify original linked list
            - DO *NOT* add an extra size field
            - MUST execute in O(n), where n is the size of the list
            
        """
        #jupman-raise

        if start < 0:
            raise ValueError('Negative values for start are not supported! %s ' % start)
        if end < 0:
            raise ValueError('Negative values for end are not supported: %s' % end)

        ret = LinkedList()

        if start >= end:
            return ret

        last = None
        i = 0
        current = self._head
        while current != None and i < start:
            current = current.get_next()
            i += 1

        if i != start:
            return ret

        while current != None and i < end:
            new = Node(current.get_data())
            if last == None:
                ret._head = new                
            else:                
                last.set_next(new)                
            last = new
            current = current.get_next()
            i += 1

        return ret
        #/jupman-raise