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

            
    def flatv(self):
        """
            See exercise text for explanation

            - MUST run in O(n) where n is the length of the list

        """
        #jupman-raise
        current = self._head
        prev = None
        while current != None:
            if prev != None and current.get_next() != None: 
                a = prev.get_data()
                b = current.get_data()
                c = current.get_next().get_data()
                if a > b and b < c:
                    new_node = Node(b)
                    prev.set_next(new_node)
                    new_node.set_next(current)
                    return
            if prev == None:
                prev = self._head
            else:
                prev = prev.get_next()
            current = current.get_next()
        #/jupman-raise
