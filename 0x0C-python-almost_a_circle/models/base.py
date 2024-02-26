#!/usr/bin/python3
"""Base Module"""


import json
import os


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
            Args:
                id(integer, optional).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        cls_name = cls.__name__
        file_name = f"{cls_name}.json"
        json_string = cls.to_json_string(
            [list_obj.to_dictionary() for list_obj in list_objs])

        with open(file_name, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(2, 3)
        elif cls.__name__ == "Square":
            dummy_instance = cls(2)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = f"{cls.__name__}.json"

        if not os.path.exists(file_name):
            return []

        with open(file_name, "r") as file:
            json_string = file.read()

            list_dicts = cls.from_json_string(json_string)

            return [cls.create(**list_dict) for list_dict in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the json string represention in a csv file"""
        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.csv"
        json_string = cls.to_json_string(
            [one_object.to_dictionary() for one_object in list_objs])

        with open(file_name, "w") as file:
            file.write(json_string)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize, returns a list of instances"""
        file_name = f"{cls.__name__}.csv"

        if not os.path.exists(file_name):
            return []
        else:
            with open(file_name, "r") as file:
                json_string = file.read()

                list_dict = cls.from_json_string(json_string)

                return [cls.create(**one_list) for one_list in list_dict]
