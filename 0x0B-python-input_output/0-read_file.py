#!/usr/bin/python3
"""Defines a function that reads a file and prints to stdout"""


def read_file(filename=""):
    """
    Reads a txt file and prints to stdout

    Args:
        filename: name of the file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_f = f.read()
        print(read_f)
