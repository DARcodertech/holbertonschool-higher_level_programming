#!/usr/bin/python3
"""import a json"""
import json
"""
make an object
"""


def load_from_json_file(filename):
    """make an object"""
    with open(filename, 'r') as f:
        return json.load(f)
