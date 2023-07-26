#! /usr/bin/python3

import sys


def arguments(parameter):
    length = len(parameter) - 1
    letter = "" if length == 1 else "s"
    symbol = "." if length == 0 else ":"
    print("{} argument{}{}".format(length, letter, symbol))
    i = 1
    if length > 0:
        while i < len(parameter):
            print("{}: {}".format(i, parameter[i]))
            i += 1


if __name__ == "__main__":
    arguments(sys.argv)
