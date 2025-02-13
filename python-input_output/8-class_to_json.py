#!/usr/bin/python3
"""
return a dictionary
"""


def class_to_json(obj):
    """return a dictionary"""
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
