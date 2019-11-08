import pprint
from queue import Queue
from collections import deque

DEBUG = True
def debug(msg):
    if DEBUG:
        print("DEBUG: ", msg.replace('\n', '\n' + (' '*8)))

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

            If source is not in the graph, raises an Exception                         
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
        #jupman-raise
        if (not self.has_vertex(source)):
            raise Exception("There is no source vertex " + str(source))
            
        if (not self.has_vertex(target)):
            raise Exception("There is no source vertex " + str(target))
                
        return target in self._edges[source]                                
        #/jupman-raise

    def remove_vertex(self, vertex):
        """ Removes the provided vertex  and returns it
            
            If the vertex is not found, raises an Exception.
        """
        #jupman-raise        
        if not vertex in self._edges:
            raise Exception("Couldn't find vertex:" +str(vertex))
        
        for source in self.verteces():
            if vertex in self._edges[source]:
                self._edges[source].remove(vertex)
        
        return self._edges.pop(vertex)
        #/jupman-raise


    def transpose(self):
        """ Reverses the direction of all the edges 
        
            NOTE: this method changes in-place the graph: does **not** create a new instance
            and does *not* return anything !!
            
            NOTE: To implement it *avoid* modifying the existing _edges dictionary (would
            probably more problems than anything else).
            Instead, create a new dictionary, fill it with the required 
            verteces and edges ad then set _edges to point to the new dictionary.

        """
        #jupman-raise
           
        # let's save the old edges   
        old_edges = self._edges   
        
        # better start from scratch with a new map
        self._edges = {}
        
        for v in old_edges:
            self._edges[v] = []
        
        for source in old_edges:
            for target in old_edges[source]:
                self.add_edge(target, source)  # using add_edge we avoid duplicates !
        #/jupman-raise

    def has_self_loops(self):
        """ Returns True if the graph has any self loop (a.k.a. cap), False otherwise """
        #jupman-raise

        for source in self._edges:
            if source in self._edges[source]:
                return True
        
        return False
        #/jupman-raise
        
    def remove_self_loops(self):
        """ Removes all of the self-loops edges (a.k.a. caps) 
            
            NOTE: Removes just the edges, not the verteces!
        """
        #jupman-raise
        for source in self._edges:
            if source in self._edges[source]:
                self._edges[source].remove(source)
                
        #/jupman-raise

    def undir(self):
        """ Return a *NEW* undirected version of this graph, that is, if an edge a->b exists in this          graph, the returned graph must also have both edges  a->b and b->a
            *DO NOT* modify the current graph, just return an entirely new one.
        """
        #jupman-raise
        ret = DiGraph()
                
        for v in self._edges:
            ret.add_vertex(v)
            
        for source in self._edges:
            for target in self._edges[source]:
                ret.add_edge(source, target)
                ret.add_edge(target, source)
                
        return ret
        #/jupman-raise


    def distances(self, source):
        """ 
        Returns a dictionary where the keys are verteces, and each vertex v is associated
        to the *minimal* distance in number of edges required to go from the source 
        vertex to vertex v. If node is unreachable, the distance will be -1
        
        Source has distance zero from itself
        Verteces immediately connected to source have distance one.

        if source is not a vertex, raises an Exception
        
        HINT: implement this using bfs search.
        """   
        #jupman-raise     
       
        # First off, we use a BFS, because it explores nodes layer by layer,
        # so in the resulting tree each node distance is always minimal with 
        # respect to the source       
       
        if not source in self.verteces():
            raise Exception("Can't find vertex:" + str(source))
        
        Q = deque()
        # we start from source 

        Q.append(source)
        visited = {}
        for v in self._edges:
            visited[v] = False
        visited[source] = True

        # As result we just want a dictionary with verteces and distances, so we 
        # create it here.                   
        distances = {}

        # Since some node may never be reached, we first we 
        # initialize everything with -1, 
        for v in self._edges:
            distances[v] = -1
        # origin distance from itself is zero:
        distances[source] = 0  


        while len(Q)>0:
            u = Q.popleft()
            #debug("Removed from queue: %s" % u)
            # Visit node u
            for v in self._edges[u]:
                # Visit edge (u,v)
                if not visited[v]:
                    #debug("  not yet visited")
                    visited[v] = True
                    distances[v] = distances[u] + 1
                    Q.append(v)
                #else:
                    #debug("  already yet visited")


        return distances  
        #/jupman-raise      
        
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
        
    def cc(self):
        """ Finds the connected components of the graph, returning a dict object
            which associates to the verteces the corresponding connected component 
            number id, where 1 <= id <= |V|  
        
            IMPORTANT:  ASSUMES THE GRAPH IS UNDIRECTED ! 
                        ON DIRECTED GRAPHS, THE RESULT IS UNPREDICTABLE !
            
            To develop this function, implement also ccdfs function inside this method.
            
        """
        #jupman-raise

        def ccdfs(counter, source, ids):
            """
                Performs a DFS from source vertex
                
                HINT: Copy in here the method from DFS and adapt it as needed       
                HINT: store the connected component id in VertexLog objects
            """
            ids[source] = counter
            for v in self._edges[source]:
                if ids[v] == 0:
                    ccdfs(counter, v, ids)

        ids = {}
        for v in self._edges:
            ids[v] = 0

        counter = 0
        
        for u in self._edges:
            if ids[u] == 0:
                counter += 1
                ccdfs(counter, u, ids)                                
            
        return ids

        #/jupman-raise
        
    def has_cycle(self):
        """ Return True if this directed graph has a cycle, return False otherwise. 
        
            - To develop this function, implement also has_cycle_rec(u) inside this method
            - Inside has_cycle_rec, to reference variables of has_cycle you need to
              declare them as nonlocal like  
                 nonlocal clock, dt, ft
            - MUST be able to also detect self-loops
        """
        #jupman-raise

        def has_cycle_rec(u):
        
            nonlocal clock, dt, ft
            clock = clock+1
            dt[u] = clock
            for v in self.adj(u):
                if dt[v] == 0:
                    if has_cycle_rec(v):
                        return True
                elif dt[u] >= dt[v] and ft[v] == 0:
                    return True
            clock = clock + 1
            ft[u] = clock
            return False
            

        clock = 0
        dt = {}
        ft = {}
        for v in self.verteces():
            dt[v] = 0
            ft[v] = 0

        for u in self.verteces():
            if ft[u] == 0:
                if has_cycle_rec(u):
                    return True
        return False
        #/jupman-raise

    def top_sort(self):
        """ RETURN a topological sort of the graph. To implement this code, 
            feel free to adapt Montresor algorithm

            - implement  Stack S  as a list
            - implement  visited  as a set
            - NOTE: differently from Montresor code, for tests to pass 
                    you will need to return a reversed list. Why ?
        """
        #jupman-raise
        def topSortRec(u, visited, S):
            visited.add(u)
            for v in self.adj(u):
                if not v in visited:
                    topSortRec(v, visited, S)
            S.append(u)

        S = []
        visited = set()
        for u in self.verteces():
            if not u in visited:
                topSortRec(u, visited, S)
        S.reverse()
        return S
        #/jupman-raise


def full_graph(verteces):
    """ Returns a DiGraph which is a full graph with provided verteces list.
    
        In a full graph all verteces link to all other verteces (including themselves!).
    """
    #jupman-raise

    g = DiGraph()    
    for v in verteces:
        g.add_vertex(v)
    
    for v in verteces:
        for w in verteces:
            g.add_edge(v, w)
    
    return g
    #/jupman-raise

def dag(verteces):
    """ Returns a DiGraph which is DAG (Directed Acyclic Graph) made out of provided verteces list
    
        Provided list is intended to be in topological order.
        NOTE: a DAG is ACYCLIC, so caps (self-loops) are not allowed !!
    """
    #jupman-raise
    g = DiGraph()    
    for v in verteces:
        g.add_vertex(v)

    if len(verteces) > 1:
        i = 1
        for v in verteces:            
            for w in verteces[i:]:
                g.add_edge(v,w)
            i += 1
    return g
    #/jupman-raise

def list_graph(n):
    """ Return a graph of n verteces displaced like a 
        monodirectional list:  1 -> 2 -> 3 -> ... -> n 
        
        Each vertex is a number i, 1 <= i <= n  and has only one edge connecting it
        to the following one in the sequence        
        If n = 0, return the empty graph.
        if n < 0, raises an Exception.
    """    
    #jupman-raise   
    if n == 0:
        return DiGraph()
        
    if n < 0:
        raise Exception("Found negative n: " + str(n))
        
    
    g = DiGraph()
    for j in range(1, n+1):
        g.add_vertex(j)

    for k in range(1, n):
            g.add_edge(k, k+1)
      
    return g    
    #/jupman-raise

