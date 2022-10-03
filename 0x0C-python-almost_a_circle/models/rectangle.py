#!/usr/bin/python3
"""
module Rectangle
"""


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super.__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    """getter y"""
    def y(self):
        return self.__y

    @y.setter
    """"setter y"""
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print a display of the rectangle"""
         print(("\n" * self.__y) +

                               "\n".join(((" " * self.__x) + ("#" * self.__width))

                                                           for i in range(self.__height)))
    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args):
        """update the attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.__id = a
                elif i == 1:
                    self.__width = a
                elif i == 2:
                    self.__height = a
                elif i == 3:
                    self.__x = a
                elif i == 4:
                    self.__y = a
