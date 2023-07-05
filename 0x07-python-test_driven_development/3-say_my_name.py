#!/usr/bin/python3
"""
Defines a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name (first name and last name) given.

    Args:
        first_name (str): name to print
        last_name (str): 2nd name to print

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
