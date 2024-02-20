#!/usr/bin/python3
"""____MODULE____"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes name contain
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        # If attrs is not provided or is an empty list, retrieve all attributes
        if attrs is None or not attrs:
            return self.__dict__

        # If attrs is a list of strings, retrieve only the specified attributes
        filtered_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_attrs[attr] = getattr(self, attr)
        return filtered_attrs

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on
        the provided dictionary.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
