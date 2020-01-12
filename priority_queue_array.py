"""
-------------------------------------------------------
priority_queue_array.py
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-01-23"
-------------------------------------------------------
"""
from copy import deepcopy


class PriorityQueue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty priority queue.
        -------------------------------------------------------
        """
        self._values = []
        self._first = None
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the priority queue.
        Use: pq.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the priority queue.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        if self._first == None:
            self._first=0
            
            
        elif value<self._values[self._first]: 
            self._first = len(self._values)-1

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the priority queue.
        Use: v = pq.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the highest priority value in the priority queue -
            the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"
        
        value = self._values.pop(self._first)
        
        i = 0
        
        self._first = 0
        while i < len(self._values):
            if self._values[self._first]>self._values[i]:
                self._first = i
            
            i+=1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the highest priority value in the priority queue -
            the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"
        
        value = deepcopy(self._values[self._first])
        return value
    
    def combine(self, pq2):
        """
        -------------------------------------------------------
        Combines contents of two priority queues into a new 
        priority queue.
        Use: pq3 = pq1.combine(pq2)
        -------------------------------------------------------
        Preconditions:
            q2 - an array-based queue (PriorityQueue)
        Postconditions:
            returns
            pq3 - Contents of self and q2 are moved 
                into pq3 (PriorityQueue)
        -------------------------------------------------------
        """
        pq3 = PriorityQueue()
        
        
        while pq2.is_empty()==False:
            pq3.insert(pq2.remove())
            while self.is_empty()==False:
                pq3.insert(self.remove())
                
        return pq3