"""
-------------------------------------------------------
dequeue_array.py
Array version of the Dequeue ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-03-03"
-------------------------------------------------------
"""
from copy import deepcopy


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
        self._values = []
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
        return len(self._values) == 0

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
        return len(self._values)

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

        self._values.insert(0, value)

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

        self._values.append(deepcopy(value))

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
        assert len(self._values) > 0, "Cannot remove from an empty dequeue"

        value = self._values.pop(0)

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
        assert len(self._values) > 0, "Cannot remove from an empty dequeue"

        value = self._values.pop(-1)

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
        assert len(self._values) > 0, "Cannot peek at an empty dequeue"

        value = deepcopy(self._values[0])

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
        assert len(self._values) > 0, "Cannot peek at an empty dequeue"

        value = deepcopy(self._values[-1])

        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the dequeue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the dequeue (?)
        -------------------------------------------------------
        """
        i = 0

        while i < len(self._values):
            yield self._values[i]
            i += 1