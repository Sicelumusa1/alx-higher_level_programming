#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return None

    length = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            length += 1
    except IndexError:
        pass
    print()
    return length
