class Node:
    
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
        
    def __init__(self):
        self._head = None
        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def is_empty(self):
        """ Return True if the list is empty, False otherwise
        
            - MUST execute in O(1)
        """
        return self._head == None


    def add(self,item):            
        """ Adds item at the beginning of the list 
        
            - MUST execute in O(1)
        """
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head        


    def linalg(self):
        """  
            Assume nodes hold data as a string "kc" where k is a single digit 
            and c any character.
            
            MODIFY the linked list by stripping the k from original nodes, 
            and inserting k-1 new nodes next to each node.
                    
            - ASSUME every k is >= 1
            - MUST execute in O(s) where s is the sum of all k found.
            
        """                
        #jupman-raise
        
        current = self._head
        
        while current != None:
            
            k = int(current._data[0])
            c = current._data[1]
            current._data = c
            
            nxt = current._next
            
            for i in range(k-1):
                new = Node(c)
                current._next = new
                current = new
            current._next = nxt
            current = nxt
            
        #/jupman-raise                