#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = None
    best_score = 0
    for key, value in a_dictionary.items():
        if value is None:
            return None
        if value > best_score:
            best_key = key
            best_score = value
    return best_key
