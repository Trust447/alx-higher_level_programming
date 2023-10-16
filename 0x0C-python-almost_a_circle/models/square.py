#!/usr/bin/python3


from models.rectangle import Rectangle

"""
module that defines a square class which is a
sub class of the rectangle class
"""


class Square(Rectangle):

    """a square class"""
    def __init__(self, size, x=0, y=0, id=None):

        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of instance"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height)

    @property
    def size(self):

        """public getter for height or width (size)"""
        return self.height

    @size.setter
    def size(self, size):

        """public setter for height or width (size)"""
        self.height = size
        self.width = size

    def update(self, *args, **kwargs):

        """assign attributes to args or kwargs"""
        if args:
            if len(args) >= 1:
                args[0] = self.id
            if len(args) >= 2:
                args[1] = self.size
            if len(args) >= 3:
                args[2] = self.x
            if len(args) >= 4:
                args[3] = self.y
        else:
            if 'id' in kwargs:
                kwargs['id'] = self.id
            if 'size' in kwargs:
                kwargs['size'] = self.size
            if 'x' in kwargs:
                kwargs['x'] = self.x
            if 'y' in kwargs:
                kwargs['y'] = self.y

    def to_dictionary(self):

        """method that returns the dictionary
        representation of a Square"""
        return {
                'id': self.id, 'size': self.height,
                'x': self.x, 'y': self.y
                }
