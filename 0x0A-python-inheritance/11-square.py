#!/usr/bin/python3
"""defines a class for BaseGeometry class representation"""


class BaseGeometry:
    """Defines the class BaseGeometry"""

    def area(self):
        """
        Computes the area of the geometry
        Raises:
            Exception: if area method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value of the given dimension

        Args:
            name (str): name of the dimension
            value (int): vale of the dimension

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an interger")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, which is a subclass of BaseGeometry

    Attributes:
        __width (int): the width of the rectangle
        __height (int): the  height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the  height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is <= 0
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of a rectangle

        Returns:
            int: computed area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representstion of the rectangle

        Returns:
            str: the string representstion of the rectangle in format
                 [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns the official string representation of the rectangle

        Returns:
            str: the official string representation of the rectangle
        """
        return self.__str__()


class Square(Rectangle):
    """
    Represents a square, which is a subclass of rectangle

    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size):
        """
        Initializes a new instance of square class

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is <= 0
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square

        Returns:
            int: the computed area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the square

        Returns:
        str: the string representation of the square in format [square]
             <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """
        Returns the official string representation of the square

        Returns:
            str: the official string representation of the square
        """
        return self.__str__()
