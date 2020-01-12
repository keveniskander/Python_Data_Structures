"""
-------------------------------------------------------
queue_array.py
Array version of the Queue ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-01-23"
-------------------------------------------------------
"""
from copy import deepcopy


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty queue.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = q.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = q.is_full()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: q.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the queue.
        -------------------------------------------------------
        """

        self._values.append(deepcopy(value))

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = q.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of the queue - the value is
            removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        
        value = self._values.pop(0)
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = q.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of the queue -
            the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[0])

        return value
    
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in a queue.
        Use: q.reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of q are reversed in order with respect
            to their order before the operation was called.
        -------------------------------------------------------
        """
        
        from stack_array import Stack
        s = Stack()
        while len(self._values)>0:
            s.push(self._values[0])
            self.remove()
        while s.is_empty()==False:
            self.insert(s.pop())