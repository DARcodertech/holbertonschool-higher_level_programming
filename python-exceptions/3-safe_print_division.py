#!/usr/bin/python3
def safe_print_division(a, b):
    total = None
    try:
        total = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(total))
    return total
