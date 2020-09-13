class Node:
    """ A Node of a LinkedQueue.

    """

    def __init__(self, initdata):
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

class LinkedQueue:
    """ A queue implemented as a LinkedList, with additional _tail pointer
        and _size counter

        - Data in enqueued at he right, in the tail
        - Data is dequeued at the left, removing it from the head

        Example, where the arrows represent _next pointers:

          _head                        _tail
              a -> b -> c -> d -> e -> f


        q = LinkedQueue()

        q.enqn(['a','b','c'])

          _head         _tail
              a -> b -> c

        q.enqn(['d'])

          _head              _tail
              a -> b -> c -> d


        q.enqn(['e','f'])

          _head                        _tail
              a -> b -> c -> d -> e -> f

        q.deqn(3)

        Returns ['a', 'b', 'c'] and queue becomes:
        
          _head         _tail
              d -> e -> f

        q.deqn(1)
        
        Returns ['d'] and queue becomes:
        
          _head    _tail
              e -> f

        q.deqn(5)

        raises LookupError as there aren't enough elements to remove

    """

    def __init__(self):
        """ Initializes the queue. Note there is no capacity as parameter

            - Complexity: O(1)
        """

        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to
            quickly inspect the data by printing it.
        """
        current = self._head
        strings = []

        while (current != None):
            strings.append(str(current.get_data()))
            current = current.get_next()

        return "LinkedQueue: " + ",".join(strings)



    def size(self):
        """ Return the size of the queue.

            - Complexity: O(1)
        """
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.

            - Complexity: O(1)
        """
        return self._head == None


    def top(self):
        """ Return the element at the head of the queue, without removing it.

            - If the queue is empty, raises LookupError.
            - Complexity: O(1)
        """
        if self._head != None:
            return self._head.get_data()
        else:
            raise LookupError("Queue is empty !")


    def tail(self):
        """ Return the element at the tail of the queue (without removing it).

            - If the queue is empty, raises LookupError.
            - Complexity: O(1)
        """
        if self._tail != None:
            return self._tail.get_data()
        else:
            raise LookupError("Queue is empty !")


    def enqn(self, lst):
        """ Enqueues provided list of elements at the tail of the queue

            - Required complexity: O(len(lst))
            - NOTE: remember to update the _size and _tail

            Example: supposing arrows represent _next pointers:

          _head         _tail
              a -> b -> c

            Calling

            q.enqn(['d', 'e', 'f', 'g'])

            will produce the queue:

          _head                             _tail
              a -> b -> c -> d -> e -> f -> g


        """
        #jupman-raise

        self._size += len(lst)

        for d in lst:

            new_node = Node(d)

            if self._head == None:     # empty queue
                self._head = new_node
                self._tail = new_node
            else:                      # non-empty queue
                self._tail.set_next(new_node)
                self._tail = new_node
        #/jupman-raise

    def deqn(self, n):
        """ Removes n elements from the head, and return them as a Python list,
            where the first element that was enqueued will appear at the *beginning* of
            the returned Python list.

            - if n is greater than the size of the queue, raises a LookupError.
            - required complexity: O(n)

            NOTE 1: return a list of the *DATA* in the nodes, *NOT* the nodes themselves
            NOTE 2: DO NOT try to convert the whole queue to a Python list for playing with splices.
            NOTE 3: remember to update _size, _head and _tail when needed.


            For example, supposing arrows represent _next pointers:


          _head                             _tail
              a -> b -> c -> d -> e -> f -> g

            q.deqn(3) will return the Python list ['a', 'b', 'c']

            After the call, the queue will be like this:

          _head              _tail
              d -> e -> f -> g

        """
        #jupman-raise
        if n > self._size:
            raise LookupError('Asked to dequeue %s elements, but only %s are available!' % (n, self._size))

        ret = []

        current = self._head

        k = 0
        while k < n:
            ret.append(current.get_data())
            current = current._next
            k += 1

        self._size -= n
        if self._size == 0:
            self._tail = None
            self._head = None
        else:
            self._head = current

        return ret
        #/jupman-raise
