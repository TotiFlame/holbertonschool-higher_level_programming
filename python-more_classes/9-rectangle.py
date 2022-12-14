#!/usr/bin/python3
""" module """


class Rectangle:
    """ Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ret_str
        for i in range(self.__height):
            if i != 0:
                ret_str += '\n'
            for j in range(self.__width):
                if type(self.print_symbol) != str:
                    self.print_symbol = str(self.print_symbol)
                ret_str += self.print_symbol
        return ret_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        r_1 = Rectangle.area(rect_1)
        r_2 = Rectangle.area(rect_2)
        if r_1 >= r_2:
            return rect_1
        elif r_1 < r_2:
            return rect_2

    def square(cls, size=0):
        new_rect = Rectangle(cls, cls)
        return new_rect
