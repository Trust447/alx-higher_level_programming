#!/usr/bin/python3

"""
module that defines a function that read text files and prints them out
"""


def read_file(filename=""):

    """a function that reads text files and prints it to stdout"""
    with open(filename, encoding='utf-8') as fil:
        f = fil.read()
    print(f, end="")
