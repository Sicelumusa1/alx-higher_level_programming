#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
        except IndexError:
            print("out of range")
            result.append(0)
            continue

        try:
            b = my_list_2[i]
        except IndexError:
            print("out of range")
            result.append(0)
            continue

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
             print("wrong type")
             result.append(0)
        elif b == 0:
            print("division by 0")
            result.append(0)
        else:
            result.append(a / b)
    return result
