#!/usr/bin/python3

"""
module that defines a function that checks if
an object is an instance of a class
"""


def inherits_from(obj, a_class):

    """function that checks if
    an object is an instance of a class"""
    return issubclass(type(obj), a_class) and not a_class
