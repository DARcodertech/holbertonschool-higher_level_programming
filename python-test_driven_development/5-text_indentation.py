#!/usr/bin/python3
"""
function that print a text
"""
def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ?, :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    skip = True
    for i in text:
        result += i
        if i in ".?:":
            result += "\n\n"
            skip = True
        elif i == " " and skip:
            result = result[:-1]
        else:
            skip = False
    print(result, end="")
