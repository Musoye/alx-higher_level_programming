#!/usr/bin/python3
"""The square model, let's write"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square model"""

    def __init__(self, size, x=0, y=0, id=None):
        """The constructor class for the square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """update the print for square"""
        value = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width)
        return (value)

    @property
    def size(self):
        """getter of size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value
