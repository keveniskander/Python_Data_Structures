"""
-------------------------------------------------------
sorted_list_array.py
Array version of the SortedList ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-02-24"
-------------------------------------------------------
"""
from copy import deepcopy


class SortedList:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty SortedList.
        Use: sl = SortedList()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty sorted list.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the sorted list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the sorted list is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the sorted list.
        Use: n = len(sl)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the sorted list.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = len(self._values) - 1

        while low <= high:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if self._values[mid] > value:
                # search the left subarray.
                high = mid - 1
            else:
                # Default: search the right subarray.
                low = mid + 1
        self._values.insert(low, value)
        return

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = len(self._values) - 1

        while low < high:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if self._values[mid] < key:
                # Search the right subarray.
                low = mid + 1
            else:
                # Default: search the left subarray.
                high = mid

        # Deferred test for equality.
        if low == high and self._values[low] == key:
            i = low
        else:
            i = -1
        return i

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        if key in self._values:
            value = self._values.pop(self._binary_search(key))
        else:
            value = None

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find in an empty list"

        if key in self._values:
            value = deepcopy(self._values[self._binary_search(key)])
        else:
            value = None

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
        Finds the location of the first occurrence of key in the sorted list.
        Use: n = sl.index( key )
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns
            i - the location of the full value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """

        i = self._binary_search(key)

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
        Returns a copy of the nth element of the sorted list.
        Use: value = sl[i]
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
        Postconditions:
            returns
            value - the i-th element of the sorted list (?)
        -------------------------------------------------------
        """
        assert self._valid_index(i), "Invalid index value"

        value = deepcopy(self._values[self._binary_search(i)])

        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the sorted list contains key.
        Use: b = key in sl
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            True if the sorted list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """

        if key in self._values:
            i = True
        else:
            i = False

        return i > -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find maximum of an empty list"

        i=0
        value = self._values[0]
        while i < len(self._values):
            if self._values[i]>value:
                value = deepcopy(self._values[i])
            i+=1

        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the sorted list (?)
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
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns
            number - the number of times key appears in the sorted list (int)
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

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        set(self._values)

        return

    def intersection(self, rs):
        """
        -------------------------------------------------------
        Returns a list that contains only values that appear in both
        the current List and rs.
        Use: new_list = sl.intersection(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another sorted list (SortedList)
        Postconditions:
            returns
            new_list - A new list that contains only the values found in both the current
                sorted list and second. Values do not repeat (SortedList)
        -------------------------------------------------------
        """
        new_list = SortedList()
        i=0
        if rs>self._values:
            while i<rs:
                if self._values[i]==rs[i]:
                    new_list.insert(rs[i])
        else:
            while i<self._values:
                if self._values[i]==rs[i]:
                    new_list.insert(rs[i])

        return new_list

    def union(self, rs):
        """
        -------------------------------------------------------
        Returns a list that contains all values in both
        the current sorted list and rs.
        Use: new_list = sl.union(rs)
        -------------------------------------------------------
        Preconditions:
            second - another sorted list (SortedList)
        Postconditions:
            returns
            new_list - A new list that contains all values found in both the current
                sorted list and second. Values do not repeat (SortedList)
        -------------------------------------------------------
        """
        new_list = SortedList()

        

        return new_list

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