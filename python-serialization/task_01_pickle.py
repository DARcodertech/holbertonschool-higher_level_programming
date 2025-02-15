#!/usr/bin/python3
"""
pickling custom class
"""


import pickle
"""import a pickle"""


class CustomObject:
    """pickling custom class"""
    def __init__(self, name, age, is_student):
        """initialize a class"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display a print"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize a class"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserialize a class"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
