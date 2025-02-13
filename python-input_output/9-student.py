#!/usr/bin/python3
"""
define a student
"""


class Student:
    """define a student"""
    def __init__(self, first_name, last_name, age):
        """init a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """return a student"""
        return{
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }