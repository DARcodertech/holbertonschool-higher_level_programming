#!/usr/bin/env python3
"""
basic serialization module
"""
import json
"""import a json"""


def serialize_and_save_to_file(data, filename):
    """serialize and save to file"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """load and deserialize"""
    with open(filename 'r') as f:
        return json.load(f)
