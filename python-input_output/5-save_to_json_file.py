#!/usr/bin/python3
import json
"""
write an object
"""


def save_to_json_file(my_obj, filename):
    """write an object"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
