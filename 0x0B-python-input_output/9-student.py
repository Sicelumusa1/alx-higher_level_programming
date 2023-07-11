#!/usr/bin/python3
"""Define a student class"""


class Student:
    """Define a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student attributes

        Attributes:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionery representation of a student

        Returns:
            dictionary representation of a student
        """
        return self.__dict__
