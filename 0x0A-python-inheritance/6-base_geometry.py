#!/usr/bin/python3
"""defines a class for BaseGeometry class representation"""


class BaseGeometry:
    """Defines the class BaseGeometry"""

    def area(self):
        """
        Raises:
            Exception: if area method is not implemented
        """
        raise Exception("area() is not implemented")
