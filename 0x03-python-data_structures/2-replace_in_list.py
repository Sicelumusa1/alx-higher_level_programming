#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list is None or len(my_list) == 0:
        return None

    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
