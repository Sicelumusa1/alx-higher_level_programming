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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionery representation of a student
        
        Args:
            attrs (list): list of attribute names to retrieve

        Returns:
            dictionary representation of a student
        """
        if attrs is None:   #retrieve all attributes
            return self.__dict__
        else: #retrieve the specified attributes
            return {attr: getattr(self, attr) 
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance using a dictionary

        Args:
            json (dict): dictionary containing attribute-value pair
        """
        for attr, value in json.items():
            setattr(self, attr, value)
