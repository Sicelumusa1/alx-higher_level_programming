#!/usr/bin/python3
"""Defines text_indentation"""


def text_indentation(text):
    """Prints a text with 2 new line after each of: ., ? and :

    Args:
        text (str): the text to be indented

    Raises:
        TypeError: if the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    
    while i < len(text):
        print(text[i], end="")
        if text[i] == '\n' or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            if i >= len(text):
                break
            continue
        i += 1
