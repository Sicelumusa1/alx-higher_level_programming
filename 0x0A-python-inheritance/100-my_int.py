#!/usr/bin/python3
"""Defines a class that inherits the int class"""


class MyInt(int):
    """
    A rebellious integer that inherits the int class
    The == and != opoerators are inverted for instances of MyInt

    Attributes:
        Inherits all attributes of the int class

    Methods:
        __eq__(self, other): overrides the == operator and inverts its
                             behavior
        __ne__(self, other): overrides the != operator and inverts its
                             behavior
    """

    def __eq__(self, other):
        """
        Overrides the == operator and inverts its behavior

        Args:
            other (int): value to compare with

        Returns:
            bool: True if the values are not equal, False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator and inverts its behavior

        Args:
            other (int): value to compare with

        Returns:
            bool: True if the values are equal, False otherwise
        """
        return super().__eq__(other)
