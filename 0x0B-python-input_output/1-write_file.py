#!/usr/bin/python3


"""
module that defines a function that writes into a file
"""


def write_file(filename="", text=""):

    """function that writes a string to a text file
    and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as fil:
        f = fil.write(text)
        return f
