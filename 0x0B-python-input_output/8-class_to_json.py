#!/usr/bin/python3
"""Defines a function that returns the dictionary 
description with simple data structure
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: an instance of a Class

    Returns:
        dictionary description with simple data structure
    """
    return obj.__dict__
