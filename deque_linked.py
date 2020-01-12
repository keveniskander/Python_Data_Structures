"""
-------------------------------------------------------
deque_linked.py
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-03-03"
-------------------------------------------------------
"""
from copy import deepcopy


class _DequeNode:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _dequeNode(value, prev, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            _prev - another deque node (_DequeNode)
            _next - another deque node (_DequeNode)
        Postconditions:
            Initializes a deque node that contains a copy of value
            and links to the previous and next nodes in the deque.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._prev = _prev
        self._next = _next
        return


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty deque.
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = d.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(d)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the deque.
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: d.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the front of the deque.
        -------------------------------------------------------
        """

        self._front = _DequeNode(value, _prev=self._front,_next=self._front)
        if self._count > 0:
            self._front._prev._next = self._front
        else: 
            self._rear = self._front

        self._count += 1
        

        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: d.insert_rear(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the deque.
        -------------------------------------------------------
        """
        
        self._rear = _DequeNode(value, _next=self._rear,_prev=self._rear)
        if self._count > 0:
            self._rear._next._prev = self._rear
        else:
            self._front = self._rear
        self._count += 1

        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = d.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of deque - the value is
                removed from deque.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty dequeue"

        value = self._front
        
        self._front = self._front._prev
        self._count -= 1
        if self._count == 0:
            self._front = None

        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = d.remove_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the rear of deque - the value is
                removed from deque.
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty dequeue"

        value = self._rear
        self._count -= 1

        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = d.peek_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of deque -
                the value is not removed from deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty dequeue"

        value = deepcopy(self._front)

        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = d.peek_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the rear of deque -
                the value is not removed from deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty dequeue"

        value = deepcopy(self._rear)

        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two pointers.
        Use: r, l = self._swap(self, l, r):
        -------------------------------------------------------
        Preconditions:
            l - a pointer to a deque node (_DequeNode)
            r - a pointer to a deque node (_DequeNode)
        Postconditions:
            returns
            l - a pointer to a deque node (_DequeNode)
            r - a pointer to a deque node (_DequeNode)
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        # your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the dequeue
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the dequeue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next