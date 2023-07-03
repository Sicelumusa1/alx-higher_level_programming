#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    A class representing a Rectangle

    Attributes:
        width (int): the width of a rectangle
        height (int): the height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes width and height of a rectangle

        Args:
            width (int): the width of a rectangle
            height (int): the height of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieves the value of the given width

        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than 0

        Return:
            width (int)
        """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, value):
        """
        Modifies the value of the given width

        Args:
            value (int): the new value of the width

        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of the given height

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0

        Return:
            height (int)
        """
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, value):
        """
        Modifies the value of the given height

        Args:
            value (int): the new value of the height

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of a rectangle by multiplying width and height

        Returns:
            Area (int): the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of a rectangle by multiplying 2 by sum
        of width and height

        Returns:
            perimeter (int): if neither width nor height = 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
