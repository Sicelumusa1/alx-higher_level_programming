#!/usr/bin/python3
"""
Defines a function that returns a list of all available 
attributes and methods of an object
"""
def lookup(obj):
    """
    Displays a list of list of all available attributes and 
    methods of an object

    Args:
        obj: The object to lookup

    Returns:
        Attributes and methods (list)
    """
    return dir(obj)
