#!/usr/bin/python3
"""Rectangle inherit from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle an instance of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor method"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set he height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) != int:
           raise TypeError("x must be an integer")
        if value < 0:
           raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
