#!/usr/bin/python3
"""module that that defines a rectangle"""


class Rectangle:
    """defining a rectangle class"""

    def __init__(self, width=0, height=0):

        """a class constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):

        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):

        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):

        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """ calculate area of a rectangle"""
        return self.__width * self__height

    def perimeter(self):

        """ calculate perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):

        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width + "\n"
        return "{}".format(rect[:-1])

    def __repr__(self):

        """Return a string representation that can recreate a new
        instance."""
        return "Rectangle({}, {})".format(
                self.__width, self.__height)
