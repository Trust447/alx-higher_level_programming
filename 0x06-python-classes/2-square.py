#!/usr/bin/python3

"""module that defines a square"""

class Square:
"""A class that represents a square"""

    def __init__(self, size=0):
        """initializing attributes"""
        self.__size = size

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
