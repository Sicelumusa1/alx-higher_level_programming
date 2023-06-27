#!/usr/bin/pycode3
"""
Defines the square class
"""


class Square:
    """
    A class representing a square

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a square object with a given size.

        Args:
            size (int): the size of the square (default is 0).

        Raises:
            TypeError: if the value is not a integer.
            ValueError: if the value is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must  be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of a square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
