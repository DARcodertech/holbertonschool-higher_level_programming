#!/usr/bin/python3
"""import a json"""
import json
"""
write an object
"""


def save_to_json_file(my_obj, filename):
    """write an object"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
