class Node:
    """ A Node of an LinkedList. Holds data provided by the user. 
    
        Node v3 remains the same as Node v2 
    """
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
        A linked list implementation, v3.
        
        Improvements upon LinkedList v2: 
        
        * calculates append() in O(1) 
        * adds last() method to retrieve last element in O(1)
        
        This class is similar to 'UnorderedList' in the book, with these differences:
            - has more pythonic names
            - tries to mimic more closely the behaviour of default Python list, raising exceptions on 
              boundary conditions like removing non exisiting elements.
    """
        
    def __init__(self):
        self._head = None
        self._size = 0  
        self._last = None # NEW attribute '_last'
        
        
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
        return self._head == None

    def add(self,item):    
        """ Adds item at the beginning of the list """
        new_head = Node(item)
        new_head.set_next(self._head)
        if self._head == None: # NEW
            self._last = new_head # NEW
        self._head = new_head
        self._size += 1 
        

    def size(self):
        """ Returns the size of the list in O(1) """
        return self._size  

    def search(self,item):
        """ Returns True if item is present in list, False otherwise        
        """
        current = self._head
        
        while (current != None):            
            if (current.get_data() == item):
                return True
            else:
                current = current.get_next()  
            
        return False
        
    def remove(self, item):
        """ Removes first occurrence of item from the list
        
            If item is not found, raises an LookupError.
        """
        current = self._head        
        prev = None
        
        while (current != None):
                                                    
            if (current.get_data() == item):
                if (self._last == current):  # NEW
                    self._last = prev        # NEW 
                
                if prev == None:  # we need to remove the head 
                    self._head = current.get_next()
                else:  
                    prev.set_next(current.get_next())
                    current = current.get_next()  
                self._size -= 1  
                return  # Found, exits the function
            else:
                prev = current
                current = current.get_next() 
        
        raise LookupError("Tried to remove a non existing item! Item was: " + str(item))
    
    def append(self, e):
        """ Appends element e to the end of the list, in O(1)                        
        """                
        
        if self._head == None:
            self.add(e)
        else:                        
            new_node = Node(e)
            self._last.set_next(new_node) # NEW, we directly exploit _last pointer 
            self._last = new_node # NEW, need to update _last
            self._size += 1  
    

                
    def index(self, e):
        """ Return the index in the list of the first item whose value is x. 
        
            If item is not found, raises a LookupError
        """
        
        current = self._head
        count = 0        
        
        while (current != None):
            if (current.get_data() == e):
                return count
            else:
                current = current.get_next()  
                count += 1
        
        raise LookupError("Couldn't find element " + str(e) )
                
    def pop(self):
        """ Remove the last item of the list, and return it. 
            
            - If the list is empty, an ValueError is raised. 
        """
        if (self._head == None):
            raise ValueError("Tried to pop an empty list!")
        else:               
            
            current = self._head
             
            if (current.get_next() == None): # one element list
                popped = self._head
                self._head = None
                self._last = None  # NEW 
            else:    # we have more than one element
                prev = None            
                while current.get_next() != None:  # current will reach last element
                    prev = current
                    current = current.get_next()                                                                                            
                popped = current
                self._last = prev   # NEW 
                prev.set_next(None)                              

            self._size -= 1  
            
            return popped.get_data()
            
            
    def last(self):
        """ Returns the last element in the list, in O(1). 
        
            - If list is empty, raises ValueError. Since v2. 
        """
        
        if (self._head == None):
            raise ValueError("Tried to get the last element of an empty list!")
        else:    
            return self._last.get_data()


    def insert(self, i, e):
        """ Insert an item at a given position. 

            The first argument is the index of the element before which to insert, 
            so list.insert(0, e) inserts at the front of the list, and 
            list.insert(list.size(), e) is equivalent to list.append(e).
            
            - If i is negative or i > list.size(), raises an IndexError (default Python list
              appends instead to the end :-/ )
            
        """    
        if (i < 0):
            raise IndexError("Tried to insert at a negative index! Index was:" + str(i))
            
        count = 0
        current = self._head
        prev = None
        
        while (count < i and current != None):
            prev = current
            current = current.get_next()
            count += 1
        
        if (current == None):
            if (count == i):
                self.append(e)
            else:
                raise IndexError("Tried to insert outside the list ! "
                                + "List size=" + str(count) + "  insert position=" + str(i))
        else:
            #0 1
            #  i
            if (prev == None):
                self.add(e)
            else:
                new_node = Node(e)
                prev.set_next(new_node)
                new_node.set_next(current) 
                    
                self._size += 1 