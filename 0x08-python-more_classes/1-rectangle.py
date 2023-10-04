#!/usr/bin/python3

'''defining a rectangle'''


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter method"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def __str__(self):
        """Custom string representation of the Rectangle object"""
        return f"Rectangle(width={self.__width}, height={self.__height})"
