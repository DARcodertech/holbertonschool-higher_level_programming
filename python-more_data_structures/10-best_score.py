#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    new_key = None
    new_value = float('-inf')
    for i, value in a_dictionary.items():
        if value > new_value:
            new_value = value
            new_key = i
    return new_key