def star_graph(n):
    """ Returns graph which is a star with n nodes 

        First node is the center of the star and it is labeled with 1. This node is linked 
        to all the others. For example, for n=4 you would have a graph like this:
        
                3
                ^
                |    
           2 <- 1 -> 4           
           
        If n = 0, the empty graph is returned
        If n < 0, raises an Exception           
    """    
    #jupman-raise
    if n == 0:
        return DiGraph()
        
    if n < 0:
        raise Exception("Found negative n: " + str(n))
    
    g = DiGraph()
    
    for i in range(1,n+1):
        g.add_vertex(i)
    
    for i in range(2,n+1):
        g.add_edge(1, i)
    
    return g
    #/jupman-raise   
    
def odd_line(n):
    """ Returns a DiGraph with n verteces, displaced like a line of odd numbers
    
        Each vertex is an odd number i, for  1 <= i < 2n. For example, for
        n=4 verteces are displaced like this:
                
        1 -> 3 -> 5 -> 7
        
        For n = 0, return the empty graph
            
    """
    #jupman-raise
        
    g = DiGraph()
    
    for i in range(1, n + 1):
        g.add_vertex(2*i - 1)
    
    for i in range(1, n):
        g.add_edge(2*i - 1, 2*i + 1)
        
    return g
    #/jupman-raise

def even_line(n):
    """ Returns a DiGraph with n verteces, displaced like a line of even numbers
    
        Each vertex is an even number i, for  2 <= i <= 2n. For example, for
        n=4 verteces are displaced like this:
                
        2 <- 4 <- 6 <- 8
        
        For n = 0, return the empty graph
            
    """
    #jupman-raise 
       
    g = DiGraph()
    
    for i in range(1, n + 1):
        g.add_vertex(2 * i)
    
    for i in range(1, n):        
        g.add_edge(2 * (i + 1), 2 * i)

    return g
    #/jupman-raise

def quads(n):
    """ Returns a DiGraph with 2n verteces, displaced like a strip of quads.
    
        Each vertex is a number i,  1 <= i <= 2n. 
        For example, for n = 4, verteces are displaced like this:
                
        1 -> 3 -> 5 -> 7
        ^    |    ^    |
        |    ;    |    ;
        2 <- 4 <- 6 <- 8
        
        where 
        
          ^                                         |
          |  represents an upward arrow,   while    ;  represents a downward arrow        
    
    """
    #jupman-raise

    g = DiGraph()
    
    for i in range(1, 2 * n + 1):
        g.add_vertex(i)
    
    for i in range(1, n):
        g.add_edge(2*i - 1, 2*i + 1)
        g.add_edge(2 * (i+1), 2 * i)

    for i in range(1, n + 1):
        if i % 2 == 0:        
            g.add_edge(2*i - 1, 2*i)
        else:
            g.add_edge(2*i, 2*i - 1)
                        
    return g
    #/jupman-raise

def pie(n):
    """ Returns a DiGraph with n+1 verteces, displaced like a polygon with a perimeter 
        of n verteces progressively numbered from 1 to n. A central vertex numbered zero 
        has outgoing edges to all other verteces.
        
        For n = 0, return the empty graph.
        For n = 1, return vertex zero connected to node 1, and node 1 has a self-loop.
        
    """
    #jupman-raise
        
    g = DiGraph()
    
    if n == 0:    
        return g
    
    for i in range(0, n + 1):
        g.add_vertex(i)
            
    for i in range(1, n + 1):
        g.add_edge(0, i)

    for i in range(1, n):
        g.add_edge(i, i + 1)
    
    if n > 0:
        g.add_edge(n, 1)
        
    return g
    #/jupman-raise
        
def flux(depth):
    """ Returns a DiGraph with 1 + (d * 3) verteces displaced like a Y:
        - from a central node numbered 0, three branches depart  
        - all edges are directed outward
        - on each branch there are 'depth' verteces. 
        - if depth < 0, raises a ValueError
                
        For example, for depth=2 we get the following graph (suppose arrows point outward):
        
             4         5
              \       /
               1     2
                \   /
                  0
                  |
                  3
                  |
                  6
        
    """
    #jupman-raise 
    if depth < 0:
        raise ValueError("Expected zero or positive depth, found instead %s " % depth)
    
    g = DiGraph()
    
    if depth == 0:
        g.add_vertex(0)
        return g
    
    for i in range(0, depth*3 + 1):
        g.add_vertex(i)

    for i in range(1, 4):
        g.add_edge(0, i)
            
    j = 1
    for lev in range(1, ((depth-1)*3) + 1):
        g.add_edge(j, j + 3)
        j += 1

    return g 
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
    