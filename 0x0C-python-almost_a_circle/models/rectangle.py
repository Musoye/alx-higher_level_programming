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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """dispaly to the stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """print statement"""
        value = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height)
        return (value)
