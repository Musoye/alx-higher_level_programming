#!/usr/bin/python3
"""The square module continue"""


class Square:
    """The class to create square."""

    def __init__(self, size=0, position=(0,0)):
        """set size to private instance variable

        Args:
            size (int): the size of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """get the area of the square

        Args:
            None

        Returns:
            Area of the square(int)
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """getter that get size variable"""
        return (self.__size)

    @property
    def position(self):
        """getter that get the position variable"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """resert the position

        Args:
            value: the position
        """
        if (not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num > 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """Set thesize to the value

        Args:
            value: the value to reset
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print square form the size"""
        value = self.__size
        if value == 0:
            print("")
            return

        [print("") for m in range(self.__position[1])]
        for i in range(value):
            [print(' ', end='') for k in range(self.__position[0])]
            [print('#', end='') for j in range(value)]
            print('')
