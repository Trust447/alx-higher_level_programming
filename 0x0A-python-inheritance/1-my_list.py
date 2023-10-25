#!/usr/bin/python3
"""
module with a method that prints lists in sorted form
"""


class MyList(list):

    """method that prints lists in a sorted form"""
    def print_sorted(self):
        print(sorted(self))
