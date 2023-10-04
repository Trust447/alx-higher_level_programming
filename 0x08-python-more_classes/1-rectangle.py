#!/usr/bin/python3

'''defining a rectangle'''


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width = 0, height = 0):
        """Initializing this rectangle class"""

        self.__width = width
        self.__height = height
    def width(self):
        """width getter method"""

        return self.__width

    def width(self, value):
        """width setter method"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """height getter method"""

        return self.__height

    def height(self, value):
        """height setter method"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
