#!/usr/bin/python3
"""Defines a list class representstion"""


class MyList(list):

    """Class that inherits the list the built-in list class"""
    def print_sorted(self):
        """
        Prints the sorted version of the list

        Returns:
            list: The sorted version of the list
        """
        sorted_list = sorted(self)
        print(sorted_list)
