#!/usr/bin/python3
"""Defines a base class"""

import json


class Base:
    """
    Base of all other classes in the project

    Attributes:
        __nb_objects: class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a public attribute

        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into its JSON string representation

        Args:
            list_dictionaries (list of dict or None):List of dict to covert

        Returns:
            str: JSON string representation of the list of dict or None if
            list is None or empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the json string rep of list_objs to a file

        Args:
            list_objs (list): List of instances that inherit from Base
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string rep into a list of dictionaries

        Args:
        json-string (str): JSON string rep

        Returns:
            list: List of dictionaries by the JSON string or empty list if
            json_string is None or empty
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set
        based on the dictionary provided

        Args:
            **dictionary: contains the attribute-value pairs

        Returns:
            Base: an instance of the class with attributes set 
            based on the dictionary
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'square':
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """
        Update the attributes of the instance based on arguments provided

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments representing attribute-value pairs
        """
        if len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1 and isinstance(self, Rectangle):
                    self.width = arg
                elif index == 1 and isinstance(self, Square):
                    self.size = arg
                elif index == 2 and isinstance(self, Rectangle):
                    self.height = arg
                elif index == 2 and isinstance(self, Square):
                    self.size = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """
        Load JSON data from a file and return a list of instances

        Returns:
            list: list of instances created from the JSON data
                if a file does not exist, an empty list is returned
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                json_data = f.read()
                dictionaries = cls.from_json_string(json_data)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []
