"""
-------------------------------------------------------
stack_linked.py
Linked version of the Stack ADT.
-------------------------------------------------------
Author:       Keven
ID:           160634540
Email:        iska4540@mylaurier.ca
__updated__ = "2017-02-13"
-------------------------------------------------------
"""
from copy import deepcopy


class _StackNode:

    def __init__(self, data, next_):
        """
        -------------------------------------------------------
        Initializes a stack node.
        Use: node = _StackNode(data, _next)
        -------------------------------------------------------
        Preconditions:
            data - data for node (?)
            next_ - another stack node (_StackNode)
        Postconditions:
            Initializes a stack node that contains a copy of data
            and a link to the next node in the stack.
        -------------------------------------------------------
        """
        self._data = deepcopy(data)
        self._next = next_
        return


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a linked structure.
        Use: s = Stack()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty stack.
        -------------------------------------------------------
        """
        self._top = None
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the stack is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._top is None

    def push(self, data):
        """
        -------------------------------------------------------
        Pushes a copy of data onto stack.
        Use: s.push(data)
        -------------------------------------------------------
        Preconditions:
            data - a data element (?)
        Postconditions:
            a copy of data is added to the top of the stack.
        -------------------------------------------------------
        """
        self._top = _StackNode(data, self._top)
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack.
        Use: data = s.pop()
        -------------------------------------------------------
        Postconditions:
            returns
            data - the data at the top of the stack - the data is
                removed from the stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot pop from an empty stack"

        data = self._top._data
        self._top = self._top._next
        return data

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        Use: value = s.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            data - a copy of the data at the top of the stack -
                the data is not removed from the stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, \
            "Cannot peek at an empty stack"

        data = deepcopy(self._top._data)
        return data