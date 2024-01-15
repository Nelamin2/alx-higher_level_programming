#!/usr/bin/python3
''' Rectangle class module'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes("hight", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attributes("y", value)
        self.__y = value

    def validate_attributes(self, name, value, eq=True):
        '''Method for validating the entered value.'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''returns the area of the rectangular'''
        return self.width * self.heigh

    def display(self):
        '''Prints string representation of this rectangle.'''
        for i in range(self.height):
            print("#" * self.width)
