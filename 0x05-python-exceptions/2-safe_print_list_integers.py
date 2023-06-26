#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return None
    length = 0

    try:
        index = 0
        while my_list and my_list[index:]:
            if index < x:
                try:
                    value = my_list[index]
                    if isinstance(value, int):
                        print("{:d}".format(value), end='')
                        length += 1
                except IndexError:
                    break
            else:
                break
            index += 1
    except (ValueError, TypeError):
        pass
    print()
    return length
