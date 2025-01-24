#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    value = set(my_list)
    for i in value:
        total += i
    return total
