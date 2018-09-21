def swap(A, i, j):
    """
    In the array A, swaps the elements at position i and j.
    """
    
    #jupman-raise
    
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
    #/jupman-raise

    # if you are a Python ninja, you might prefer this very concise version:
    # A[i], A[j] = A[j], A[i]  

    

def argmin(A, i):
    """
    Return the index of the element in list A which is lesser or equal than all other elements in A 
    that start from index i included
    """
    
    #jupman-raise    
    
    minpos = i
    
    for j in range(i+1, len(A)):
        if (A[j] < A[minpos]):
            minpos = j 
    return minpos
    
    #/jupman-raise
    
    
def selection_sort(A):
    """
    Sorts the list A in-place in O(n^2) time this ways:
        1. Looks at minimal element in the array [i:n], and swaps it with first element.
        2. Repeats step 1, but considering the subarray [i+1:n]
    """
    #jupman-raise    
    
    for i in range(0, len(A)-1):
        m = argmin(A, i)
        swap(A, i, m)
    
    #/jupman-raise