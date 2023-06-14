#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return 0

    result = 0
    unique_list = []
    for num in my_list:
        if num not in unique_list:
            unique_list.append(num)
    for i in unique_list:
        result += i
    return result
