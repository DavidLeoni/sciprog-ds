
class CircularQueue:
    """ A circular queue with a fixed capacity.
    """
    
    
    def __init__(self, capacity):
        """ Initializes the queue, reserving space for a number of elements equal to provided capacity.
        
            - If capacity is not an int, raises ValueError.
            - If capacity is <= 0, raises ValueError.
            - Complexity: O(capacity)
        """
        #jupman-raise
        if type(capacity) is not int:
            raise ValueError("Expected an int, found instead: %s" % capacity)
        
        if capacity <= 0:
            raise ValueError("Expected positive capacity, found instead %s" % capacity)
            
        self._A = [None] * capacity   # Creates array of capacity objects, fills it with None
        self._head = 0
        self._size = 0
        #/jupman-raise
        
    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to 
            quickly inspect the data by printing it. 
        """        
        
        return "CircularQueue: " + str(vars(self))

        
        
    def size(self):
        """ Return the size of the queue.
        
            - Complexity: O(1)
        """
        #jupman-raise
        return self._size
        #/jupman-raise
            
    def capacity(self):
        """ Return the capacity of the queue, that is, the maximum number of allowed elements in the queue.
            
            - Complexity: O(1)
        """
        #jupman-raise
        return len(self._A)
        #/jupman-raise

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.
        
            - Complexity: O(1)
        """
        #jupman-raise
        return self._size == 0
        #/jupman-raise
    
    def top(self):
        """ Return the element at the head of the queue, without removing it. 
        
            - If the queue is empty, raises LookupError.            
            - Complexity: O(1)
        """
        #jupman-raise
        if self._size > 0:
            return self._A[self._head]
        else:
            raise LookupError("Queue is empty !")    
        #/jupman-raise
            
    def enqueue(self, v):
        """ Enqueues provided element v at the end of the queue.
        
            - If the queue is full, raises BufferError.
            - Complexity: O(1)
        """
        #jupman-raise
        if self._size < len(self._A):
            self._A[(self._head + self._size) % len(self._A) ] = v
            self._size += 1
        else:
            raise BufferError("Queue is full !")
        #/jupman-raise

    def dequeue(self):
        """ Removes head element and returns it.
            
            - If the queue is empty, raises a LookupError.
            - Complexity: O(1)
        """
        #jupman-raise
        if self._size > 0:
            temp = self._A[self._head]
            self._head = (self._head + 1) % len(self._A)
            self._size -= 1
            return temp
        else:
            raise LookupError("Queue is empty !")                    
        #/jupman-raise
