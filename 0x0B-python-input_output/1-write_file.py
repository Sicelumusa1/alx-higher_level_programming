#!/usr/bin/python3
"""Defines  a function that writes a string to a file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns a number of
    characters written

    Args:
        filename (.txt): name of the file to write in
        text (str): string to write in the file
    Returns:
        number of characters (int): number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        count = 0
        for i in range(len(text)):
            write_f = f.write(text[i])
            count += 1
        return count
