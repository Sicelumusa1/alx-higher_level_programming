#!/usr/bin/python3
"""defines a fuction that appends a string a the end of a text file"""


def append_write(filename="", text=""):
    """
    Appends a string  athe end of a text file and returns a number of
    characters added

    Args:
        filename (.txt): name of the file to append a string on
        text (str): the string to append
    Returns:
        number of characters (int): number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        count = 0
        for i in range(len(text)):
            app_f = f.write(text[i])
            count += 1
        return count
