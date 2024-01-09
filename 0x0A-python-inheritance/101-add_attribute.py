#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attribute, value):
    """Add attribute to object if possible.

    Args:
        obj: The object.
        attribute: The attribute to add.
        value: The value for the attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__") and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
