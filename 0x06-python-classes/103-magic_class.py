#!/usr/bin/python3
import math
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""
class MagicClass:
    """Represent a circle."""
    def __init__(self, radius=0):
        """Initialize a MagicClass
        Arg:
            radius (float or int): The radius of the new MagicClass."""
        self.__radius = 0
         if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi
        """Return the area of the MagicClass."""
    def circumference(self):
        return 2 * math.pi * self.__radius
        """Return The circumference of the MagicClass."""
