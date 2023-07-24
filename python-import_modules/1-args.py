#!/usr/bin/python3

if __name__ == "__main__":
    def arguments(*args):
        length = len(args)
        letter = "" if length == 1 else "s"
        symbol = "." if length == 0 else ":"
        print("{} argument{}{}".format(length, letter, symbol))
        if length > 0:
            i = 1
            for arg in args:
                print("{}: {}".format(i, arg))
                i += 1
