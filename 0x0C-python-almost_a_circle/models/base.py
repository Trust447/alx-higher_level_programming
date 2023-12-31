#!/usr/bin/python3
"""
a module that has the base of other classes in the project
"""
import json


class Base:

    """base class of other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):

        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
