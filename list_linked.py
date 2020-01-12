"""
-------------------------------------------------------
list_linked.py
Linked version of the list ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-02-13"
-------------------------------------------------------
"""
from copy import deepcopy


class _ListNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node.
        Use: node = _ListNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            _data - data value for node (?)
            _next - another list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return


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
            returns
            True if the list is empty, False otherwise.
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
            returns
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

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
        if i < 0:
            # negative index
            i = self._count + i

        n = 0
        previous = None
        current = self._front

        while n < i and current is not None:
            # find the proper location in the list
            previous = current
            current = current._next
            n += 1

        if previous is None:
            # Insert a new node into the front of the list.
            self._front = _ListNode(value, self._front)
        else:
            # Insert a new node elsewhere in the list
            previous._next = _ListNode(value, current)
        self._count += 1
        return

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the list.
        Use: l.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element. (?)
        Postconditions:
            value is added to the front of the list.
        -------------------------------------------------------
        """
        self.insert(0, value)
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        Use: p, c, i = self._linear_search(key)
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
        current = self._front
        previous = None
        
        while current!=None and current._data!=key:
            index += 1
            previous = current
            current = current._next
            
        if current == None:
            index = -1
       

        return previous, current, index
    
    def _linear_search_r(self,key):
        index = 0
        current = self._front
        previous = None
        index = self._linear_search_r_aux(key,index,current,previous)
        return index,current,previous
        
    def _linear_search_r_aux(self,key,index,current,previous):
        if current == None:
            index = -1
        elif current._data != key:
            index = self._linear_search_r_aux(key,index+1,current._next, current)
            
        return index
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
        assert self._front is not None, "Cannot remove from an empty list"
        
        p, c, i = self._linear_search(key)
        current = c
        previous = p
        if current == None:
            value = None
        elif previous == None:
            self._front = current._next
            value = current._data
        else:
            value = current._data
            previous._next = current._next
        
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._data
        self._front = self._front._next
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            Removes all values matching key.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

# your code here

        return

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

        current = self._front
        found = False
        while found == False:
            if current == None:
                value = None
                found = True
            elif current._data == key:
                found = True
                value = current._data
            else:
                current = current._next
                
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

        value = self._front._data

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index(key)
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
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
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

        current._data = deepcopy(value)
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
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        p, current, i = self._linear_search(key)
       

        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = l.max()
        -------------------------------------------------------
        Postconditions:
            returns
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        max_data = self._front._data
        current = self._front
        while current != None:
            if current._data>max_data:
                max_data = current._data
            current = current._next
            
        

        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = l.min()
        -------------------------------------------------------
        Postconditions:
            returns
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        min_data = self._front._data
        current = self._front
        while current != None:
            if current._data<min_data:
                min_data = current._data
            current = current._next

        return min_data

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

        number = 0
        current = self._front
        while current!= None:
            if current._data == key:
                number+=1
            current = current._next

        return number

    def append(self, value):
        """
        ---------------------------------------------------------
        Appends a copy of value to the end of the List.
        Use: l.append(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the end of the List.
        -------------------------------------------------------
        """

        current = self._front
        previous = None
        while current is not None:
            # find the proper location in the list
            previous = current
            current = current._next

        if previous is None:
            # Insert a new node into the front of the list.
            self._front = _ListNode(value, self._front)
        else:
            # Insert a new node elsewhere in the list
            previous._next = _ListNode(value, current)
        self._count += 1

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (iterative algorithm)
        Use: l.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        front = self._front._data
        current = self._front
        
        while current._next != None:
            
            if current._next._data == front:
                current._next = current._next._next
                
            else:
                current = current._next
                front = current._data
    
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
        
    def clean_r_aux(self,front,current):
        
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
    
    
    def identical(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        Use: b = l.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            is_identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != rs._count:
            is_identical = False
        else:
            current1 = self._front
            current2 = rs._front

            while current1 is not None and current1._data == current2._data:
                current1 = current1._next
                current2 = current2._next

            is_identical = current1 is None
        return is_identical
    
    def identical_r(self,rs):
        current1 = self._front
        current2 = rs._front
        is_identical = self.identical_r_aux(current1,current2)
        return is_identical
    
    def identical_r_aux(self,current1,current2):
        if current1 == None:
            is_identical = True
        elif current1._data!=current2._data:
            is_identical = False
        elif current1 != None and current1._data == current2._data:
            is_identical = self.identical_r_aux(current1._next,current2._next)
        return is_identical
    
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        Use: l.reverse()
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
    
    def reverse_r(self):
        temp = None
        new_front = None
        self.reverse_r_aux(new_front,temp)
        return reversed
    
    def reverse_r_aux(self,new_front,temp):
        if self._front == None:
            self._front = new_front
        elif self._front!=None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = temp
            self.reverse_r_aux(new_front,temp)
        return
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant.
        -------------------------------------------------------
        Postconditions:
            returns
            even - the even indexed elements of the list (List)
            odd - the odd indexed elements of the list (List)
            The list is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()

        while self._front is not None:
            new_node = self._front
            self._front = self._front._next
            new_node._next = even._front
            even._front = new_node

            if self._front is not None:
                new_node = self._front
                self._front = self._front._next
                new_node._next = odd._front
                odd._front = new_node

        odd._count = self._count // 2
        even._count = self._count - odd._count
        self._count = 0
        return even, odd
    
    def split_alt_r(self):
        even = List()
        odd = List()
        even, odd = self.split_alt_r_aux(even, odd)
        odd._count = self._count // 2
        even._count = self._count - odd._count
        self._count = 0
        return even,odd
        
    def split_alt_r_aux(self,even,odd):
        if self._front != None:
            new_node = self._front
            self._front = self._front._next
            new_node._next = even._front
            even._front = new_node
            
            even, odd =self.split_alt_r_aux(odd, even)
        return even,odd
    
    def intersection(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (List)
        -------------------------------------------------------
        """
        new_list = List()
        temp = rs._front

        while temp is not None:
            _, current, _ = self._linear_search(temp._data)

            if current is not None:
                # Value exists in both lists.
                _, current, _ = new_list._linear_search(temp._data)

                if current is None:
                    # Value does not appear in new list.
                    new_list.insert(0, temp._data)

            temp = temp._next
        return new_list
    
    