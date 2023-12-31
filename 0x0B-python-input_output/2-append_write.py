#!/usr/bin/python3


"""
module that defines a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):

    """function that appends a string at the end of a text file
    and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as fil:
        return fil.write(text)
