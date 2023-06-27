#!/usr/bin/python3
"""
Defines the square class
"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The positin of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object with a given size

        Args:
            size (int): the size of the square (default is 0)
            position (tuple): the position of teh square

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Modifies the value of the square size

        Args:
            value (int):The new size value has to be int and > 0
        Raises:
            TypeError: if the value is not an integer.
            ValueError; if  the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        retrieves the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Modifies the value of the square position

        Args:
            value (taple): The new position value has to be a tuple of 2
            positive integers.
        Raises:
            TypeError: if the value is not a taple or not containing 2
            positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = value
        if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of a square.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' character
        If the siz eis 0, prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
