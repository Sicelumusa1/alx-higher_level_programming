#!/usr/bin/python3
"""Defines a function a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible

    Args:
        obj (object): object to add the attribute to
        attr_name (str): name of the attribute
        attr_value (any): value of the attribute

    Raises:
        TypeError: if the object cannot have a new attribute
    """
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
