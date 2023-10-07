#!/usr/bin/python3

"""This represents a rectangle"""


class Square:

    """"this is a class of  squarea"""
    def __init__(self, size=0):
        """"initializing attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):

        """function/method that squares up the size of the square"""
        return (self.__size ** 2)
