#!/usr/bin/python3
'''____MODULE_____'''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list(filename, *args):
    try:
        # Load existing items from file if it exists
        items = load_from_json_file(filename)
    except FileNotFoundError:
        # If file doesn't exist, initialize an empty list
        items = []

    # Add new items to the list
    items.extend(args)

    # Save the updated list to the file
    save_to_json_file(items, filename)


if __name__ == "__main__":
    # Ignore the first argument, which is the script name
    arguments = sys.argv[1:]

    # Add the arguments to the list and save to file
    add_items_to_list("add_item.json", *arguments)
