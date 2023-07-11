#!/usr/bin/python3
"""defines a function that creates an object from a JsoN file"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JsoN file

    Args:
        filename: file to create the object from
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
