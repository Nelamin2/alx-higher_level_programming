#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            sub += n

    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman.keys())

    sum= 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if roman.get(ch) <= last_rom:
                    sum += to_subtract(list_num)
                    list_num = [roman.get(ch)]
                else:
                    list_num.append(roman.get(ch))

                last_rom = roman.get(ch)

    sum += to_subtract(list_num)

    return (sum)
