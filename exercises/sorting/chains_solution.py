

def has_duplicates(external_list):
    """
        Returns True if internal lists inside external_list contain duplicates, 
        False otherwise. For more info see exam and tests.

        INPUT: a list of list of strings, possibily containing repetitions, like:

            [
                ['ab', 'c', 'de'],
                ['v', 'a'],
                ['c', 'de', 'b']
            ]

        OUTPUT: Boolean  (in the example above it would be True)

    """
    #jupman-raise
    found = set()
    for internal_list in external_list:
        for s in internal_list:
            if s in found:
                return True
            else:
                found.add(s)
    return False
    #/jupman-raise

def chain(external_list):
    """
        Takes a list of list of strings and return a list containing all the strings 
        from external_list in sequence, joined by the ending and starting strings
        of the internal lists. For more info see exam and tests.

        INPUT: a list of list of strings , like:

                [
                    ['ab', 'c', 'de'],
                    ['gh', 'i'],
                    ['de', 'f', 'gh']
                ]
                
        OUTPUT: a list of strings, like   ['ab', 'c', 'de', 'f', 'gh', 'i']


    """
    #jupman-raise
    # First maps starting strings to the list where they are contained

    import itertools
    ds = dict()

    for internal_list in external_list:
        if internal_list[0] not in ds:            
            ds[internal_list[0]] = internal_list
    
    ret = []

    ret.extend(external_list[0])
    
    for i in range(len(external_list) - 1):
        if ret[-1] in ds:            
            complete_list = ds[ret[-1]]
            ret.extend(itertools.islice(complete_list, 1, None))
        else:
            raise ValueError("Couldn't find any list starting with %s " % ret[-1])
    return ret
    #/jupman-raise


