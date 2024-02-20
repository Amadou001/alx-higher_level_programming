#!/usr/bin/python3
"""______MODULE_______"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Initialize an empty dictionary to store the serialized data
    serialized_data = {}

    # Iterate over the attributes
    for attr_name, attr_value in attributes.items():
        # Check if the attribute value is serializable
        if isinstance(attr_value, (list, dict, str, int, bool)):
            serialized_data[attr_name] = attr_value
        elif isinstance(attr_value, object):
            # Recursively serialize nested objects
            serialized_data[attr_name] = class_to_json(attr_value)

    return serialized_data
