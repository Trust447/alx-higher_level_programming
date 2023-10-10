#!/usr/bin/python3


"""
module that defines a function that returns an object
(Python data structure) represented by a JSON string
"""


def from_json_string(my_str):

    """function that returns an object
    (Python data structure) represented by a JSON string"""
    return jason.load(my_str)
