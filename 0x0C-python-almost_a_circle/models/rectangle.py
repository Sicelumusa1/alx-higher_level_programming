#!/usr/bin/python3
"""Defines a rectangle class that inherites from Base"""

from models.base import Base


class Rectangle(Base):
    """Inherits class base attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance attributes

        Args:
            width: width of a rectangle
            height: height of the rectangle
            x: x coordinate
            y: y coordinate
            id: rectangle id
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieves the value of the width property
        of the rectangle

        Returns:
            The width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Assignes a new value to the width property of
        the rectangle

        Args:
            value: new value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of the height property
        of the rectangle

        Returns:
        The height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Assignes a new value to the height property of
        the rectangle

        Args:
            value: new value of the height

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves the value of the x property
        of the rectangle

        Returns:
            The x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Assignes a new value to the x property of
        the rectangle

        Args:
            value: new value of x

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the value of the y property
        of the rectangle

        Returns:
            The y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Assignes a new value to the y property of
        the rectangle

        Args:
            value: new value of y

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the rectangle instance

        Returns:
            area
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle in stdout with # character
        taking into account the x and y position
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Returns the string representation of the rectangle instance

        Returns:
            the string representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update the rectangle attributes

        Args:
            *args: Variable length positional arguments
            **kwargs: Variable length keyword arguments
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle

        Returns:
            dict: the dictionary representation of the rectangle
        """
        return {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
