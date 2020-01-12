"""
-------------------------------------------------------
test_sorts_array.py
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-03-21"
-------------------------------------------------------
"""
# Imports
import random
from number import Number
from sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Create a sorted list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        values - a sorted list of SIZE Number objects.
    -------------------------------------------------------
    """
    values = []
    for i in range(100):
        values.insert(-1,Number(i))
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        values - a reversed list of SIZE Number objects.
    -------------------------------------------------------
    """
    
    values = []
    for i in range(100,0,-1):
        values.append(Number(i))
    
    return values 


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE.
    -------------------------------------------------------
    """
    from random import randint

    arrays = []
    for i in range(100):
        x = randint(1,XRANGE)
        arrays.insert(0,Number(x))

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and print out
    its comparisons for sorted, reversed, and random arrays
    of data.
    -------------------------------------------------------
    Preconditions:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Postconditions:
        prints the number of comparisons necessary to sort an
        array: in order, in reverse order, and a list of arrays
        in random order.
    -------------------------------------------------------
    """

    create_sorted()
    create_reversed()
    create_randoms()
    
       
    print("Sort with {}".format(title))
    func(create_sorted())
    print("Sorted comparisons: {}".format(Number.comparisons))
    Number.comparisons = 0
    func(create_reversed())
    print("Reversed comparisons: {}".format(Number.comparisons))
    Number.comparisons = 0
    func(create_randoms()[0])
    print("Random comparisons: {}".format(Number.comparisons))
    Number.comparisons = 0
    return