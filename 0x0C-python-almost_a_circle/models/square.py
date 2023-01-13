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

    def update(self, *args, **kwargs):
        """update the attribute based on variable/keyword argument"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0: 
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return the dictionary representa... of attr..."""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
