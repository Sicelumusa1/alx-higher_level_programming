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
