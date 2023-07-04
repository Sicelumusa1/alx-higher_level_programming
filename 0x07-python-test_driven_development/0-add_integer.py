#!/usr/bin/python3
"""This function add two integers and return their sum."""

def add_integer(a, b=98):
    """
    Computes the sum by adding two integers

    Args:
        a (int): first integer to add, if it is float it must be type casted
        b (int): second integer to add, if it is float it must be type casted

    Raises:
        TypeError: if the a and/or b are not float(s) or integer(s)

    Returns:
        int: The sum of 'a' and 'b'
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
