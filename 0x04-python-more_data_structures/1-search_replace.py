#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or len(my_list) == 0:
        return None
    
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
