#!/usr/bin/python3
'''_____MODULE_____'''


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
