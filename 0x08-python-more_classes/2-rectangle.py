#!/usr/bin/python3
"""Module3-rectangle
DefinesaRectangleclass.
"""


classRectangle:
    """Rectangleclassdefinedbywidthandheight."""

    def__init__(self, width=0, height=0):
        """InitializesaRectangleinstance.
        Args:
        width:widthoftherectangle
        height:heightoftherectangle
        """
        self.width = width
        self.height = height

    def__str__(self):
        """Returnsaninformalandnicelyprintablestringrepresentation
        ofaRectangleinstance,filledwiththe'#'character."""
        ifself.__height == 0 orself.__width == 0:
            return''
    rec_str = ''
    for i in range(self.__height):
        for j in range(self.__width):
            rec_str += '#'
    rec_str + = '\n'
    returnrec_str[:-1]

    @property
    defwidth(self):
        """RetrievesthewidthofaRectangleinstance."""
    returnself.__width

    @width.setter
    def width(self, value):
        """SetsthewidthofaRectangleinstance
        Args:
        value:valueofthewidth,mustbeapositiveinteger
        """
        if not isinstance(value, int):
            raise TypeError("width must bean integer")
        if value < 0:
            raise ValueError("widthmustbe > = 0")
        self.__width = value

    @property
    def height(self):
        """RetrievestheheightofaRectangleinstance."""
        return self.__height
