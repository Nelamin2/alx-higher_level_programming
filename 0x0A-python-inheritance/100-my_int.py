#!/usr/bin/python3
""" A module Contains the class MyInt. """


class MyInt(int):
    """ A rebel class of int """
    def __eq__(self, other):
        """ Invert the behavior of == """
        return super().__ne__(other)

    def __ne__(self, other):
        """  Invert the behavior of != """
        return super().__eq__(other)
