"""
-------------------------------------------------------
sorted_list_linked.py
Linked Version of The Sorted List ADT
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-02-13"
-------------------------------------------------------
"""
from copy import deepcopy


class _SLNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SLNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            next_ - another sorted list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return


class SortedList:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty sorted list.
        Use: sl = SortedList()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty sorted list.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

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
        return self._count

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
        previous = None
        current = self._front
        if current is None:
            self._front = _SLNode(value, self._front)
        #spot = current._data < current._next.data
        while current is not None and value >= current._data:
            previous = current
            current = current._next
        if previous is None:
            self._front = _SLNode(value, self._front)
        else:
            previous._next = _SLNode(value, current)
        self._count += 1
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        index = 0
        previous = None
        current = self._front

        while current is not None and current._data != key:
            index += 1
            previous = current
            current = current._next

        if current is None:
            current = None
            previous = None
            index = -1
        return previous, current, index

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
        assert self._front is not None, "Cannot remove from an empty list"

        p, c, i = self._linear_search(key)

        if i == -1:
            value = None
        # found in first node
        elif p is None:
            value = deepcopy(self._front._data)
            # removes front
            self._front = self._front._next
            self._count -= 1
        else:
            value = deepcopy(c._data)
            # removes link from previous to current, thus removing current
            p._next = c._next
            self._count -= 1

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
        assert self._front is not None, "Cannot find in an empty list"

        p, c, i = self._linear_search(key)

        if c is not None:
            value = deepcopy(c._data)
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
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._data)

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """

        p, c, i = self._linear_search(key)

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
        n = self._count
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

        current = self._front

        if i < 0:
            # negative index - convert to positive
            i = self._count + i
        j = 0

        while j < i:
            current = current._next
            j += 1

        value = deepcopy(current._data)

        return value

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
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """

        p, c, i = self._linear_search(key)
        current = c
        return i != -1

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
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        value = self._front._data
        while current._next is not None:
            if current._data>value:
                value = current._data
            current = current._next

        value = deepcopy(current._data)

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
        assert self._front is not None, "Cannot find minimum of an empty list"

        current = self._front
        value = self._front._data
        while current != None:
            if current._data<value:
                value = current._data
            current = current._next

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

        number = 0
        current = self._front

        while current is not None:
            if current._data == key:
                number += 1
            current = current._next

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
        front = self._front._data
        current = self._front

        while current._next is not None:
            if current._next._data == front:
                current._next = current._next._next
                self._count-=1
            else:
                current = current._next
                front = current._data

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list.
        Use: l.clean_r()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        return self.clean_r_aux(self._front._data, self._front)

    def clean_r_aux(self, front, current):
        if current._next:
            if current._next._data == front:
                current._next = current._next._next
            else:
                current = current._next
                front = current._data
            front, current = self.clean_r_aux(front, current)
        return front, current

    def pop(self, *i):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.remove(i)
        -------------------------------------------------------
        Preconditions:
            i - an array of arguments (?)
                i[0], if it exists, is the index
        Postconditions:
            returns
            value - if i exists, the value at position i, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(i) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                i[0] = self._count + i[0]
            j = 0

            while j < i[0]:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._data

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (SortedList)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (SortedList)
        -------------------------------------------------------
        """

        new_list = SortedList()
        temp = rs._front

        while temp is not None:
            _, current, _ = self._linear_search(temp._data)

            if current is not None:
                # Value exists in both lists.
                _, current, _ = new_list._linear_search(temp._data)

                if current is None:
                    # Value does not appear in new list.
                    new_list.insert(temp._data)

            temp = temp._next
        return new_list

    def union(self, rs):
        """
        -------------------------------------------------------
        Copies all of the values in both self and rs to
        a new List. Each value appears only once. (iterative)
        -------------------------------------------------------
        Preconditions:
            rs - another List (SortedList)
        Postconditions:
            Returns:
            new_list - a List containing one copy each of all values
            in both self and rs. (SortedList)
        -------------------------------------------------------
        """
        current = self._front
        current2 = rs._front
        a1 = []
        a2 = []
        new_list = SortedList()
        new = []
        while current is not None:
            a1.append(current._data)
            current = current._next
        while current2 is not None:
            a2.append(current2._data)
            current2 = current2._next
        temp = a1 + a2
        x = 0
        while(x < len(temp)):
            if (temp[x] not in new):
                new.append(temp[x])
            x += 1
        while (new):
            new_list.insert(new.pop(0))  # change this nigga
        return new_list

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes first node in list.
        Use: value = sl.remove_front()
        -------------------------------------------------------
        Postconditions:
          Returns:
          value - the first value in the list, None if the list is empty.
        -------------------------------------------------------
        """

        value = self._front._data
        self._front = self._front._next
        return value

    def _reverse(self):
        """
        -------------------------------------------------------
        Helper method - reverses the order of the elements in list.
        Use: l._reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        new_front = None

        while self._front is not None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = temp

        self._front = new_front
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next
