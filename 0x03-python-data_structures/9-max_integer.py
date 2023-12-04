#!/usr/bin/python3

def max_integer(my_list=None):
    if my_list is None:
        my_list = []

    my_list.sort()
    my_list.reverse()
    return my_list[0]
