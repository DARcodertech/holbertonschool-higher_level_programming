#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous_value = 0
    for i in roman_string:
        current_value = roman_number.get(i, 0)
        if current_value > previous_value:
            total += current_value - 2 * previous_value
        else:
            total += current_value
        previous_value = current_value
    return total
