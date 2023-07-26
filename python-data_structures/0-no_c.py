#!/usr/bin/env python3

def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char == "c" or char == "C":
            continue
        else:
            new_string += char
    else:
        return new_string
