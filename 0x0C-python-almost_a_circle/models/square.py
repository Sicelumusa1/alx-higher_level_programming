#!/usr/bin/python3
"""Defines the square class that inherits from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Retrieves the value of the size of the square

        Returns:
            int: the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the size of the square

        Args:
            value (int): new size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assignes the attributes

        Args:
            *args:  list of arguments - no-keyworded arguments
                    1st argument should be the id attribute
                    2nd argument should be the size attribute
                    3rd argument should be the x attribute
                    4th argument should be the y attribute
            **kwargs: Dictionery of keyworded arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square

        Returns:
            dict: the dictionary representation of the square
        """
        return {'id': self.id, 'size': self.width,'x': self.x, 'y': self.y}
