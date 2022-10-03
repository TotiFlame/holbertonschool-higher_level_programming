#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """  Square class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
                else:
                    return
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
            else:
                return

    def to_dictionary(self):
        dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dict
