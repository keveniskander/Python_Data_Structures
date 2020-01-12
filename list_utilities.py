def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    Use: list_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of List are tested for both empty and 
        non-empty lists using the data in a:
        is_empty, insert, remove, append, index, __contains__,
        find, max, min, __getitem__, __setitem__
    -------------------------------------------------------
    """
    from list_array import List
    l = List()
    print(l.is_empty())
    l.insert(0,a[0])
    print(l[0])
    print(l.is_empty())
    

    return