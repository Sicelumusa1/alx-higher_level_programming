#!/usr/bin/python3
"""
Defines a function that writes an object to a text file using
JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
        my_obj: object to write
        filename (.txt): file to write in
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
