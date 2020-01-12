"""
-------------------------------------------------------
stack_utilities.py
.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-01-16"
-------------------------------------------------------
"""
from stack_array import Stack

def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of a onto s.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        The contents of a are moved into s, a is empty.
    -------------------------------------------------------
    """
    
    while 0 < len(a):
        value = a.pop()
        s.push(value)
        
    
def stack_to_array(s, a):
    """
    -------------------------------------------------------
    Pops contents of s into a.
    Use: stack_to_array(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        Contents of s are moved into a, s is empty.
    -------------------------------------------------------
    """
    
    while s.is_empty()==False:
        value = s.pop()
        a.append(value)
    
def stack_test(a):
    """
    -------------------------------------------------------
    Tests 
    Use: stack_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Stack are tested for both empty and 
        non-empty stacks using the data in a:
        is_empty, push, pop, peek
    -------------------------------------------------------
    """
    s = Stack()
    print("Empty:",s.is_empty())
    array_to_stack(s, a)
    print(s.peek())
    print(s.pop())
    print("Empty:",s.is_empty())
    stack_to_array(s,a)

    return 