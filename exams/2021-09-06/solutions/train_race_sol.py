class TrainRace:
    
    
    def __init__(self, lengths, velocities):
        """ Initializes the class with two lists holding the lengths and velocities of trains

            - if list lengths mismatches, raise ValueError
            - if a length or a velocity is less than one, raises ValueError
            
            - MUST execute in O(n) where n is sum of train lengths
            - HINT: think about additional fields which may help speeding up the program
        """
        #jupman-raise
        
        if len(lengths) != len(velocities):
            raise ValueError("Mismatching input lengths: %s %s" % (lengths, velocities))
        
        for i in range(len(lengths)):
            l = lengths[i]
            v = velocities[i]
            if l < 1:
                raise ValueError("Invalid length at pos %s: %s" % (i, l))
            if v < 1:
                raise ValueError("Invalid velocity at pos %s: %s" % (i, v))
        
        self._velocities = velocities        
        self._lengths = lengths        
        self._paths = []
        
        for tl in lengths:
            self._paths.append(['*']*tl)
        self._pos = [0] * len(lengths)
        #/jupman-raise


    def get_paths(self):
        """ 
            Return the train paths as a list of list of characters
        
            ********  MUST RUN IN O(1)  *********
        
            HAVE YOU READ THE REQUIREMENT ABOVE ?
        """
        #jupman-raise
        return self._paths
        #/jupman-raise


    def step(self):
        """ Steps the simulation by moving each train toward right 
            by a number of cells given by its velocity.            
            
                        
            *** MUST run in O(v) where v is the sum of all velocities     
            
            *** Complexity MUST *NOT* depend on train length nor dashes length
            
            *** For simplicity, ASSUME velocity is always 
                less or equal than train length                 
            
            ********      HAVE YOU READ THE REQUIREMENTS ABOVE ?   ********
        """
        #jupman-raise
        
        # the idea is to avoid costly inserting by overwriting the existing train with some '-',
        # then append some '*' at the right.
        # In order to jump directly at the start of the train, we need the pos indexes.
        
        # NOTE 1: if you have used instructions like .insert(0, '-') remember it has complexity O(n), 
        #         if put inside a loop you get quadratic complexity!
        # NOTE 2: if you used instructions like list1 + list2, remember it has complexity O(n + m) 
        #          and creates a NEW list each time! Instead, when you want performance you should
        #          reuse existing data structures as much as possible 
        
        
        for i in range(len(self._paths)):            
            v = self._velocities[i]
            p = self._pos[i]
            l = self._lengths[i]
            for j in range(min(v,l)):
                self._paths[i][p+j] = '-'


            # v <= l example

            #     012345678901234
            #     p            
            #-----**********
            #     |        
            #     |  v  | 
            #     |   l    |  v  |            
            #-----------**********


            # v > l example
                
            #     012345678901234567890123456
            #     p            
            #-----*********
            #     |        
            #     |         v       |
            #     |   l   |         |   l   |            
            #-----------------------*********
                
            
            for j in range(v-l):
                self._paths[i].append('-')
                
            for j in range(min(v,l)):
                self._paths[i].append('*')                            
                
            self._pos[i] += v
        #/jupman-raise