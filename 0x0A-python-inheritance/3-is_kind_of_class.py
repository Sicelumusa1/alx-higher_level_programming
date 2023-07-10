#!/usr/bin/python3
"""Defines a function that checks if an object belongs into a class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class
    inherited

    Args:
        obj: object to check
        a_class: class to compare

    Returns:
        bool: True if the object is an instance of a class inherited
              False otherwise
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
