#!/usr/bin/python3


"""
module that defines a rectangle class
"""


class Rectangle(7-base_geometry.BaseGeometry):

    """ creating a rectangle class"""

"""constructor"""
    
    def __init__(self, width, height):


        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("must be an int")
        if value < 0:
            raise ValueError("must be greater than 0")
        self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("must be an int")
            if value < 0:
                raise ValueError("must be greater than 0")
            self.__height = value

        def area(self):
            """Returns the area of the rectangle"""
            return (self.__width * self.__height)

        def perimeter(self):
            """Returns the perimeter of the rectangle"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) + (self.__height * 2))

        def __str__(self) -> str:
            """presents a diagram of the rectangle defined for an object"""
            if self.__width == 0 or self.__height == 0:
                return ("")
            rectangle = ""
            for column in range(self.__height):
                for row in range(self.__width):
                    try:
                        rectangle += str(self.print_symbol)
                    except Exception:
                        rectangle += type(self).print_symbol
                        if column < self.__height - 1:
                            rectangle += "\n"
                            return (rectangle)

                        def __repr__(self)
                        """returns a string representation of the rectangle"""
                        return "Rectangle({:d}, {:d})".format(self.__width,
                            self.__height)

                    def __del__(self):
                        """prints a message for every object that is deleted"""
                        print("Bye rectangle...")
                        Rectangle.number_of_instances -= 1
