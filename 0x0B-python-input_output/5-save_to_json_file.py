#!/usr/bin/python3


import json


"""
module that defines a function that writes an
Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):

    """function that writes an
    Object to a text file, using a JSON representation"""

    with open(filename, "w") as fil:
        return json.dump(j_obj, fil)
