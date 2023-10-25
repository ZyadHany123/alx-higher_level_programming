#!/usr/bin/python3

"""class square."""


class Square:
    """square."""

    def __init__(self, size=0, position=(0, 0)):
        """ new square """

        self.position = position
        self.size = size

    @property
    def size(self):
        """get value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setvalue """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getpos"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set pos"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ square area """
        return (self.__size ** 2)

    def my_print(self):
        """print square"""
        if not self.__size:
            print("")
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
