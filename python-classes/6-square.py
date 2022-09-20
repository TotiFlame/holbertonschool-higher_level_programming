#!/usr/bin/python3
""" Task 6 """


class Square:
    """ square class """

    def __init__(self, size=0, position=(0, 0)):
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) is not int) or (type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            if i != 0:
                print("")
            for spaces in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
        print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
