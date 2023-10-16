#!/usr/bin/python3
from models.base import Base


"""
module that defines a rectangle class that inherits
from Base
"""


class Rectangle(Base):

    """a rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):

        """constructor for the instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):

        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):

        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):

        """ height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):

        """ x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):

        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):

        """ y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def __str__(self):

        """class constructor"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def area(self):

        """method that clculates the area of a rectangle"""
        return self.height * self.width

    def display(self):

        """Prints out the rectangle to the screen."""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):

        """assigning attributes to args"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if kwargs:
                if 'id' in kwargs:
                    kwargs['id'] = self.id
                if 'width' in kwargs:
                    kwargs['width'] = self.width
                if 'height' in kwargs:
                    kwargs['height'] = self.height
                if 'x' in kwargs:
                    kwargs['x'] = self.x
                if 'y' in kwargs:
                    kwargs['y'] = self.y

    def to_dictionary(self):

        """pulic method that returns the dictionary
        representation of a Rectangle"""
        return {
                'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y
                }
