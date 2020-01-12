"""
-------------------------------------------------------
stack_array.py
Array version of the Stack ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-02-02"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a list.
        Use: s = Stack()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty stack.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns True if the stack is empty, False otherwise.
        -------------------------------------------------------
        """

        if len(self._values) == 0:
            b = True
        else:
            b = False
        return b

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto stack.
        Use: s.push(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the top of the stack.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack.
        Use: value = s.pop()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the top of the stack - the value is
                removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"

        value = self._values.pop()

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        Use: value = s.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the top of the stack -
                the value is not removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        value = deepcopy(self._values[-1])

        return value
    
    
    def split(self):
        """
        -------------------------------------------------------
        Splits the current stack into separate stacks. Current stack 
        is empty when operation is done.
        Use: s2, s3 = s.split()
        -------------------------------------------------------
        Postconditions:
            returns
            s2 - contains alternating values from current stack (Stack)
            s3 - contains other alternating values from current stack (Stack)
        -------------------------------------------------------
        """
        
        
        s2=[]
        s3=[]
        
        while (self.is_empty()==False):
            
            s2.append(self._values.pop())
            if(self.is_empty()==False):
                
                
            
                s3.append(self._values.pop())
            
        return s2,s3