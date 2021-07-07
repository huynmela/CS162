# Author: Melanie Huynh
# Date: 2/18/2021
# Description: This program is a LinkedList class which contains methods implmented
# recursively.

#================================NODE CLASS======================================
class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        """
        Initializes the node
        """
        self._data = data
        self._next = None

# GETTERS AND SETTERS FOR NODE -------------------------------------------------
    def get_data(self):
        """
        Returns the data of the node
        """
        return self._data

    def get_next(self):
        """
        Returns the next node
        """
        return self._next

    def set_data(self, val):
        """
        Sets val as data of the node
        """
        self._data = val

    def set_next(self, val):
        """
        Sets val as data of the next node
        """
        self._next = val
# ==============================LINKEDLIST CLASS=================================
class LinkedList:
    """
    Represents a LinkedList class
    """
    def __init__(self):
        """
        Initializes the linked list abstract data type
        """
        self._head = None
# GETTERS AND SETTERS ----------------------------------------------------------
    def get_head(self):
        """
        Returns the Node object that is at the _head of the linked list
        """
        return self._head

    def set_head(self, node):
        """
        Sets node object as the _head of the linked list
        """
        self._head = node

# ADD METHOD --------------------------------------------------------------------
    def helper_add(self, cur, val):
        """
        Helper function of the add method
        """
        # Base case
        if cur.get_next() is None: # Checks to see if the next node is none
            cur.set_next(Node(val)) # if so then add

        # Recursion
        else: # Otherwise, recursively check next node
            self.helper_add(cur.get_next(), val)

    def add(self, val):
        """
        Adds a node containing val from the linked list
        """
        if self._head is None: # Check if head node is none
            self._head = Node(val)

        else:
            self.helper_add(self._head, val)

# REMOVE METHOD ----------------------------------------------------------------
    def helper_remove(self, prev, current, val):
        """
        Helper function of the remove method
        """
        # Base case
        if current is None: # if the list is empty
            return

        if current.get_data() == val: #If the current node you are on contains val
            prev.set_next(current.get_next())

        # Recursion
        else:
            # iterate over your nodes recursively until you find the one you want then remove
            self.helper_remove(current, current.get_next(), val) # shift the nodes

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if val == self._head.get_data():
            self._head = self._head.get_next()
        else:
            self.helper_remove(self._head, self._head.get_next(), val)

# CONTAINS METHOD --------------------------------------------------------------
    def helper_contains(self, key, current):
        """
        Helper function of the contains method
        """
        if current.get_data() == key: # check if the current node contains the key
            return True

        if current.get_next() is None: # check if next node is None
            return False

        return self.helper_contains(key, current.get_next()) # otherwise, iterate to next node

    def contains(self, key):
        """
        Returns True if the list contains a Node with the value key, otherwise False
        """
        if self._head is None:
            return False
        else:
            return self.helper_contains(key, self._head)

# INSERT METHOD ----------------------------------------------------------------
    def helper_insert(self, val, pos, prev, cur):
        """
        Helper function of insert method
        """
        if pos == 0: # Once the head node has been reached
            new_node = Node(val)
            prev.set_next(new_node)
            new_node.set_next(cur)

        if cur is None: # check if the last node points to none
            new_node = Node(val)
            prev.set_next(new_node) # add it to the last node

        else:
            self.helper_insert(val, pos - 1, cur, cur.get_next())

    def insert(self, val, pos):
        """
        Inserts a node containing val into the linked list
        """
        if self._head is None: # If the list is empty
            self.add(val) # just add the val

        if pos == 0: # If the first position is at the head
            temp = self._head # Set a temporary variable for storing the head node
            self._head = Node(val) # redefine the head node as the value
            self._head.set_next(temp) # make the next node to the head the original head node

        else:
            self.helper_insert(val, pos - 1, self._head, self._head.get_next())

# REVERSE METHOD ----------------------------------------------------------------
    def helper_reverse(self, prev, cur):
        """
        Helper function of the reverse method
        """
        # Base case
        if cur is None:
            # If reached the end of the list
            self._head.set_next(None) # flip the end and head node
            self._head = prev
            return # exit recursion
        # Recursion
        # Otherwise, recurse and flip positions as you iterate through
        next_node = cur.get_next()
        cur.set_next(prev) # set the current node to the previous
        self.helper_reverse(cur, next_node)

    def reverse(self):
        """
        Reverses the linked list
        """
        if self._head is not None:
            self.helper_reverse(self._head, self._head.get_next())

# TO_PLAIN_LIST METHOD ---------------------------------------------------------
    def helper_to_plain_list(self, cur, a_list):
        """
        Helper function of the to_plain_list method
        """
        if cur is None:
            return a_list

        a_list.append(cur.get_data())

        return self.helper_to_plain_list(cur.get_next(), a_list)

    def to_plain_list(self):
        """
        Returns a regular Python list that has the same values
        """
        a_list = []
        if self._head is None: # If the list is empty
            return a_list # return an empty list

        else:
            return self.helper_to_plain_list(self._head, a_list)

# ADDITIONAL HELPFUL METHODS FOR TESTING ---------------------------------------
#    def display(a_list.add(

# TESTING
#a_list = LinkedList()
#a_list.add(1)
#a_list.add(2)
#a_list.add(3)
#a_list.add(4)
#a_list.add(5)

#a = a_list.to_plain_list()
#print(a)
