#!/usr/bin/python3
"""
Defines a Square class
"""
class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.
       
       Args:
            size (int): the size of the square (default is 0).
        
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size    
