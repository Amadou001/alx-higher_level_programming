#!/usr/bin/python3
"""Module that defines a node"""

class Node:
    """Class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Constructor for Node class
        
        Args:
            data: Data to be stored in the node
            next_node: Reference to the next node in the list (default is None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property getter for data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter for data attribute
        
        Args:
            value: New value to be set for data attribute
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Property getter for next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter for next_node attribute
        
        Args:
            value: New value to be set for next_node attribute
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """Constructor for SinglyLinkedList class"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list (increasing order)
        
        Args:
            value: Value to be inserted into the list
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list"""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
