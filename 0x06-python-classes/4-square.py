#!/usr/bin/python3

"""module that defines a rectangle"""


class Square:

    def __init__(self, size=0):
        """initializing attributes"""
        self.__size = size

    @property
    def size(self):
        """method to get value of object"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set value of object"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
