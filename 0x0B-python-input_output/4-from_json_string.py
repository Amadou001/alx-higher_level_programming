#!/usr/bin/python3
'''_____MODULE______'''


import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.
    """
    return json.loads(my_str)
