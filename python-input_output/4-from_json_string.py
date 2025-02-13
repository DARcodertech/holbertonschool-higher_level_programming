#!/usr/bin/python3
"""import a json"""
import json
"""
return an object
"""


def from_json_string(my_str):
    """return an object"""
    return json.loads(my_str)
