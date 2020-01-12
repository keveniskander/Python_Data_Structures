def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    from queue_array import Queue
    q = Queue()
    
    q.insert(a[1])
    q.peek()
    print(q.peek())
    print(q.remove())

    return