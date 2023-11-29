#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
                print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(char), end="")

