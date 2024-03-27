#!/usr/bin/python3


def find_peak(list_of_integers):

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = int(len(list_of_integers) / 2)

    if mid != len(list_of_integers) - 1:
        if list_of_integers[mid - 1] < list_of_integers[mid] and\
           list_of_integers[mid + 1] < list_of_integers[mid]:
            return list_of_integers[mid]
    else:
        if list_of_integers[mid - 1] < list_of_integers[mid]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid - 1]

    if list_of_integers[mid - 1] > list_of_integers[mid]:
        a_list = list_of_integers[0:mid]
    else:
        a_list = list_of_integers[mid + 1:]

    return find_peak(a_list)
