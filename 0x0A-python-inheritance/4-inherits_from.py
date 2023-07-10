#!/usr/bin/python3
"""
Defines a function that heck if an object is an instance of a 
class that inherited
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited 
    (directly or indirectly) the specified class

    Args: 
        obj: object to check
        a_class: class to compare agaist

    Returns:
        bool: True is the object is an instance of a class inheritance, 
              False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
