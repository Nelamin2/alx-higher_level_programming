#!/usr/bin/python3
"""a module for a text file-reading function."""


def read_file(filename=""):
    """a funtion to Print the contents of a UTF8 text file to stdout."""
    try:
        with open(filename, encoding="utf-8") as file:
            content = file.read()
            print(content, end="")
    except FileNotFoundError:
        pass
