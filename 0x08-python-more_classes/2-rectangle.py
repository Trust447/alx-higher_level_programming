#!/usr/bin/python3
"""
the module defines a rectangle
"""


class Rectangle:

    """creating a rectangle class"""

    def __init__(self, width=0, height=0):

        """ class constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """calculate area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):

        """calculate perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
