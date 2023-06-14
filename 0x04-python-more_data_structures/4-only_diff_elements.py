#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None

    if len(set_1) == 0 or len(set_2) == 0:
        return set()
    set_3 = set_1.symmetric_difference(set_2)
    return set_3
