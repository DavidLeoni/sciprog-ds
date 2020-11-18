DEBUG=True

import math 

# call this like if it were a print
def debug(*args):
    if DEBUG:
        print(*args)
        
def distance(features1, features2):
    """ Takes two lists, each having m features as floats
        and RETURN  a float which is the vector distance among 
        the two features
        
        - MUST RUN IN O(m) WHERE m IS THE NUMBER OF FEATURES       
    """
    raise Exception('TODO IMPLEMENT ME !')    
    
def lineup(waiting_room, description):
    """ RETURN a NEW list of the criminals names sorted by similarity distance with description, 
               from most distant to least distant
        PRINT all the passages 
        MODIFY waiting_room so it's empty at the end        
    """
    raise Exception('TODO IMPLEMENT ME !')

    
def mcfats(clients):    
    """ RETURN a NEW sorted list with the client weights, from smallest to greatest
        PRINT all the passages 
        DO *NOT* MODIFY clients list
    """
    
    raise Exception('TODO IMPLEMENT ME !')
    

def partitocracy(people, level=0):
    """Takes a list of integers and:
    
       RETURN a partitocracy as a NEW list of nested lists    
       PRINT the process, starting each line  with a number 
             of spaces proportional to recursion level parameter       
    
       - DO NOT modify the input list.
       - a recursive implementation is acceptable
    """
    raise Exception('TODO IMPLEMENT ME !')


