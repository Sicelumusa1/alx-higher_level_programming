#!/usr/bin/python3
def common_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return set()
    
    set_3 = set_1.intersection(set_2)
    return set_3
