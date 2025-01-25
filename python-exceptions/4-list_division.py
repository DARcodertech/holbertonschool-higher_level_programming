#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    total = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if not isinstance(my_list_1[i], (int, float)) or \
                    not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
            divised = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            divised = 0
        except TypeError as e:
            print(e)
            divised = 0
        except IndexError as e:
            print(e)
            divised = 0
        finally:
            total.append(divised)
    return total
