#!/usr/bin/python3


"""
module that defines a function that returns the JSON
representation of an object (string)
"""


json = __import__(json).json


def to_json_string(my_obj):

    """function that returns the JSON representation of an object"""
    return json.dumps(my_obj)
