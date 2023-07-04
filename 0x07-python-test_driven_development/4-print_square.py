#!/usr/bin/python3
"""Defines a function that prints a squire"""

def print_square(size):
    """
    Prints a quare with the character #.

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if isinstance(size, float):
        raise TypeError('size must be an integer')

    if  size < 0:
        raise ValueError('size must be >= 0')

    if size == 0:
        print("")
    else:
        for i in range(size):
            print("#" * size)
