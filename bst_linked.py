"""
-------------------------------------------------------
bst_linked.py
Linked version of the BST ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-03-06"
-------------------------------------------------------
"""

from copy import deepcopy
from stack_array import Stack


class _BSTNode:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing a copy of value.
        Use: node = _BSTNode(value)
        -------------------------------------------------------
        Preconditions:
            value - data for the node (?)
        Postconditions:
            Initializes a BST node containing value. Child pointers are None,
            height is 1.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        return

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Postconditions:
            _height is 1 plus the maximum of the node's (up to) two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._data)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty bst.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - data to be inserted into the bst (?)
        Postconditions:
            returns
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of _data into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Preconditions:
            node - a bst node (_BSTNode)
            value - data to be inserted into the node (?)
        Postconditions:
            returns
            node - the current node (_BSTNode)
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BSTNode(value)
            self._count += 1
            inserted = True
        elif node._data > value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif node._data < value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot retrieve from an empty BST"

        node = self._root
        value = None

        while node is not None and value is None:

            if node._data > key:
                node = node._left
            elif node._data < key:
                node = node._right
            elif node._data == key:
                # for comparison counting
                value = deepcopy(node._data)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value matching key if found,
            otherwise returns None. Update structure of bst as required.
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot remove from an empty BST"

        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Preconditions:
            node - a bst node to search for key (_BSTNode)
            key - data to search for (?)
        Postconditions:
            returns
            node - the current node or its replacement (_BSTNode)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        
        
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._data:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._data:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._data
            # Replace this node with another node.
            if node._left is None:
                # node has no left child or has no children.

# your code here

            elif node._right is None:
                # node has no right child.

# your code here

            else:
                # Node has two children
                if node._left._right is None:
                    # left child is replacement node
                    repl_node = node._left
                else:
                    # find replacement node in right subtree of left node
                    repl_node = self._delete_node(
                        node._left, node._left._right)
                    repl_node._left = node._left

                repl_node._right = node._right
                node = repl_node
                node._update_height()

            self._count -= 1

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node(self, parent, child):
    
    
    """
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node(node, node._right)
        -------------------------------------------------------
        Preconditions:
            parent - node to search for largest value (_BSTNode)
            child - the right node of parent (_BSTNode)
        Postconditions:
            returns
            repl_node - the node that replaces the deleted node. This node 
            is the node with the maximum value in the deleted node's left
            subtree (_BSTNode)
        -------------------------------------------------------
        """
        
        
        """

# your code here

        # Recursively update all parent node heights
        parent._update_height()
        return repl_node
        """
    
    def identical(self, rs):
    
    
    
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another bst (BST)
        Postconditions:
            returns
            is_identical - True if this bst contains the same values
            in the same order as rs, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        
        
        
        
        if self._count != rs._count:
            is_identical = False
        else:
            is_identical = self._identical_aux(self._root, rs._root)
        return is_identical
        
        
        
        
    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Postconditions:
            returns
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        
        zero, one, two = self._node_counts_aux(self._root)
        return zero, one, two
    
    def preorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in preorder order.
        Use: bst.preorder()
        -------------------------------------------------------
        Postconditions:
            prints
            The contents of the tree are printed preorder.
        -------------------------------------------------------
        """
        node = self._root
        
        if node is not None:
            print(node._data)
            print("Left {}".format(node._left))
            print("Right {}".format(node._right))
            
    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        
        node = self._root
        
        while node._left is not None:
            node = node._left

        value = deepcopy(node._data)
        return value
    
    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        node = self._root

        while node._right is not None:
            node = node._right

        value = deepcopy(node._data)
        
        return value
    
    
    def _max_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the largest value in a BST node. (Recursive algorithm)
        Use: v = self._max_aux(node)
        ---------------------------------------------------------
        Preconditions:
            node - valid linked BST node (_BSTNode)
        Postconditions:
            returns
            value - a copy of the largest value in the node subtree (?)
        ---------------------------------------------------------
        """
        
        if node._right is None:
            value = deepcopy(node._data)
            
        else:
            value = self._max_aux(node._right)
            
        return value
    
    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        
        value = self._max_aux(self._root)
        
        return value
    
    def traverse(self):
        a = []
        self.traverse_aux(self._root,a)
        return a
    def traverse_aux(self,node,a):
        if node is not None:
            self.traverse_aux(node._left, a)
            a.append(node._data)
            self.traverse_aux(node._right, a)
        return
    
    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Postconditions:
            returns
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        balanced = False
        node = self._root
        if node._left != None:
            lh = node._left._height
        else:
            lh = 0
        if node._right!=None:
            rh = node._right._height
        else:
            rh = 0
        while node._right != None:
            if node == None:
                balanced = True
            elif abs(lh-rh)>1:
                balanced = False
            elif abs(lh-rh)==1:
                balanced = True
            node = node._right
        return balanced
    
    def is_valid(self):
        
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Postconditions:
            returns
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        valid = False
        node = self._root
        lh = node._left._height
        rh = node._right._height
        if node._left != None:
            lh = node._left._height
        else:
            lh = 0
        if node._right!=None:
            rh = node._right._height
        else:
            rh = 0
        while node._right != None:
            if node == None:
                valid = True
            elif lh != None and lh<node._height:
                valid = True
            elif rh != None and rh>node._height:
                valid = True
            node = node._right
        return valid
    
    def mirror(self):
        """
        ---------------------------------------------------------
        Creates a mirror version of a BST. All nodes are swapped with nodes on
        the other side the tree. Nodes may take the place of an empty spot.
        The resulting tree is a mirror image of the original tree. (Note that
        the mirrored BST is no longer a BST itself.) The original BST is unchanged.
        Use: tree = bst.mirror()
        ---------------------------------------------------------
        Postconditions:
            returns
            tree - a mirror version of bst.
        ---------------------------------------------------------
        """
        node = self._root
        while node._left!=None:
            node._left, node._right = node._right,node._left
            node = node._left
