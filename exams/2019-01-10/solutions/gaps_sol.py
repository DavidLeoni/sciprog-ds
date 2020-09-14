import unittest

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
        This is a stripped down version of the LinkedList seen in the lab
        
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

    def gaps(self):
        """ Assuming all the data in the linked list is made by numbers,
            finds the gaps in the LinkedList and return them as a Python list.
            
            - we assume empty list and list of one element have zero gaps
            - MUST perform in O(n) where n is the length of the list

            NOTE: gaps to return are *indeces* , *not* data!!!!
        """
        #jupman-raise
        
        ret = []
        
        i = 1
        current = self._head
        while current != None:
            d = current.get_data()
            if current.get_next() != None:
                if d < current.get_next().get_data():
                    ret.append(i)
            i += 1                
            current = current.get_next()
        
        return ret   
        #/jupman-raise
         

