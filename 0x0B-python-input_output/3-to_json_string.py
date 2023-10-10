#!/usr/bin/python3


"""
module that defines a function that returns the JSON
representation of an object (string)
"""


jsn = __import__(jason).jason


def to_json_string(my_obj):

    """function that returns the JSON representation of an object"""
    return jason.dumps(my_obj)
