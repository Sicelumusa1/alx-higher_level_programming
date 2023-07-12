#!/usr/bin/python3
"""Defines a function tha iserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string

    Args:
        filename: name of the file to modify
        search_string (str): String to search for and add text after
        new-string (str): string to append after each occurence of
                          the search_string
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
