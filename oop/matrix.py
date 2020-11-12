
"""   

       WARNING: THIS FILE IS ONLY AN *INTERFACE*, 

       YOU DO *NOT* NEED TO IMPLEMENT ANYTHING HERE !
        
"""


class Matrix:
    """ An IMMUTABLE Matrix interface
    """
    
    def __init__(self, *args):
        """Initializes the Matrix with either:

            One argument: a list of lists
            Three arguments: number of rows
                             number of columns
                             a list of cell triplets (row_index,col_index,value)
                            - if number of rows or columns is less than indeces found 
                              in triplets, raise Value Error

            In both cases, provided data must allow the creation of a matrix with 
            at least one row and a column, otherwise raise ValueError
        """
        raise Exception("Should be implemented in a descendant of Matrix!") 

    def __str__(self):
        """ RETURN a nice human-readable formatted string, when POSSIBLE like this:
            
              Matrix  [ [5,2,6,3],
                        [8,4,7,4],
                        [2,1,9,8] ]

              - substitute Matrix with the descendant class name
              - NOTE: sometimes this representation is impractical (i.e. sparse matrices 
                      with large n/m), in that case use another format of your choice
        """
        raise Exception("Should be implemented in a descendant of Matrix!")
    
    def __repr__(self):
        """ RETURN one-line string representing a Python expression which would recreate the atrix
        """
        raise Exception("Should be implemented in a descendant of Matrix!")
    
    def shape(self):
        """RETURN the number of rows and columns as a tuple
        """
        raise Exception("Should be implemented in a descendant of Matrix!")

    def __getitem__(self, key):
        """Overrides default bracket access behaviour. 
           key is whatever the user passes within the brackets, in our case 
           we want user to be able to write

           my_mat[2,5]  to access element at row 2 and column 5

           NOTE 1: if the user types 2,5 inside the brackets, Python will actually 
                 generate a TUPLE (2,5)  so that is the key type you should 
                 accept (a tuple of *exactly two* integers)
           NOTE 2: Since this method signature is defined by Python documention:

              https://docs.python.org/3/reference/datamodel.html#object.__getitem__
  
            you MUST write it respecting ALL the indications of the docs, in particular
            think also about  what should happen in undesired scenarios when
            the user enters a key of wrong type, wrong value, etc as described 
            in the documentation
        """
        raise Exception("Should be implemented in a descendant of Matrix!")

    def nonzero(self):
        """Return a list of triplets (row index, column index, value) of non-zero cells,
           in no particular order.           
        """
        raise Exception("Should be implemented in a descendant of Matrix!")
            

    def isclose(self, other, delta):
        """ RETURN True if each cell in this matrix is within a delta distance
            from other Matrix. RETURN False if any cell couple differs more than delta.

            - if matrices have different dimensions, raise ValueError
        """
        raise Exception("Should be implemented in a descendant of Matrix!")
               
    def __eq__(self, other):                        
        raise Exception("Should be implemented in a descendant of Matrix!")

    def __add__(self, other):         
        raise Exception("Should be implemented in a descendant of Matrix!")
    
    def __mul__(self, other): 
        """ Implement ONLY multiplication by:
            - a scalar
            - a vector (of appropriate dimensions)!
               - notice vector can be on the right or on the left, with different dimensions !
        """  

        raise Exception("Should be implemented in a descendant of Matrix!")
        
    def __rmul__(self, other):
        """ Implement ONLY multiplication by:
            - a scalar
            - a vector (of appropriate dimensions)!
        """  
        raise Exception("Should be implemented in a descendant of Matrix!")

    

