#!/usr/bin/python3
"""writing the base class"""


class Base:
    """writing the base class of this model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method

        Args:
            id : the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
