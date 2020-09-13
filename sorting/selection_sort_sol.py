def swap(A, i, j):
    """ MODIFIES the array A by swapping the elements at position i and j
    """
    #jupman-raise
    
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

    # if you are a Python ninja, you might prefer this very concise version:
    # A[i], A[j] = A[j], A[i]  

    #/jupman-raise

    

def argmin(A, i):
    """ RETURN the *index* of the element in list A which is lesser than or equal
        to all other elements in A that start from index i included
    
        - MUST execute in O(n) where n is the length of A
    """

    
    #jupman-raise    
    
    minpos = i
    
    for j in range(i+1, len(A)):
        if (A[j] < A[minpos]):
            minpos = j 
    return minpos
    
    #/jupman-raise
    
    
def selection_sort(A):
    """ Sorts the list A in-place in O(n^2) time this ways:
        1. Looks at minimal element in the array [i:n],
           and swaps it with first element.
        2. Repeats step 1, but considering the subarray [i+1:n]
        
        Remember selection sort has complexity O(n^2) where n is the 
        size of the list.
    """
    #jupman-raise    
    
    for i in range(0, len(A)-1):
        m = argmin(A, i)
        swap(A, i, m)
    
    #/jupman-raise