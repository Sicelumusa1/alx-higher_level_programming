#!/usr/bin/python3
"""Defines a fuction checking if object belongs to a clas"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj: object to check
        a_class: class to compare against

    Returns:
        bool: True if an object is exactly an instance of the specified class
              False otherwise
    """
    return type(obj) is a_class
