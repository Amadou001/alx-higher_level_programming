#!/usr/bin/python3
"""Module that defines a node"""


class Node:
    """Class that defines a node"""

    def __init__(self, data, next_node=None):
        """Constructor

            Args:
                data (int): data of the node
                next_node (Node): optional
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Function that retrieves the private instance __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Function that defines the value of the private instance __data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Function that retrieves the private instance __next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Function that defines a new node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """Constructor function"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted\
        position in the list (increasing order)"""
        new_node = Node(value)
        if self.__head is None or value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None\
                    and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
