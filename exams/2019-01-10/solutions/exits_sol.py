import pprint
from queue import Queue
from collections import deque

DEBUG = True
def debug(msg):
    if DEBUG:
        print("DEBUG: ", str(msg).replace('\n', '\n' + (' '*8)))


#PrettyPrint(indent=4)
pp = pprint.PrettyPrinter(indent=4).pprint
pformat = pprint.PrettyPrinter(indent=4).pformat

class DiGraph:
    """ A simple graph data structure, represented as a dictionary of adjacency lists
    
        Verteces can be of any type, to keep things simple in this data model they coincide with their labels.
        Adjacency lists hold the target verteces. 
        Attempts to add duplicate targets will be silently ignored.
        
        For shorthand construction, see separate dig() function
    """
            
    def __init__(self):
        # The class just holds the dictionary _edges: as keys it has the verteces, and 
        # to each vertex associates a list with the verteces it is linked to.
        self._edges = {}
        
    def add_vertex(self, vertex):
        """ Adds vertex to the DiGraph. A vertex can be any object.
            
            If the vertex already exist, does nothing.
        """
        if vertex not in self._edges:            
            self._edges[vertex] = []
    
    def verteces(self):
        """ Returns a set of the graph verteces. Verteces can be any object. """
        
        # Note dict keys() return a list, not a set. Bleah.  
        # See http://stackoverflow.com/questions/13886129/why-does-pythons-dict-keys-return-a-list-and-not-a-set
        return set(self._edges.keys()) 
        
    def has_vertex(self, vertex):
        """ Returns true if graph contains given vertex. A vertex can be any object. """
        return vertex in self._edges
    
    def add_edge(self, vertex1, vertex2):
        """ Adds an edge to the graph, from vertex1 to vertex2
        
            If verteces don't exist, raises an Exception.
            If there is already such an edge, exits silently.            
        """
        
        if not vertex1 in self._edges:
            raise Exception("Couldn't find source vertex: " + str(vertex1))

        if not vertex2 in self._edges:
            raise Exception("Couldn't find target vertex: " + str(vertex2))        
            
        if not vertex2 in self._edges[vertex1]:
            self._edges[vertex1].append(vertex2)
            
    def __str__(self):
        """ Returns a string representation like the following:
        
            >>> print gr('a',['b','c', 'd'],
                         'b', ['b'],
                         'c', ['a'])

            a: [b,c]
            b: [b]
            c: [a]         
            d: []
        
        """
        
        if (len(self._edges) == 0):
            return "\nDiGraph()" 
        
        max_len=0
        
        sorted_verteces = sorted(self._edges.keys(), key=str)
        
        for source in self._edges:
            max_len = max(max_len, len(str(source)))
        
        strings = ["\n"]
        
        for source in sorted_verteces:
            
            strings.append(str(source).ljust(max_len))
            strings.append(': ')            
            strings.append(str(self._edges[source]))
            
            strings.append('\n')
        
        return ''.join(strings)
        
    def __repr__(self):              
        return self.__str__()

    def adj(self, vertex):
        """ Returns the verteces adjacent to vertex. 
            
            NOTE: verteces are returned in a NEW list.
            Modifying the list will have NO effect on the graph!
        """
        if not vertex in self._edges:
            raise Exception("Couldn't find a vertex " + str(vertex))
        
        return self._edges[vertex][:]
      
    def __eq__(self, other):
        """ !!!   NOTE: although we represent the set with adjanceny lists, for __eq__
            graph dig('a', ['b','c']) is considered equals to a graph dig('a', ['c', 'b']) !!! 
        """
            
        if not isinstance(other, DiGraph):
            return False            
        
        if self.verteces() != other.verteces():
            return False
        
        
        for source in self._edges:            
            if set(self._edges[source]) != set(other._edges[source]):
                return False
        
        return True              
        
    def is_empty(self):
        """  A DiGraph for us is empty if it has no verteces and no edges """
        
        return len(self._edges) == 0

    def bfs(self, source):
        """ Example bfs that performs a simple breadth first search 
            in the graph and prints visited nodes.
            Starts from provided source vertex id.

            If source is not in the graph, raises a Exception
        """
   
       
        if not source in self.verteces():
            raise Exception("Can't find vertex:" + str(source))
        
        Q = deque()
        # we start from source 

        Q.append(source)
        visited = {}
        for v in self._edges:
            visited[v] = False
        visited[source] = True

        while len(Q)>0:
            u = Q.popleft()
            debug("Removed from queue: %s" % u)
            # Visit node u
            for v in self._edges[u]:         
                debug("  Found neighbor: %s" % v)   
                # Visit edge (u,v)
                if not visited[v]:
                    debug("    not yet visited, enqueueing ..")
                    visited[v] = True
                    Q.append(v)                                        
                else:
                    debug("    already visited")
            debug("  Queue is: %s " % list(Q))

    def dfs(self, source):
        """ Example of a simple recursive depth first search on the graph,
            Starts from source vertex id and prints steps.
            Already visited nodes are set in provided boolean list  mark
            
            - If the graph is empty, raises an Exception.
        """
        
        if self.is_empty():
            raise Exception("Cannot perform DFS on an empty graph!")                

        S = []
        S.append(source)
        visited = {}
        for v in self.verteces():
            visited[v] = False

        debug("Stack is: %s " % S)
        while not len(S) == 0:
            u = S.pop()
            debug("popping from stack: %s" % u)
            if not visited[u]:
                debug("  not yet visited")
                # visit node u (pre-order)
                visited[u] = True
                for v in self.adj(u):
                    debug("  Scheduling for visit: %s" % v)
                    # visit edge (u,v)
                    S.append(v)
                debug("Stack is : %s " % S)
            else:
                debug("  already visited!")
        

    def has_edge(self, source, target):
        """  Returns True if there is an edge between source vertex and target vertex. 
             Otherwise returns False.

            If either source, target or both verteces don't exist raises an Exception.
        """
        if (not self.has_vertex(source)):
            raise Exception("There is no source vertex " + str(source))
            
        if (not self.has_vertex(target)):
            raise Exception("There is no source vertex " + str(target))
                
        return target in self._edges[source]                                


    def cp(self, source):
        """ Performs a BFS search starting from provided node label source and 
            RETURN a dictionary of nodes representing the visit tree in the 
            child-to-parent format, that is, each key is a node label and as value 
            has the node label from which it was discovered for the first time

            So if node "n2" was discovered for the first time while
            inspecting the neighbors of "n1", then in the output dictionary there 
            will be the pair "n2":"n1".

            The source node will have None as parent, so if source is "n1" in the 
            output dictionary there will be the pair  "n1": None

            NOTE: This method must *NOT* distinguish between exits 
                  and normal nodes, in the tests we label them n1, e1 etc just
                  because we will reuse in next exercise
            NOTE: You are allowed to put debug prints, but the only thing that
                  matters for the evaluation and tests to pass is the returned 
                  dictionary

        """
        #jupman-raise
        if not source in self.verteces():
            raise Exception("Can't find vertex:" + str(source))
        
        ret = {}

        Q = deque()
        # we start from source 

        Q.append(source)
        visited = {}
        for v in self._edges:
            visited[v] = False
        visited[source] = True
        ret[source] = None

        while len(Q)>0:
            u = Q.popleft()
            debug("Removed from queue: %s" % u)
            # Visit node u
            for v in self._edges[u]:         
                debug("  Found neighbor: %s" % v)   
                # Visit edge (u,v)
                if not visited[v]:
                    debug("    not yet visited, enqueueing ..")
                    visited[v] = True
                    ret[v] = u
                    Q.append(v)                                         
                    
                else:
                    debug("    already visited")
            debug("  Queue is: %s " % list(Q))

        return ret
        #/jupman-raise


          

def exits(cp):
    """
        INPUT: a dictionary of nodes representing a visit tree in the 
        child-to-parent format, that is, each key is a node label and 
        as value has its parent as a node label. The root has
        associated None as parent.

        OUTPUT: a dictionary mapping node labels of exits to a list
                of node labels representing the the shortest path from 
                the root to the exit (root and exit included)
                
    """
    #jupman-raise
    ret = {}
    for v in cp:
        if v.startswith('e'):
            ret[v] = []
    
    # find traces until source node
    for v in ret:
        u = v
        while u != None:
            ret[v].append(u)
            u = cp[u]
    
    # reverses
    for v in ret:
        ret[v].reverse()

    return ret
    #/jupman-raise