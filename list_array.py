"""
-------------------------------------------------------
list_array.py
Array version of the list ADT.
-------------------------------------------------------
Author: Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-01-31"
-------------------------------------------------------
"""
from copy import deepcopy


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty list.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the list at index i.
        Use: l.insert(i, value)
        -------------------------------------------------------
        Preconditions:
            i - index value (int)
            value - a data element (?)
        Postconditions:
            a copy of value is added to index i, all other values are pushed right
            If i outside of range of length of list, appended to end
        -------------------------------------------------------
        """
        self._values.insert(i,value)

        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """
        i = 0
        found = False
        while found == False:
            if len(self._values)> i and self._values[i] == key:
                found = True
            i+=1
        if found == False:
            i = -1
        return i-1
    
    def _linear_search_r(self,key):
        i=0
        i = self._linear_search_r_aux(key,i)
        return i
    
    def _linear_search_r_aux(self,key,i): 
        if len(self._values) <= i:
            i = -1
        elif self._values[i] != key:
            i = self._linear_search_r_aux(key, i+1)
        return i

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: value = l.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty list"
        i = self._linear_search(key)
        if i == -1:
            value = None
        else:
            value = self._values.pop(i)

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        i = self._linear_search(key)
        if i == -1:
            value = None
        else:
            value = deepcopy(self._values[i])

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty list"

        value = deepcopy(self._values[0])
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list. Finds the first occurence of key in the list
        Use: n = l.index(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
              key is not in the list. (int)
        -------------------------------------------------------
        """

        i = self._linear_search(key)
        
        
        return i

    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Preconditions:
            i - an index value (int)
        Postconditions:
            returns
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
        Postconditions:
            returns
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._valid_index(i), "Invalid index value"

        value = deepcopy(self._values[i])

        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
            value - a data value (?)
        Postconditions:
            The i-th element of list contains a copy of value. The existing
                value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._valid_index(i), "Invalid index value"

        self._values.insert(i,deepcopy(value))

        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = 0
        b = False
        while b == False:
            if key[i] in self._values:
                b = True
            i+=1
        
        return i > -1


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = l.max()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find maximum of an empty list"

        i = 1
        n = len(self._values)
        value = self._values[0]
        while i < n:
            if value>self._values[i]:
                value = self._values[i]
            i+=1

        return deepcopy(value)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = l.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find minimum of an empty list"

        i = 1
        n = len(self._values)
        value = self._values[0]
        while i > n:
            if value>self._values[i]:
                value = self._values[i]
            i+=1

        return value


    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = l.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number = -1
        n = len(self._values)
        i = 0
        while i < n:
            if key == self._values[i]:
                number+=1
            i+=1

        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the operation was called.
        -------------------------------------------------------
        """

        i = 0
        while i < len(self._values):
            new_val = self._values[-1]
            self.insert(0, new_val)
            new_val = self._values[-1]
            self.remove(new_val)
            i+=1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Appends a copy of value to the end of the list.
        Use: l.append(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the end of the list.
        -------------------------------------------------------
        """

        self._values.append(deepcopy(value))

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list.
        Use: l.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        i = 1 
        front = self._values[0]
        while i<len(self._values):
            if self._values[i]==front:
                self.remove(self._values[i])
            else:
                i+=1

        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.pop()
        Use: value = l.pop(i)
        -------------------------------------------------------
        Preconditions:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Postconditions:
            returns
            value - if args exists, the value at position args[0], otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value